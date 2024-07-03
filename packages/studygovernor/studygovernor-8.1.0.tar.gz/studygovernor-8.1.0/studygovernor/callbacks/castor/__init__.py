# Copyright 2017 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import netrc
import re
import traceback
from typing import Any, Dict, List, Optional, Union
import urllib.parse

import taskclient
import xnat
import yaml
from jsonpointer import resolve_pointer

from .connection import CastorConnection
from .utils import pprint

JSONType = Union[None, int, str, bool, List[Any], Dict[str, Any]]


def download_latest_file_version(session: xnat.XNATSession, url: str) -> JSONType:
    """
    Download the latest version of a file on XNAT that has a {timestamp} wildcard in the
    URI.

    :param session: The XNAT session to use
    :param url: The URL of the file te download
    :return: The JSON-parsed content of the file
    """
    split_url = urllib.parse.urlparse(url)
    path = split_url.path

    resource, filename = path.split('/files/')
    print('Found desired filename: {}'.format(filename))
    if '{timestamp}' in path:
        pattern = filename.format(timestamp=r'(_?(?P<timestamp>\d\d\d\d\-\d\d\-\d\dT\d\d:\d\d:\d\d(\.\d+)?)_?)?') + '$'

        # Query all files and sort by timestamp
        files = session.get_json('{}/files'.format(resource))
        files = [x['Name'] for x in files['ResultSet']['Result']]
        print('Found file candidates {}, pattern is {}'.format(files, pattern))
        files = {re.match(pattern, x): x for x in files}
        files = {k.group('timestamp'): v for k, v in files.items() if k is not None}
        print('Found files: {}'.format(files))

        if len(files) == 0:
            return None

        # None is the first, timestamp come after that, so last one is highest timestamp
        latest_file = sorted(files.items())[-1][1]
        print('Select {} as being the latest file'.format(latest_file))

        # Construct the correct path again
        path = '{}/files/{}'.format(resource, latest_file)

    data = session.get_json(path)

    return data


def collect_fields(template: JSONType, data: JSONType):
    result = {}
    for field, description in template.items():
        if field not in data:
            continue

        if description['control'] == 'TabsWidget':
            for tab_name, content in description['content'].items():
                print(f"Descending into {field}/{tab_name}")
                field_result = collect_fields(content, data[field])
                result.update(field_result)
            continue

        if description['control'] == 'BoxWidget':
            print(f"Unpacking {field} box")
            field_result = collect_fields(description['content'], data[field])
            result.update(field_result)
            continue

        if description['control'] == 'ListingWidget':
            print(f"Processing {field} listing")
            listing_data = []
            for entry in data[field]:
                listing_data.append(collect_fields(description['content'], entry))
            result[field] = listing_data

            # Add the counts
            count_field = f'{field}_count'

            print(f"Adding count field {count_field} with value {len(data[field])}")
            result[count_field] = len(data[field])
            continue

        if description['control'] == 'MarkerEdit':
            field_data = data[field]

            if isinstance(field_data, list) and len(field_data) == 1:
                print(f"Splitting {field} marker: {field_data}")
                field_data = field_data[0]
                result[f'{field}_x'] = field_data['pos'][0]
                result[f'{field}_y'] = field_data['pos'][1]
                result[f'{field}_z'] = field_data['pos'][2]
            else:
                print(f"Cannot split {field} marker, not a single marker: {field_data}")
                result[field] = field_data

            continue

        result[field] = data[field]
    return result


def castor(callback_execution_data,
           config: Dict[str, Any],
           field_files: Union[str, List[str]],
           templates: Union[str, List[str]],
           castor_study_name: str,
           castor_site_name: str,
           castor_visit_name: str,
           extra_variable_map: Optional[Dict[str, str]] = None,
           translation_map: Optional[Dict[str, str]] = None,
           xnat_external_system: str = 'XNAT',
           castor_external_system_name: str = 'CASTOR',
           taskmanager_external_system_name: str = 'TASKMANAGER',
           **ignore):
    """
    Create taskmanager task

    :param callback_execution_data: callback execution data
    :param config: flask app configuration dict
    :param field_files: location of the data, relative to the XNAT experiment
    :param templates: name of the TaskManager template(s) used to create the data
    :param castor_study_name: The name of then study on castor
    :param castor_site_name: The name of the site on castor
    :param castor_visit_name: The name of the visit on castor
    :param extra_variable_map: Map of extra variable to be added to the fields based
                               on information from callback_execution_data
    :param translation_map: Map of translations for field names in the data to castor
    :param xnat_external_system: name of the external xnat [XNAT]
    :param castor_external_system_name: Castor external ID [CASTOR]
    :param taskmanager_external_system_name: Taskmanager external ID [TASKMANAGER]

    Example:

    .. code-block:: YAML

      function: create_task
      callback_arguments:
        field_files: "resources/FIELDS/files/data_location{timestamp}.json"
        templates: "data_template"
        castor_study_name: "Study Name"
        castor_site_name: "Site Name"
        extra_variable_map:
          ergo_id: "/subject/label"
          experiment_id: "/experiment/label"
          visit_date: "/experiment/scandate"
        translation_map:
          if_hippo_vol: "hippocampus volume"
        xnat_external_system: XNAT
        castor_external_system: CASTOR
        taskmanager_external_system_name: TASKMANAGER

    """

    # Get the correct servers to talk to
    xnat_server = callback_execution_data['external_systems'][xnat_external_system].rstrip('/')
    castor_server = callback_execution_data['external_systems'][castor_external_system_name].rstrip('/')
    task_manager_server = callback_execution_data['external_systems'][taskmanager_external_system_name].rstrip('/')

    # Get the correct XNAT ids to retrieve the data for
    experiment = callback_execution_data['experiment']
    subject = callback_execution_data['subject']

    xnat_experiment_id = experiment['external_ids'][xnat_external_system]
    xnat_subject_id = subject['external_ids'][xnat_external_system]

    # Get the data
    xnat_experiment_path = "data/archive/subjects/{subject}/experiments/{experiment}".format(
        project=config['STUDYGOV_XNAT_PROJECT'],
        subject=xnat_subject_id,
        experiment=xnat_experiment_id
    )

    # Download all data from XNAT
    if not isinstance(field_files, list):
        field_files = [field_files]

    print('=' * 80)
    data = []
    with xnat.connect(xnat_server) as session:
        for entry in field_files:
            xnat_fields_uri = '{}/{}/{}'.format(xnat_server, xnat_experiment_path, entry)
            json_data = download_latest_file_version(session=session, url=xnat_fields_uri)
            print(f"=== Loaded data for fields file {entry} ===")
            print(json_data)
            data.append(json_data)

    # Download all templates from task-manager
    if not isinstance(templates, list):
        templates = [templates]

    template_data = []
    with taskclient.connect(task_manager_server) as taskman:
        for task_template in templates:
            task_template_data = taskman.get_json(f'/task_templates/{task_template}')
            task_template_data = yaml.safe_load(task_template_data['content'])
            print(f"=== Loaded data for template {task_template} ===")
            print(task_template_data)
            template_data.append(task_template_data)

    # Collect all field data given the data and template
    fields = []
    for data_entry, template, template_name in zip(data, template_data, templates):
        field_data = collect_fields(template['qa_fields'], data_entry)
        print(f"=== Collected fields for template {template_name} ===")
        pprint(field_data)
        fields.append(field_data)

    print('=' * 80)

    # Insert data into castor
    netloc = urllib.parse.urlparse(castor_server).netloc
    try:
        auth_info = netrc.netrc().authenticators(netloc)
        castor_client_id, _, castor_client_secret = auth_info
    except IOError:
        raise ValueError(f'Could not get login information for {netloc} from netrc')

    with CastorConnection(castor_server) as castor_client:
        # Log in
        castor_client.login(castor_client_id, castor_client_secret)
        castor_client.change_reason = f"Imported via StudyGovernor callback {callback_execution_data['web_uri']}"
        print(f"Set change reason to: {castor_client.change_reason}")

        if translation_map:
            castor_client.field_translation = translation_map

        # Get RSS study id
        studies = castor_client.get_items('/study', item_key="study")
        study = next((x for x in studies if x['name'] == castor_study_name), None)

        if study is None:
            msg = f'CRITICAL: Cannot find study "{castor_study_name}" on Castor, aborting!'
            print(msg)
            raise KeyError(msg)

        study_id = study['study_id']

        # Get study site for this participant
        sites = castor_client.get_items(f'/study/{study_id}/site', 'sites')
        site = next((x for x in sites if x['name'] == castor_site_name), None)

        if site is None:
            msg = f'CRITICAL: Cannot find site "{castor_site_name}" on Castor, aborting!'
            print(msg)
            raise KeyError(msg)

        site_id = site["id"]

        # Get participant id and make sure participant exists on Castor
        participant_id = callback_execution_data['subject']['label']

        participant_data = {
            'participant_id': participant_id,
            'site_id': site_id,
        }
        response = castor_client.post(f'/study/{study_id}/participant', data=participant_data)
        participant_existed = False
        if response.status_code == 201:
            print(f'Participant{participant_id} created')
        elif response.status_code == 422:
            print(f'Participant{participant_id} already exists')
            participant_existed = True
        else:
            # Something unexpected happened, so abort and throw an error
            msg = f'Invalid response when creating subject: [{response.status_code}] {response.text}'
            print(msg)
            raise ValueError(msg)

        # Result variables to be logged
        data_inserted = {}
        error = None
        traceback_str = None

        for field_data, template in zip(fields, templates):
            # Add extra variables based on studygovernor information
            for key, value in extra_variable_map.items():
                field_data[key] = resolve_pointer(doc=callback_execution_data, pointer=value, default=None)

            # We use try/except to log the progress and return partial results, but still abort the callback and log
            # the error and traceback
            try:
                data_inserted[template] = castor_client.post_meta(study_id=study_id,
                                                                  participant_id=participant_id,
                                                                  data=field_data,
                                                                  visit_name=castor_visit_name)
            except BaseException as exception:
                error = str(exception)
                traceback_str = traceback.format_exc()
                print(error)
                break

    return {
        'study_name': castor_study_name,
        'study_id': study_id,
        'site_name': castor_site_name,
        'site_id': site_id,
        'participant_id': participant_id,
        'field_files': field_files,
        'templates': templates,
        'participant_existed': participant_existed,
        'data_inserted': data_inserted,
        "__traceback__": traceback_str,
        "__exception__": error,
        "__success__": not bool(error),
    }
