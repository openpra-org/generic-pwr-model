import os
from JSInp_parser import JSONParser
from JSInp_dumper import JSONDumper
import json

def main():
    input_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_actual_models/'
    output_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_saphsolve_actual_models/'

    # List all JSON files in the input directory
    json_files = [file for file in os.listdir(input_directory) if file.endswith('.JSInp')]

    # Parse each JSON file and dump it
    for file_name in json_files:
        input_file_path = os.path.join(input_directory, file_name)
        output_file_path = os.path.join(output_directory, f'dumped_{file_name}')

        print(f"Processing file: {input_file_path}")

        # Validate the JSON file
        try:
            with open(input_file_path, 'r') as file:
                json.load(file)
            # Parse the JSON file if it's valid
            json_parser = JSONParser(input_file_path)
            parsed_saphsolve_input_object = json_parser.parse_to_object()
            # Dump the parsed data back into another JSON file
            json_dumper = JSONDumper(parsed_saphsolve_input_object)
            json_dumper.dump_to_json(output_file_path)
            print(f"File {file_name} parsed and dumped successfully.")
        except json.JSONDecodeError as e:
            print(f"Error in file {file_name}: {e}. Skipping parsing and dumping.")

if __name__ == "__main__":
    main()
