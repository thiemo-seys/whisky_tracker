import json


def save_json_to_file(json_path, elements, indent=4, mode='w'):
    with open(json_path, mode) as file:
        json.dump(elements, file, indent=indent)


def load_json_file(json_path):
    with open(json_path) as file:
        return json.load(file)
