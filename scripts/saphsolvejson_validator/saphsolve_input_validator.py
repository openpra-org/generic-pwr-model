import os
import json
import csv
import glob
from jsonschema import validate, ValidationError

def validate_json(json_file, schema):
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
        validate(instance=json_data, schema=schema)
        return True, None
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON format: {e.msg}"]
    except ValidationError as e:
        return False, [e.message]

def main(json_directory, schema_file, log_file):
    try:
        with open(schema_file, 'r') as f:
            schema = json.load(f)
    except Exception as e:
        print(f"Error parsing schema file: {e}")
        return

    with open(log_file, 'w', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow(['JSON File', 'Status', 'Errors'])

        for root, _, files in os.walk(json_directory):
            for file in files:
                if file.endswith('.JSInp'):
                    json_file = os.path.join(root, file)
                    valid, error_log = validate_json(json_file, schema)
                    if valid:
                        log_writer.writerow([json_file, 'valid', ''])
                    else:
                        error_messages = "; ".join(error_log)
                        log_writer.writerow([json_file, 'invalid', error_messages])
    print(f"Validation complete. Results are logged in {log_file}")

if __name__ == "__main__":
    json_directory = "/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_actual_models/generic_PWR_V1.2"
    schema_file = "/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_schema/input_schema.json"
    log_file = "validation_log.csv"
    main(json_directory, schema_file, log_file)
