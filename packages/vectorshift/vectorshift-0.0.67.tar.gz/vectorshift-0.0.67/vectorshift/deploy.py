# functionality to deploy and run pipelines
import inspect
import json
import mimetypes
import requests
from types import GenericAlias

import vectorshift
from vectorshift.integration import *
from vectorshift.pipeline import Pipeline
from vectorshift.consts import *


class Config:
    # For now, the config is just a wrapper for the API key
    def __init__(self, api_key=None, public_key=None, private_key=None):
        """Create a Config object, which can be used to perform various tasks related to interacting with the VectorShift platform. Given an API key in the constructor, various other class methods can be used to interact with the API using the key.

        Parameters:
            api_key (str): The API key to use for authentication.
            public_key (str): The public key to use for authentication if applicable.
            private_key (str): The private key to use for authentication if applicable.

        Returns:
            Config: The Config object.
        """
        self.api_key = api_key or vectorshift.api_key
        self.public_key = public_key or vectorshift.public_key
        self.private_key = private_key or vectorshift.private_key

    def fetch_user_details(self) -> dict:
        """Fetch user details, including the user ID, organization ID, and username, from the VectorShift platform. The details will be for the user with which the API key passed into the Config object is associated.

        Returns:
            dict: A JSON representation of the fetched user details.
        """
        response = requests.get(
            API_USER_DETAILS_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_all_pipelines(self) -> dict:
        """Fetch all the user's accessible pipelines from the VectorShift platform.

        Returns:
            dict: A JSON representation of the fetched pipelines.
        """
        response = requests.get(
            API_PIPELINE_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_all_pipeline_ids(self) -> list[str]:
        """Fetch all the user's accessible pipeline IDs from the VectorShift platform.

        Returns:
            list[str]: The fetched pipeline IDs.
        """
        ps = self.fetch_all_pipelines()
        ids = [p.get('id') for p in ps]
        return [id for id in ids if id is not None]

    # Save the pipeline as a new pipeline to the VS platform.
    def save_new_pipeline(self, pipeline: Pipeline) -> dict:
        # already implemented in the Pipeline class
        # save method will itself raise an exception if 200 isn't returned
        """Save a new pipeline to the VectorShift platform. This is equivalent to using the Pipeline.save method.

        Parameters:
            pipeline (Pipeline): The pipeline to save.

        Returns:
            dict: The JSON response from the VectorShift platform, including the representation of the saved pipeline.
        """
        response = pipeline.save(
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=False,
        )
        return response.json()

    def fetch_shared_pipelines(self) -> dict:
        """Fetch all the user's shared pipelines from the VectorShift platform.

        Returns:
            dict: The JSON representations of the fetched shared pipelines.
        """
        response = requests.get(
            API_PIPELINE_SHARED_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    # Update the pipeline, assuming it already exists in the VS platform.
    # Raises if the pipeline ID doesn't exist, or isn't in the VS platform.
    def update_pipeline(self, pipeline: Pipeline) -> dict:
        response = pipeline.save(
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=True,
        )
        """Update an existing pipeline in the VectorShift platform. This is equivalent to using the Pipeline.save method with update_existing set to True.

        Parameters:
            pipeline (Pipeline): The pipeline to update.

        Returns:
            dict: The JSON response from the VectorShift platform.
        """
        response = pipeline.save(
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=True,
        )

        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def delete_pipelines(self, pipeline_ids: list[str]) -> dict:
        """Delete pipelines from the VectorShift platform according to their pipeline IDs.

        Parameters:
            pipeline_ids (list[str]): The pipeline IDs to delete.

        Returns:
            dict: The JSON response from the VectorShift platform.
        """
        if pipeline_ids == []:
            return
        response = requests.delete(
            API_PIPELINE_DELETE_ENDPOINT,
            data={'pipeline_ids': pipeline_ids},
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_all_files(self) -> list[dict]:
        """Fetch all user files from the VectorShift platform.

        Returns:
            list[dict]: The JSON representations of the fetched files.
        """
        response = requests.get(
            API_FILE_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_files_by_ids(self, file_ids: list[str]) -> list[dict]:
        """Fetch user files from the VectorShift platform based on their file IDs.

        Parameters:
            file_ids: The file IDs to fetch.

        Returns:
            list[dict]: The JSON representations of the fetched files.
        """
        response = requests.get(
            API_FILE_FETCH_BY_ID_ENDPOINT,
            params={'file_ids': file_ids},
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_files_by_names(self, file_names: list[str]) -> list[dict]:
        """Fetch user files from the VectorShift platform based on their file names.

        Parameters:
            file_names: The file names to fetch.

        Returns:
            list[dict]: The JSON representations of the fetched files.
        """
        response = requests.get(
            API_FILE_FETCH_ENDPOINT,
            params={'file_names': file_names},
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def upload_file(
        self, file: str, folder_id: str = None, filetype: str = None
    ) -> dict:
        """Upload a file to the VectorShift platform.

        Parameters:
            file (str): The path to the file to upload. The value of the path will be the name of the file on the VectorShift platform.
            folder_id (str): The ID of the folder to upload the file to. Defaults to None.
            filetype (str): The file type of the file. Defaults to None.

        Returns:
            dict: The JSON response from the VectorShift platform, including the representation of the uploaded file.
        """
        try:
            headers = {
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            }
            # infer the file type
            if filetype is None:
                filetype = mimetypes.guess_type(file)[0]
            if filetype is None:
                raise ValueError(
                    f'Could not determine file type of {file}. Please ensure the file name has an appropriate suffix.'
                )

            with open(file, 'rb') as f:
                files = {'file': (file, f, filetype)}
                response = requests.post(
                    API_FILE_UPLOAD_ENDPOINT,
                    data={'folderId': folder_id},
                    headers=headers,
                    files=files,
                )
        except Exception as e:
            raise ValueError(f'Problem uploading file: {e}')
        response_json = response.json()
        uploaded_filename = next(iter(response_json.get('uploaded_files', [])), {}).get(
            'name'
        )
        if uploaded_filename:
            print(f'Successfully uploaded file as {uploaded_filename}.')
        return response_json

    def delete_files_by_id(self, file_ids: list[str]) -> dict:
        """Delete user files from the VectorShift platform based on their file IDs.

        Parameters:
            file_ids: The file IDs to delete.

        Returns:
            dict: The JSON response from the VectorShift platform.
        """
        headers = {
            'Api-Key': self.api_key,
            'Public-Key': self.public_key,
            'Private-Key': self.private_key,
        }
        response = requests.delete(
            API_FILE_DELETE_ENDPOINT,
            data={'file_ids': file_ids},
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        print('Successfully deleted file(s).')
        return response.json()

    def delete_files_by_name(self, file_names: list[str]) -> dict:
        """Delete user files from the VectorShift platform based on their file names.

        Parameters:
            file_names: The file names to delete.

        Returns:
            dict: The JSON response from the VectorShift platform.
        """
        headers = {
            'Api-Key': self.api_key,
            'Public-Key': self.public_key,
            'Private-Key': self.private_key,
        }
        response = requests.delete(
            API_FILE_DELETE_BY_NAMES_ENDPOINT,
            data={'file_names': file_names},
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        print('Successfully deleted file(s).')
        return response.json()

    def fetch_all_knowledge_bases(self) -> list[dict]:
        """Fetch all of a user's Knowledge Bases from the VectorShift platform.

        Returns:
            list[dict]: The JSON representations of the fetched Knowledge Bases.
        """
        response = requests.get(
            API_VECTORSTORE_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    fetch_all_vectorstores = fetch_all_knowledge_bases

    # TODO add methods to delete vectorstores & share objs

    def fetch_all_integrations(self) -> list[dict]:
        """Fetch all of a user's Integrations from the VectorShift platform.

        Returns:
            list[dict]: The JSON representations of the fetched Integrations.
        """
        return Integration.fetch_all(
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
        )

    def fetch_integration(self, integration_id: str) -> dict:
        """Fetch an Integration by its ID from the VectorShift platform.

        Parameters:
            integration_id: The ID of the Integration to fetch.

        Returns:
            dict: The JSON representation of the fetched Integration."""
        return Integration.fetch(
            integration_id,
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
        )

    def fetch_all_transformations(self) -> list[dict]:
        """Fetch all of a user's Transformations from the VectorShift platform.

        Returns:
            list[dict]: The JSON representations of the fetched Transformations.
        """
        response = requests.get(
            API_TRANSFORMATION_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_transformation(
        self, transformation_id: str = None, transformation_name: str = None
    ):
        """Fetch a Transformtion from the VectorShift platform. Specify either the ID or the name.

        Parameters:
            transformation_id: The ID of the Transformation to fetch.
            transformation_name: The name of the Transformation to fetch.

        Returns:
            dict: The JSON representation of the fetched Transformation."""
        if transformation_id is None and transformation_name is None:
            raise ValueError(
                'At least one of the transformation ID or name must be specified.'
            )
        params = {}
        if transformation_id is not None:
            params['transformation_id'] = transformation_id
        if transformation_name is not None:
            params['transformation_name'] = transformation_name
        response = requests.get(
            API_TRANSFORMATION_FETCH_ENDPOINT,
            params=params,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def save_transformation(
        self,
        transformation_func,
        outputs: dict[str, str],
        name: str = '',
        description: str = '',
        inputs: dict[str, str] = {},
        update_id: str = None,
    ) -> dict:
        """Save a Transformation to the VectorShift platform from a Python function. The inputs and outputs provided should be dicts of input/output names to the expected types. The function parameters must have names corresponding to the keys of inputs. The function must return a dict of outputs whose keys should match the keys in the outputs dict provided. The function must be a callable object. If the function declaration is annotated, the input types may be inferred and do not need to be provided.

        Supported types are 'Any', 'Text', 'Bool', 'Integer', 'Float', 'List', and 'Dict',

        Parameters:
            transformation_func: The function to save as a transformation.
            outputs: A dict of output names to output types of the function.
            name: The name of the transformation.
            description: The description of the transformation.
            inputs: A dict of input names to input types of the function.
            update_id: The ID of the transformation to update.

        Returns:
            dict: The JSON representation of the saved transformation.

        Example:
        vs = Config(...)

        def foo(aaa: str, bbb: list[str]):
            return {
                'prepended': [aaa] + bbb,
                'joined': aaa.join(bbb)
            }

        vs.save_transformation(
            transformation_func=foo,
            name='my_transformation',
            description='my description',
            inputs={
                'aaa': 'Text',
                'bbb': 'List'
            },
            outputs={
                'prepended': 'List',
                'joined': 'Text'
            },
        )

        NB: inputs did not need to be explicitly provided, as the types could have been inferred from the function signature type annotations.
        """

        def get_transformation_type_from_anno_type(t):
            if type(t) == type:
                return TRANSFORMATION_TYPE_NAMES.get(t.__name__, 'Any')
            elif isinstance(t, GenericAlias):
                return TRANSFORMATION_TYPE_NAMES.get(t.__origin__.__name__, 'Any')
            return 'Any'

        # validate inputs
        if not callable(transformation_func):
            raise ValueError('Cannot save a non-function object as a transformation')
        f_code = transformation_func.__code__
        n_args = f_code.co_argcount
        if inputs != {} and len(inputs.keys()) != n_args:
            raise ValueError(
                f'Incorrect number of inputs given for function (expected {n_args})'
            )
        f_argnames = f_code.co_varnames[:n_args]
        if inputs != {} and sorted(inputs.keys()) != sorted(f_argnames):
            raise ValueError(
                f'Incorrect input names given for function (expected {f_argnames})'
            )
        supported_transformation_types = TRANSFORMATION_TYPE_NAMES.values()
        for t in inputs.values():
            if t not in supported_transformation_types:
                raise ValueError(f'Invalid transformation input type {t}')
        for t in outputs.values():
            if t not in supported_transformation_types:
                raise ValueError(f'Invalid transformation output type {t}')
        # infer types from annotations if applicable
        _f_members = inspect.getmembers(transformation_func)
        f_members = {m[0]: m[1] for m in _f_members}
        f_type_annos = f_members.get('__annotations__', {})
        for argname in f_argnames:
            if argname in f_type_annos:
                arg_t = get_transformation_type_from_anno_type(f_type_annos[argname])
                if argname in inputs:
                    input_t = inputs[argname]
                    if input_t != 'Any' and input_t != arg_t:
                        raise ValueError(
                            f'Provided transformation type {input_t}is incompatible with inferred type {arg_t} from type annotations'
                        )
                else:
                    inputs[argname] = arg_t
            else:
                if argname not in inputs:
                    inputs[argname] = 'Any'
        if name == '':
            name = transformation_func.__name__
        # TODO is there some way to check outputs?
        transformation_rep = {
            'id': update_id,
            'name': name,
            'description': description,
            'functionName': transformation_func.__name__,
            'inputs': inputs,
            'outputs': outputs,
            'function': inspect.getsource(transformation_func),
        }
        print(transformation_rep)
        transformation_json = json.dumps(transformation_rep, indent=4)
        response = requests.post(
            API_TRANSFORMATION_SAVE_ENDPOINT,
            data={'transformation': transformation_json},
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(f'Server error creating transformation: {response.text}')
        return response.json()

    def delete_transformations(self, transformation_ids: list[str]):
        """Delete Transformations from the VectorShift platform by their IDs.

        Parameters:
            transformation_ids (list[str]): The IDs of the Transformations to delete.

        Returns:
            dict: The JSON response from the VectorShift platform.
        """
        headers = {
            'Api-Key': self.api_key,
            'Public-Key': self.public_key,
            'Private-Key': self.private_key,
        }
        response = requests.delete(
            API_TRANSFORMATION_DELETE_ENDPOINT,
            data={'transformation_ids': transformation_ids},
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        print('Successfully deleted transformation(s).')
        return response.json()


VectorShift = Config
