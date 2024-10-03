#!/usr/bin/python3
"""
pull from json
"""
import json as js


def load_from_json_file(filename):
    """
    load
    """
    with open(filename) as file:
        return js.load(file)
