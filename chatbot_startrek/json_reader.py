import json
import os


def read_json(file):
    if os.path.isfile(file):
        with open(file) as json_file:
            return json.load(json_file)
    else:
        raise FileNotFoundError("File: {} does not exist".format(file))
