#!/usr/bin/python3
"""
basic serialization
"""
import json as js


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    """
    dump
    """

    with open(filename, 'w') as file:
        data_js = js.dump(data, file)


"""
basic deserialization
"""


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    """
    load
    """

    with open(filename) as file:
        data_js = js.load(file)
        return (data_js)
