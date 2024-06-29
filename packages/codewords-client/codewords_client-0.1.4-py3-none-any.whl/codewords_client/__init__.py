import asyncio
import datetime
import json
import os

import requests
import websockets
from codewords_core.file_type_utils import (
    download_files_and_update_variables,
    upload_files_and_update_variables,
)

# add ../ to sys.path
from codewords_core.io_metadata import InputOutputMetadata

WS_URL = os.getenv('CWR_WS_URL', "wss://d21x5wziv7.execute-api.eu-west-2.amazonaws.com/prod/")
HTTPS_URL = os.getenv('CWR_HTTPS_URL', "https://na9ywpljw9.execute-api.eu-west-2.amazonaws.com/prod/runtime")


def cw_function(
    *,
    function_id: str,
    version: str,
    auth_data: dict | None = None,
    runner_id: str,
    sync: bool = True,
    **init_kwargs
) -> 'CWFunction':
    if auth_data is None:
        # get CODEWORDS_API_KEY from the environment
        auth_data = {
            "type": "api_key",
            "data": os.getenv("CODEWORDS_API_KEY")
        }
        if auth_data['data'] is None:
            raise ValueError("auth_data or CODEWORDS_API_KEY must be provided")

    resp = requests.post(
        HTTPS_URL,
        json={
            "action": "get_info",
            "function_id": function_id,
            "version": version,
            "auth_data": auth_data,
            "runner_id": runner_id,
        },
    )
    resp.raise_for_status()
    definition_dict = resp.json()

    inputs_metadata = [InputOutputMetadata.parse_obj(input_data) for input_data in definition_dict['inputs']]
    outputs_metadata = [InputOutputMetadata.parse_obj(output_data) for output_data in definition_dict['outputs']]
    function_class = SyncCodewordsFunction if sync else AsyncCodewordsFunction

    return function_class(
        definition_dict,
        inputs_metadata,
        outputs_metadata,
        auth_data=auth_data,
        runner_id=runner_id,
        **init_kwargs
    )


class CWFunction():
    def __init__(
        self,
        definition_dict,
        inputs_metadata,
        outputs_metadata,
        *,
        working_directory='.',
        auth_data: dict,
        runner_id: str,
        verbose=False,
    ):
        self.definition_dict = definition_dict
        self.inputs_metadata = inputs_metadata
        self.outputs_metadata = outputs_metadata
        self.working_directory = working_directory
        self.auth_data = auth_data
        self.runner_id = runner_id
        self._print = print if verbose else lambda *args, **kwargs: None

    async def run(self, inputs: dict) -> tuple[dict, dict]:
        # find all the file type fields and upload them
        inputs = await upload_files_and_update_variables(
            variables=inputs,
            variables_metadata=self.inputs_metadata,
            working_directory=self.working_directory,
        )

        # call the lambda at WS_URL with an event
        event = {
            'action': 'run',
            'function_id': self.definition_dict['function_id'],
            'version': self.definition_dict['version'],
            'inputs': inputs,
            'runner_id': self.runner_id,
            'auth_data': self.auth_data,
        }
        # stop 10 minutes from now if no end time is specified
        time_to_end = datetime.datetime.now() + datetime.timedelta(minutes=10)
        message_parts = {}
        return_value = None

        async with websockets.connect(WS_URL) as ws:
            self._print(f"sending event to runtime: {event}")
            await ws.send(json.dumps(event))

            while datetime.datetime.now() < time_to_end and return_value is None:
                recv_timeout = (time_to_end - datetime.datetime.now()).total_seconds()
                try:
                    response = await asyncio.wait_for(ws.recv(), timeout=recv_timeout)
                except asyncio.TimeoutError:
                    raise TimeoutError(f"Receiving message timed out after {recv_timeout} seconds")

                response = json.loads(response)
                self._print(f"📬 received message: {response}")

                # Process message chunks
                if 'chunk' in response:
                    sequence_id = response['sequence_id']
                    chunk = response['chunk']
                    index = response['index']
                    total_chunks = response['total_chunks']

                    if sequence_id not in message_parts:
                        message_parts[sequence_id] = [None] * total_chunks

                    message_parts[sequence_id][index] = chunk

                    # Check if all parts are received
                    if all(part is not None for part in message_parts[sequence_id]):
                        complete_message = ''.join(message_parts[sequence_id])
                        message_parts.pop(sequence_id)
                        response = json.loads(complete_message)
                        return_value = await self._process_message(response, ws)

                # Non-chunked message
                else:
                    return_value = await self._process_message(response, ws)

        outputs = response['outputs']
        # download any files that were uploaded
        outputs = await download_files_and_update_variables(
            variables=outputs,
            variables_metadata=self.outputs_metadata,
            working_directory=self.working_directory,
        )

        return outputs, response['run_info']

    async def _process_message(self, response, ws):
        if response['type'] in (
            'run_start',
            'block_start',
            'block_update',
            'block_complete',
        ):
            self._print(f"📬 received message: {response}")
            pass

        if response['type'] == 'block_error':
            # there's an error in the user code, we should still get a run_complete
            # message afterwards so for now continue
            return

        elif response['type'] == 'run_complete':
            return response

        elif response['type'] == 'function_missing':
            raise ValueError(
                f'Could not find function with id {self.definition_dict["function_id"]} '
                f'and version {self.definition_dict["version"]}'
            )

        elif response['type'] == 'run_error':  # an error occurred in the runtime
            raise ValueError(f"An error occurred when using the Codewords Runtime: {response}")

    async def call_async(self, **inputs):
        outputs, run_info = await self.run(inputs)
        # if there's an error throw that
        if len(run_info['error_messages']) > 0:
            raise Exception(f"Run failed with error messages: {run_info['error_messages']}")

        return outputs

    def call_sync(self, **inputs):
        return asyncio.run(self.call_async(**inputs))


class SyncCodewordsFunction(CWFunction):
    def __call__(self, **inputs):
        return self.call_sync(**inputs)


class AsyncCodewordsFunction(CWFunction):
    async def __call__(self, **inputs):
        return self.call_async(**inputs)
