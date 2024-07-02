"""
This module contains the main functions for the API Testing Toolkit

Functions:
    display(data) -> None
    load_env(name: str) -> object
"""

from requests.structures import CaseInsensitiveDict
from IPython.display import JSON, display as ipy_display
import json


def display(data, label=None):
    """
    Display the data in a nice way, does not return anything but uses the IPython display function
    :param data: Some (mostly) JSON-able data
    :param label: Optional label to display
    :return: None
    """

    if isinstance(data, CaseInsensitiveDict):
        data = dict(data)  # just reset it

    if isinstance(data, dict):
        data = JSON(data, expanded=True)

    if label:
        print(label + ':')

    ipy_display(data)
    print('')  # add a new line


d = display  # alias for display


def load_env(name: str) -> object:
    """
    Load the environment variables from the env folder
    :param name: The name of the JSON document to load
    :return: The JSON object
    """

    try:
        f = open('env/{}.json'.format(name))
        return json.load(f)
    except FileNotFoundError:
        print('no env found, returning nothing')
        return {}
