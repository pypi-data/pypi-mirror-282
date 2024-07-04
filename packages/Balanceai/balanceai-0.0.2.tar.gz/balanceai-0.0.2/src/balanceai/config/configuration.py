import json
import logging


def load_json(data):
    return json.loads(data)


def read_json(file):
    try:
        with open(file, 'r') as myfile:
            data = myfile.read()

        return load_json(data)

    except FileNotFoundError as e:
        logging.error('Error reading json:', e)
        return None
