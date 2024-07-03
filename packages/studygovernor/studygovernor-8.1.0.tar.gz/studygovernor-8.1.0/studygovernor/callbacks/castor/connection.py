import requests
from typing import Any, Container, Dict, List, Optional, Tuple, Union
from urllib import parse

from .exceptions import ConflictingDataError, LoginError, ResponseError


TimeoutType = Optional[Union[float, Tuple[float, float]]]


class CastorConnection:
    reserved_field_names = {'participant_id', 'if_other_description'}

    def __init__(self, host, token=None):

        self.host = host
        self.token = token
        self.session = requests.Session()
        self.api_prefix = '/api'
        self.change_reason = 'Imported via StudyGovernor callback'

        # Store field translations for this session
        self.field_translation: Dict[str, str] = {}
         
        if self.token is not None:
            self.session.headers.update(self.auth_header)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.session.close()

    @property
    def auth_header(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else None

    def login(self, client_id, client_secret):
        response = self.session.post(
            f"{self.host}/oauth/token", 
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials",
                })

        # Check response
        data = response.json()
        if response.status_code != 200:
            # Some fields that might give us insight in the error
            reason = data.get("reason", "")
            error = data.get("error", "error")
            error_description = data.get("error_description", "")

            msg = f"Error during login: [{error}] {reason} {error_description}"
            raise LoginError(msg)

        self.token = data["access_token"]
        self.session.headers.update(self.auth_header)
        
    def get(self,
            endpoint: str,
            stream: bool = False,
            query: Optional[Dict[str, str]] = None,
            accepted_status: Optional[Container[int]] = None,
            timeout: TimeoutType = None,
            headers: Optional[Dict[str, str]] = None) -> requests.Response:
        accepted_status = accepted_status or [200]

        # Insert auth header
        headers = dict(headers) if headers else {}
        headers.update(self.auth_header)

        # Use querystring
        if query:
            query_string = '?' + parse.urlencode(query, safe='/', doseq=True)
        else:
            query_string = ''

        response = self.session.get(f"{self.host}{self.api_prefix}{endpoint}{query_string}",
                                    headers=headers,
                                    stream=stream,
                                    timeout=timeout)

        if response.status_code not in accepted_status:
            raise ResponseError(response=response,
                                message=f"Invalid response for GET on endpoint {endpoint}: "
                                        f"{response.status_code}, expected {accepted_status}")

        return response

    def get_json(self,
                 endpoint: str,
                 query: Optional[Dict[str, str]] = None,
                 accepted_status: Optional[Container[int]] = None,
                 timeout: TimeoutType = None,
                 headers: Optional[Dict[str, str]] = None):
        response = self.get(endpoint,
                            query=query,
                            accepted_status=accepted_status,
                            timeout=timeout,
                            headers=headers)
        return response.json()

    def get_items(self,
                  endpoint: str,
                  item_key: str,
                  page_size: str = 500):
        result_data = []
        first_page_data = self.get_json(endpoint=endpoint,
                                        query={'page_size': str(page_size)})

        total_items = first_page_data['total_items']
        result_data.extend(first_page_data['_embedded'][item_key])

        # In case a page is not paginated, we are done
        if len(result_data) == total_items:
            return result_data

        # First do some sanity checks in the result
        if first_page_data['page_size'] != page_size:
            raise ValueError(f'The data returned has incorrect page size: found'
                             f' {first_page_data["page_size"]} while expecting {page_size}')

        if first_page_data['page'] != 1:
            raise ValueError('The data returned is not for the first page')

        page_count = first_page_data['page_count']

        for page in range(2, page_count + 1):
            page_data = self.get_json(endpoint=endpoint,
                                      query={'page_size': str(page_size), 'page': str(page)})
            result_data.extend(page_data['_embedded'][item_key])

        if len(result_data) != total_items:
            raise ValueError(f'The total number of items after retrieval did not match the expected number:'
                             f'retrieved  {len(result_data)} items while expecting {total_items} items.')

        return result_data

    def post(self, endpoint, data):
        return self.session.post(f"{self.host}{self.api_prefix}{endpoint}", headers=self.auth_header, json=data)
    
    def put(self, endpoint):
        raise NotImplementedError("PUT method has not been implemented, use requests.put instead.")
    
    def delete(self, endpoint):
        raise NotImplementedError("PUT method has not been implemented, use requests.delete instead.")

    def prepare_post_entry(self, field_id, value):
        return {
            'field_id': field_id,
            'field_value': str(value),
            'change_reasons': self.change_reason,
            'confirmed_changes': True
        }

    def prepare_instance_field_entry(self, instance_id, field_id, value):
        return {
            'field_id': field_id,
            'field_value': str(value),
            'instance_id': instance_id,
            'change_reasons': self.change_reason,
            'confirmed_changes': True
        }

    def prepare_request_payload(self, post_data):
        return {
            'common': {
                'change_reason': self.change_reason,
                'confirmed_changes': True
            },
            'data': post_data
        }

    def get_repeating_form_id(self, study_id, form_name):
        repeating_data_forms = self.get_items(f'/study/{study_id}/repeating-data', item_key='repeatingData')
        for form in repeating_data_forms:
            if form['name'] == form_name:
                return form['id']

    def get_visit_id(self, study_id, visit_name):
        visits = self.get_items(f'/study/{study_id}/visit', item_key='visits')
        for visit in visits:
            if visit['visit_name'] == visit_name:
                return visit['id']
        raise ValueError(f'Visit {visit_name} not found on castor server')

    def map_fields(self, study_id):
        field_mapping = dict()
        field_info = dict()

        # TODO: This should probably be allowing more than 500 entries in the future?
        fields = self.get_items(f'/study/{study_id}/field', 'fields')

        # Field variable names are unique
        for field in fields:
            # Defined the field_key based on the Castor field information. If possible use the field_variable_name
            # but that is not set for repeated measurements. In that case we create a field_key based on field_label.
            # If the field_label is also empty, then we will skip this variable in the mapping.
            field_key = field['field_variable_name']
            if not field_key:
                field_key = field['field_label'].lower().replace(' ', '_')

            if not field_key:
                print(f"Skipping field: {field}")
                continue
            field_mapping[field_key] = field['id']

            field_info[field['id']] = field
        return field_mapping, field_info

    @staticmethod
    def to_string(value: Any) -> str:
        # Translate booleans
        if value is True:
            value = 'true'
        if value is False:
            value = 'false'

        # Cast value to string
        return str(value)

    def prepare_data(self,
                     study_id: str,
                     data: Dict[str, Any]) -> Dict[str, str]:
        fields_mapping, field_info = self.map_fields(study_id)

        prepared_data = {}
        for field, value in data.items():
            if field in self.reserved_field_names:
                continue

            if field in self.field_translation:
                field = self.field_translation[field]

            field_id = fields_mapping.get(field)

            if field_id is None:
                print(f'Field {field} not found')
                continue

            field_def = field_info[field_id]

            print(f'Processing {field} ({field_def["field_type"]}): {field_def["field_label"]}')

            if field_def['field_type'] == 'repeated_measures':
                print(f"Skipping repeated measure: {field_def['field_label']}")
                continue

            value = self.to_string(value)
            prepared_data[field] = value

        return prepared_data

    def prepare_post_data(self,
                          study_id: str,
                          data: Dict[str, Any],
                          instance_id: Optional[str] = None) -> List[Dict[str, str]]:
        fields_mapping, field_info = self.map_fields(study_id)

        post_data = list()
        data = self.prepare_data(study_id=study_id, data=data)

        for field, value in data.items():
            field_id = fields_mapping.get(field)

            # Dispatch to correct entry preparation
            if instance_id is None:
                post_entry = self.prepare_post_entry(field_id, value)
            else:
                post_entry = self.prepare_instance_field_entry(instance_id, field_id, value)

            post_data.append(post_entry)

        return post_data

    def get_repeating_data(self,
                           study_id: str,
                           data: Dict[str, List[Dict]]) -> List[Dict[str, Any]]:
        fields_mapping, field_info = self.map_fields(study_id)

        repeating_data = list()
        for field, value in data.items():
            if field in self.reserved_field_names:
                continue

            # Skip empty values
            if not value:
                continue

            if field in self.field_translation:
                field = self.field_translation[field]

            field_id = fields_mapping.get(field)

            if field_id is None:
                print(f'Field {field} not found')
                continue

            field_def = field_info[field_id]

            if field_def['field_type'] != 'repeated_measures':
                continue

            for nr, entry in enumerate(value):
                repeating_data.append({
                    'id': field_def['report_id'],
                    'label': f"{field}-{nr}",
                    'data': self.prepare_data(study_id=study_id, data=entry),
                })

        return repeating_data

    def _compare_post_data(self, post_data, existing_data, study_id=None):
        # If existing data is empty, things are fine
        if not existing_data:
            return True

        if study_id is not None:
            fields_mapping, field_info = self.map_fields(study_id)
        else:
            fields_mapping, field_info = {}, {}

        for field_id, field_value in post_data.items():
            if field_id in existing_data:
                if field_value != existing_data[field_id] and existing_data[field_id] != '':
                    print(f"ERROR: Field {field_id=} is {field_value} in new data, but {existing_data[field_id]} in existing data, "
                          f"field info: {field_info.get(field_id)}")
                    return False
            if field_id not in existing_data:
                if field_value != "":
                    print(f"ERROR: New field {field_id=} {field_value=} not present in existing data, field info: {field_info.get(field_id)}")
                    return False

        return True

    def _check_existing(self,
                        study_id: str,
                        participant_id: str,
                        post_data: [List[Dict]],
                        repeated_data: List) -> bool:
        # See if there is already data present, if so we need to check if the data is not conflicting
        try:
            old_data = self.get_items(f"/study/{study_id}/participant/{participant_id}/data-points/study",
                                      item_key='items')
        except ResponseError as exception:
            if exception.status_code == 404:
                print(f"Did not find {study_id=} {participant_id=}")
                return False
            else:
                raise exception

        print(f"Found {study_id=} {participant_id=}")

        # Reformat data for easier comparison
        post_data = {x['field_id']: x['field_value'] for x in post_data}
        old_data = {x['field_id']: x['field_value'] for x in old_data}

        # If there is no old data entered, this is also fine
        if not old_data:
            return False

        if not self._compare_post_data(post_data, old_data, study_id):
            raise ConflictingDataError(f"New data for subject {participant_id} conflicts with already present data.")

        self._check_existing_repeated_measurements(study_id=study_id,
                                                   participant_id=participant_id,
                                                   repeated_data=repeated_data)

        # We found existing data and it is compatible with the new data
        return True

    def _check_existing_repeated_measurements(self,
                                              study_id: str,
                                              participant_id: str,
                                              repeated_data: List):
        # Get existing repeated data measurements to see how to patch it
        try:
            data = self.get_items(f"/study/{study_id}/participant/{participant_id}/repeating-data-instance",
                                  item_key='repeatingDataInstance')
        except ResponseError as exception:
            if exception.status_code == 404 and len(repeated_data) == 0:
                return
            elif exception.status_code == 404:
                raise ConflictingDataError(f"Cannot find repeated measurements in existing data")
            else:
                raise exception

        data = {x['name']: x for x in data}

        for new_repeated_measurement in repeated_data:
            label = new_repeated_measurement['label']
            name = f'{participant_id}-{label}'

            old_repeated_measurement = data.get(name)
            if old_repeated_measurement is None:
                raise ConflictingDataError(f"New repeated measurement {name} not found in existing data")

            print(f'INFO: Repeated measure name {name} already in use!')

            old_fields = self.get_items(
                f"/study/{study_id}/participant/{participant_id}/data-point/repeating-data/{old_repeated_measurement['id']}",
                item_key='RepeatingDataDataPoints'
            )

            old_fields = {x['field_variable_name']: x['value'] for x in old_fields}

            if not self._compare_post_data(new_repeated_measurement['data'], old_fields):
                print(f"ERROR: Repeated measurement {name} differs!")
                raise ConflictingDataError(f"Repeated measurment {name} differs!")

        return

    def post_meta(self,
                  study_id: str,
                  participant_id: str,
                  data: Dict[str, Any],
                  visit_name: str) -> bool:

        # Format data is the correct format to post
        post_data = self.prepare_post_data(study_id, data)

        # Get repeated measurement data
        repeated_data = self.get_repeating_data(study_id, data)

        # Check if data to upload conlficts with existing data
        exists = self._check_existing(participant_id=participant_id,
                                      study_id=study_id,
                                      post_data=post_data,
                                      repeated_data=repeated_data)

        if exists:
            print(f"INFO Data is already present (and the same) in the system")
            return False

        request_payload = self.prepare_request_payload(post_data)

        response = self.post(f'/study/{study_id}/participant/{participant_id}/data-points/study', data=request_payload)
        if response.status_code != 201:
            message = f'ERROR Status code {response.status_code}: {response.json()}'
            print(message)
            raise ResponseError(response=response, message=message)

        visit_id = self.get_visit_id(study_id, visit_name)

        for repeated_entry in repeated_data:
            self.post_repeated_measurement(
                study_id=study_id,
                participant_id=participant_id,
                visit_id=visit_id,
                repeated_measure_id=repeated_entry['id'],
                repeated_measure_label=repeated_entry['label'],
                repeated_measure_data=repeated_entry['data'],
            )

        return True

    def post_repeated_measurement(self,
                                  study_id: str,
                                  participant_id,
                                  visit_id: str,
                                  repeated_measure_id: str,
                                  repeated_measure_label: str,
                                  repeated_measure_data: Dict):
        name = f'{participant_id}-{repeated_measure_label}'
        create_repeating_instance_data = {
            'repeating_data_id': repeated_measure_id,
            'repeating_data_name_custom': name,
            'parent_id': visit_id,
        }

        # Post the measurement
        response = self.post(f'/study/{study_id}/participant/{participant_id}/repeating-data-instance',
                             data=create_repeating_instance_data)
        print(f"Repeating data post: {create_repeating_instance_data}")

        if response.status_code == 201:
            instance_id: str = response.json()['id']
            post_data = self.prepare_post_data(study_id, repeated_measure_data, instance_id)
            request_payload = self.prepare_request_payload(post_data)
            print(f"Repeating data fields post: {create_repeating_instance_data}")

            post_rdi_response = self.post(
                f'/study/{study_id}/participant/{participant_id}/data-points/repeating-data-instance/{instance_id}',
                data=request_payload
            )
            if post_rdi_response.status_code != 201:
                print(f'ERROR Code {post_rdi_response.status_code}: {post_rdi_response.json()}')
        else:
            print(f'ERROR Code {response.status_code}: {response.json()}')
