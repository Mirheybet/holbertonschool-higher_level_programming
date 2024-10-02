#!/usr/bin/python3
"""
from file to json
"""
import json as js


def save_to_json_file(my_obj, filename):
    """
    duump with write
    """
    with open("my_dict.json", "w") as file:
        return js.dump(my_obj, file)
