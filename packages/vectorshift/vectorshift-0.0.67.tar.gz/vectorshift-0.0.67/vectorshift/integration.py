import json

import requests
import vectorshift
from vectorshift.consts import *


class Integration:
    def __init__(self, id: str, name: str, description: str, type: str):
        self.id = id
        self.name = name
        self.description = description
        self.type = type

    def to_json_rep(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_json_rep(), indent=4)

    @staticmethod
    def from_json_rep(json_data: dict[str, any]) -> 'Integration':
        return Integration(
            name=json_data.get('name'),
            description=json_data.get('description'),
            type=json_data.get('type'),
            id=json_data.get('id'),
        )

    @staticmethod
    def from_json(json_str: str) -> 'Integration':
        json_data = json.loads(json_str)
        return Integration.from_json_rep(json_data)

    def __repr__(self) -> str:
        return str(self.to_json_rep())

    @staticmethod
    def fetch_all(
        api_key=None,
        public_key=None,
        private_key=None,
    ) -> list['Integration']:
        """Fetch all integrations from the VectorShift platform.

        Parameters:
            api_key (str) : The API key to use.
            public_key (str): The public API key to use, if applicable.
            private_key (str): The private API key to use, if applicable.

        Returns:
            list[Integration]: A list of all user integrations.
        """
        response = requests.get(
            API_INTEGRATION_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()

        integrations = [
            Integration.from_json_rep(integration) for integration in response
        ]
        return integrations

    @staticmethod
    def fetch(
        integration_id: str, api_key=None, public_key=None, private_key=None
    ) -> 'Integration':
        """
        Loads an existing integration from the VectorShift platform.

        Creating, deleting, and modifying integrations must be done via the VectorShift website.

        Parameters:
            integration_id (str): The ID of the integration to load.
            api_key (str): The API key to use.
            public_key (str): The public API key to use, if applicable.
            private_key (str): The private API key to use, if applicable.

        Returns:
            Integration: The loaded integration.
        """
        if not integration_id:
            return None
        response = requests.get(
            API_INTEGRATION_FETCH_ENDPOINT,
            params={'integration_id': integration_id},
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return Integration.from_json_rep(response)

    def sync_metadata(
        self,
        api_key=None,
        public_key=None,
        private_key=None,
    ) -> list:
        """Sync the metadata of an existing Integration from the VectorShift platform. This should be called on an Integration object that refers to an Integration on the platform (e.g. has been fetched).

        Parameters:
            api_key (str): The API key to use.
            public_key (str): The public API key to use, if applicable.
            private_key (str): The private API key to use, if applicable.

        Returns:
            list: The server response from the VectorShift platform.
        """
        if self.id is None:
            raise ValueError('Missing integration id.')
        response = requests.post(
            API_INTEGRATION_SYNC_METADATA_ENDPOINT,
            data={
                'integration_id': self.id,
            },
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            },
        )

        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()
        return response

    def sync_integration(
        self,
        api_key=None,
        public_key=None,
        private_key=None,
    ):
        """Sync an existing Integration from the VectorShift platform. This should be called on an Integration object that refers to an Integration on the platform (e.g. has been fetched).

        Parameters:
            api_key (str): The API key to use.
            public_key (str): The public API key to use, if applicable.
            private_key (str): The private API key to use, if applicable.

        Returns:
            dict: The server response from the VectorShift platform.
        """
        if self.id is None:
            raise ValueError('Missing integration id.')
        response = requests.post(
            API_INTEGRATION_SYNC_ENDPOINT,
            data={
                'integration_id': self.id,
            },
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            },
        )

        if response.status_code != 200:
            raise Exception(response.text)
        return

    def get_item_ids(
        self,
        api_key=None,
        public_key=None,
        private_key=None,
    ) -> list:
        """
        Returns a visualization of the file tree of an Integration which can be used for mapping metadata.
        """
        if self.id is None:
            raise ValueError('Missing integration id.')

        response = requests.get(
            API_INTEGRATION_GET_ITEM_IDS_ENDPOINT,
            params={'integration_id': self.id},
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            },
        )

        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()
