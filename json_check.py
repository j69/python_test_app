# Python test program for Avoine from Jyrki)
# This program queries the endpoint and validates the format and contents of the JSON data

from jsonschema import validate, exceptions
from helpers import get_schema, py2_check, load_json

py2_check()


def validate_json(json_data, schema_name):
    """Validate the JSON file with the schema"""
    try:
        validate(instance=json_data, schema=get_schema(schema_name))
    except exceptions.ValidationError as err:
        # we should put it also in logger here
        print('ValidationError:', err)
        return False, 'JSON data is InValid'

    return True, 'JSON data is Valid'


def main():
    """Load JSON and validates it"""

    # Make request for json data
    data = load_json()
    if not data or 'people' not in data:
        exit('Empty JSON response')

    # Additional check
    if not data or 'people' not in data:
        return False, 'Empty JSON response'

    # Validate JSON object
    return validate_json(data['people'], 'people')


if __name__ == "__main__":
    print(main())
