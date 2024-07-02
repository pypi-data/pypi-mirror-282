"""TODO: document this."""
import ast
import json
import requests
import datasets
import io
import os
import soundfile as sf
import urllib


def _nijta_serializer(obj):
    """Serialize audio dataset.

    Serialize audio data from a datasets.DatasetDict or datasets.arrow_dataset.Dataset
    into a dictionary of hex-encoded audio data.

    Args:
        obj (datasets.dataset_dict.DatasetDict or datasets.arrow_dataset.Dataset):
            Input audio dataset.

    Returns:
        dict: A dictionary containing hex-encoded audio data.
    """
    if isinstance(obj, datasets.dataset_dict.DatasetDict):
        serialized = {}
        for subset in obj:
            for f in obj[subset]:
                buffer = io.BytesIO()
                sf.write(buffer,
                         f["audio"]["array"].transpose(),
                         f["audio"]["sampling_rate"],
                         format="wav")
                name = f["audio"]["path"]
                serialized[name] = buffer.getvalue().hex()
        return serialized
    if isinstance(obj, datasets.arrow_dataset.Dataset):
        serialized = {}
        for f in obj:
            buffer = io.BytesIO()
            sf.write(buffer,
                     f["audio"]["array"].transpose(),
                     f["audio"]["sampling_rate"],
                     format="wav")
            name = f["audio"]["path"]
            serialized[name] = buffer.getvalue().hex()
        return serialized


def session(token, api_url='https://api.nijta.com/'):
    """
    Start a session.

    Args:
        token (str): your token to access the api
        api_url (str): the url of the api

    Returns:
        the session id if authorized, status otherwise
    """
    headers = {"Content-Type": "application/json; charset=utf-8",
               "TOKEN": token}
    response = json.loads(requests.post(api_url + '/session', headers=headers).content)
    if "status" in response:
        return response['status']
    return response['session_id']


def send_request(input_data, params, session_id, headers,
                 task='anonymize', api_url='https://api.nijta.com/', storage_options=None):
    """
    Send an HTTP POST request containing audio dataset information to a specified API endpoint.

    Args:
        input_data (str or list): Path to a local folder, URL, or list of audio file paths.
        params (dict): Parameters to include in the request.

    Returns:
        requests.Response or str: The API response or an error message.
    """
    if task == "text":
        url = f"{api_url}/tasks/text/{session_id}"
        try:
            response = requests.post(url,
                                     json={'text': input_data, **params},
                                     headers=headers)
            return response
        except requests.exceptions.RequestException as e:
            return f"Error sending request: {e}"
    else:
        audio_dataset = _create_dataset(input_data, storage_options)

        if audio_dataset:
            dataset = audio_dataset.cast_column("audio",
                                                datasets.Audio(decode=True, mono=False))['train']
            try:
                if task == 'ASR':
                    url = f"{api_url}/tasks/asr/{session_id}"
                else:
                    url = f"{api_url}/tasks/{session_id}"

                response = requests.post(url,
                                        json=json.dumps(
                                            dataset,
                                            default=_nijta_serializer),
                                        headers=headers,
                                        params=urllib.parse.urlencode(params))
                return response
            except requests.exceptions.RequestException as e:
                return f"Error sending request: {e}"
        else:
            return "Invalid input_data format."


def _create_dataset(input_data, storage_options=None) -> datasets.Dataset:
    audio_dataset = None
    if isinstance(input_data, str):
        # Check if the input_data is a folder path or URL
        if input_data.startswith('http://') or input_data.startswith('https://'):
            audio_dataset = datasets.load_dataset('audiofolder', data_files=input_data)
        elif input_data.startswith('s3://'):
            if storage_options:
                fs = datasets.filesystems.S3FileSystem(**storage_options)
            else:
                # if credentials are not in storage_options, they're expected to be
                # found in ~/.aws/credentials
                fs = datasets.filesystems.S3FileSystem()

            if not fs.exists(input_data):
                raise FileNotFoundError()

            if fs.isfile(input_data):
                audio_dataset = datasets.load_dataset('audiofolder',
                                                      data_files=[input_data],
                                                      storage_options=storage_options
                                                      )
            else:
                input_data = [f's3://{f}' for f in fs.glob(f"{input_data[len('s3://'):]}/**/*")
                              if fs.isfile(f's3://{f}')]
                audio_dataset = datasets.load_dataset('audiofolder',
                                                      data_files=input_data,
                                                      storage_options=storage_options
                                                      )
        elif os.path.isfile(input_data):
            audio_dataset = datasets.load_dataset('audiofolder', data_files=[input_data])
        else:
            audio_dataset = datasets.load_dataset('audiofolder', data_dir=input_data)
    elif isinstance(input_data, list):
        audio_dataset = datasets.load_dataset('audiofolder', data_files=input_data,
                                              storage_options=storage_options)
        input_data = ''
    return audio_dataset


def read_response(task_id, api_url='https://api.nijta.com/'):
    """
    Parse the HTTP POST response containing anonymized audio dataset.

    Args:
        task_id (int): Id of the task.

    Returns:
        The anonymized batch in a dict with original file names as keys if input data are audio files.
        {'filename': {
            'audio': b'audio data',
            'transcription': 'transcription'
        }}
        Or a list of masked text if input data are texts
        ['Masked text 1', 'Masked text 2']
    """
    response = requests.get(f'{api_url}/tasks/{task_id}')
    try:
        content = json.loads(response.content)
    except Exception:
        print(response)
        raise
    if content['data']['task_status'] != 'finished':
        return content['data']['task_status'], None

    anon_batch_in_bytes = bytes.fromhex(content['data']['task_result']['response'])
    anon_batch = anon_batch_in_bytes.decode().replace('true', 'True').replace('false', 'False')
    anon_batch = json.loads(anon_batch)
    if 'data' in anon_batch:
        anon_batch = anon_batch['data']

    result = {}
    if isinstance(anon_batch, dict):
        # audio input (anonymize or ASR)
        for filename in anon_batch:
            result[filename] = anon_batch[filename]
            if 'audio' in anon_batch[filename]:
                result[filename]['audio'] = bytes.fromhex(anon_batch[filename]['audio'])
    else:
        # text input
        result = anon_batch

    return content['data']['task_status'], result
