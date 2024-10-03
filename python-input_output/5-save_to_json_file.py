#!/usr/bin/python3
"""
from file to json
"""
import json as js


def save_to_json_file(my_obj, filename):
    """
    duump with write
    """
    with open("my_dict.json", 'w', encoding= 'utf-8') as file:
        file = file.write(js.dumps(my_obj))
        return file
