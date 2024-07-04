import base64
import json
import os
import requests
import pandas as pd


# Encode files to base64
def get_base64_encoded_files(folder_path):
    encoded_files = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                encoded_content = base64.b64encode(file.read()).decode("utf-8")
                encoded_files[filename] = encoded_content
    return encoded_files


def print_structure(d, indent=0):
    for key, value in d.items():
        print(" " * indent + str(key))
        if isinstance(value, dict):
            print_structure(value, indent + 4)


def get_all_files_in_folder(folder_path):
    files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files

def encoded(filepath):
    with open(filepath, "rb") as file:
        encoded_content = base64.b64encode(file.read()).decode("utf-8")
    return f"data:application/pdf;base64,{encoded_content}"


def file(filepath):
    return {
        "file_url": encoded(filepath),
                "options": {
                    "parserType": "tela-pdf-parser"
                }
        }


class TelaClient:
    def __init__(self, api_key, api_url="https://api.tela.com"):
        self.api_key = api_key
        self.api_url = api_url

    def request(self, documents, canvas_id):
        try:
            url = f"{self.api_url}/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            }
            data = {
                "uses": canvas_id,
                "with": documents,
                "input": "",
                "long_response": True,
            }
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code != 200:
                print(response.json())
                print(response.status_code)
            return response.json()
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def newCanvas(self, canvas_id, expected_input=None):
        return Canvas(self, canvas_id, expected_input)


class Canvas:
    def __init__(self, tela_client, canvas_id, expected_input=None):
        self.canvas_id = canvas_id
        self.tela_client = tela_client
        self.expected_input = expected_input

    def run(self, output_type='json', **kwargs):
        documents = {}
        if self.expected_input:
            for i in self.expected_input:
                if i in kwargs:
                    documents[i] = kwargs[i]
                else:
                    raise ValueError(f"Missing expected input: {i}")
        else:
            documents = kwargs
        response = self.tela_client.request(documents, self.canvas_id)
        if "choices" in response and len(response["choices"]) > 0:
            content = response["choices"][0]["message"]["content"]
            if output_type == 'dataframe':
                return self._json_to_dataframe(content)
            return content
        return None

    def _json_to_dataframe(self, json_data):
        def flatten_json(y):
            out = {}

            def flatten(x, name=''):
                if type(x) is dict:
                    for a in x:
                        flatten(x[a], name + a + '.')
                elif type(x) is list:
                    i = 0
                    for a in x:
                        flatten(a, name + str(i) + '.')
                        i += 1
                else:
                    out[name[:-1]] = x

            flatten(y)
            return out

        if isinstance(json_data, list):
            flat_data = [flatten_json(item) for item in json_data]
        else:
            flat_data = [flatten_json(json_data)]

        return pd.DataFrame(flat_data)


# EXAMPLE USAGE
# from tela.tela import TelaClient, file

# TELA_API_KEY = "Your API KEY"
# tela_client = TelaClient(TELA_API_KEY)

# canvas_id = "2b57f4ae-c48e-4883-a0a4-130a573ffdfc"
# canvas = tela_client.newCanvas(canvas_id, expected_input=['document'])

# FILE_NAME = "./Cartao CNPJ produtor.pdf"
# canvas.run(document=file(FILE_NAME))