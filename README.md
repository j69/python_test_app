# python_test_app
one of the test python app

# This folder contains 2 program files
* calculate_average - The first program returns the average age per hobby.
* json_check - The second program validates the format and contents of the JSON data

## Step 1 - Setup Virtualenv
* cd test
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt

## Step 2 - run file

### RUn this for first program - returns the average age per hobby.
* python calculate_average.py

### RUn this for the second program - validates the JSON data
* python json_check.py

The link to json server is in configuration file `.env`
Connection to link is in the `helpers.py` file with schema loading
The Schemas folder contains all of the schemas to map from server

Additionally we can setup the `test` folder with unittests for both programs

### TODO
And in a free time we can setup the logging into `log.file`
and beautiful `cli` output with `yaml` settings file
