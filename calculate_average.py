# Python test program for Avoine from Jyrki)
# This program queries the endpoint and returns the average age per hobby.

from json_check import validate_json
from helpers import py2_check, load_json

py2_check()

# Make request for json data
data = load_json()
if not data or 'people' not in data:
    exit('Empty JSON response')

# Convert json to python object.
people = data['people']

# Validate JSON object
is_valid, err_message = validate_json(data['people'], 'people')
if not is_valid
    exit(err_message)
    

# Get a list of ages by hobby
hobbies_counter = {}
for person in people:
    for hobby in person['hobbies']:
        hobbies_counter.setdefault(hobby, []).append(person['age'])

# Will be like
# {
#   'woodworks': [80, 51, 25, 95, 71, ...],
#   'motorcycles': [80, 51, 27, 34, ...],
#   'climbing': [51, 95, 27, 83, 41,...],
#    ...
# }

# Calculate average by age list of hobby
output = {}
for hobby in hobbies_counter:
    ages = hobbies_counter[hobby]
    output[hobby] = round(sum(ages) / len(ages))

# Will be like
#  {'woodworks': 59, 'motorcycles': 56, 'climbing': 63, 'knitting': 59, 'sleeping': 64, 'cooking': 62}
print("The average age per hobby : \n", output)
