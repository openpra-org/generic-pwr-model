from JSInp_parser import JSONParser
from JSInp_dumper import JSONDumper

def main():
    JSInp_file_path = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_actual_models/EQK-BIN1_et_Grp-1_24-02-26_15-57-10.JSInp'
    dumped_JSInp_file_path = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_saphsolve_actual_models/dumped_EQK-BIN1_et_Grp-1_24-02-26_15-57-10.JSInp'

    # Parse the JSON file
    json_parser = JSONParser(JSInp_file_path)
    # parsed_saphsolve_input = json_parser.parse_from_json()

    # Convert parsed data to Python objects
    parsed_saphsolve_input_object = json_parser.parse_to_object()

    # Dump the parsed data back into another JSON file
    json_dumper = JSONDumper(parsed_saphsolve_input_object)
    json_dumper.dump_to_json(dumped_JSInp_file_path)

if __name__ == "__main__":
    main()
