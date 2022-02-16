# This is additional help functions for main programs

import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()


def py2_check():
    """NO more Python2 checks =)"""
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")


def get_schema(name):
    """This function loads the given schema from schemas module"""
    with open('./schemas/{}.json'.format(name), 'r') as file:
        schema = json.load(file)
    return schema


def load_json():
    """This function loads the json data from link"""
    r = requests.get(os.getenv('LINK'))
    # Check for status = 200 - if not will Raise HTTPError
    r.raise_for_status()
    return r.json()
