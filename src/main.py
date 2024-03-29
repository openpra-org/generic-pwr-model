import os
import json
from JSInp_parser import JSONParser
from JSInp_dumper import JSONDumper
from XML_parser import XMLParser
from XML_dumper import XMLDumper
from JSInp_to_XML_converter import JSONtoXMLConverter
import xml.etree.ElementTree as ET

def main():

    # parsing json and dumping json
    json_input_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_actual_models/generic_PWR/'
    json_output_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_saphsolve_actual_models/generic_PWR/'

    # List all JSON files in the JSON input directory
    json_files = [file for file in os.listdir(json_input_directory) if file.endswith('.JSInp')]

    # Parse each JSON file and dump it
    for file_name in json_files:
        input_file_path = os.path.join(json_input_directory, file_name)
        output_file_path = os.path.join(json_output_directory, f'dumped_{file_name}')

        print(f"Processing JSON file: {input_file_path}")

        try:
            # Parse the JSON file
            json_parser = JSONParser(input_file_path)
            parsed_json_object = json_parser.parse_to_object()

            # Dump the parsed data into another JSON file
            json_dumper = JSONDumper(parsed_json_object)
            json_dumper.dump_to_json(output_file_path)

            print(f"JSON file {file_name} parsed and dumped successfully.")
        except json.JSONDecodeError as e:
            print(f"Error in JSON file {file_name}: {e}. Skipping parsing and dumping.")
    #
    # # parsing xml and dumping xml
    # # Input and output directories for XML files
    # xml_input_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/openpsamef_synthetical_models/'
    # xml_output_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_openpsamef_synthetical_models/'
    #
    # # List all XML files in the XML input directory
    # xml_files = [file for file in os.listdir(xml_input_directory) if file.endswith('.xml')]
    #
    # # Create XML parser
    # xml_parser = XMLParser()
    #
    # # Create XML dumper
    # xml_dumper = XMLDumper()
    #
    # # Parse each XML file and dump it
    # for file_name in xml_files:
    #     input_file_path = os.path.join(xml_input_directory, file_name)
    #     output_file_path = os.path.join(xml_output_directory, f'dumped_{file_name}')
    #
    #     print(f"Processing XML file: {input_file_path}")
    #
    #     try:
    #         # Parse the XML file
    #         parsed_object = xml_parser.parse(input_file_path)
    #
    #         # Dump the parsed data into another XML file
    #         xml_dumper.dump_object_to_xml(parsed_object, output_file_path)
    #
    #         print(f"XML file {file_name} parsed and dumped successfully.")
    #
    #     except Exception as e:
    #         print(f"Error in XML file {file_name}: {e}. Skipping parsing and dumping.")

    # # converting json to xml
    # json_to_be_converted_input_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_saphsolve_actual_models/ETH_BWR/'
    # xml_converted_output_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_to_openpsamef_actual_models/ETH_BWR'
    #
    # # List all JSON files in the JSON input directory
    # json_files_to_be_converted = [file for file in os.listdir(json_to_be_converted_input_directory) if file.endswith('.JSInp')]
    #
    # # Parse each JSON file and dump it
    # for file_name in json_files_to_be_converted:
    #     input_file_path = os.path.join(json_to_be_converted_input_directory, file_name)
    #     output_file_path = os.path.join(xml_converted_output_directory, f'converted_{os.path.splitext(file_name)[0]}.xml')
    #
    #     print(f"Processing JSON file: {input_file_path}")
    #
    #     try:
    #         # Parse the JSON file
    #         json_parser = JSONParser(input_file_path)
    #         parsed_json_object = json_parser.parse_to_object()
    #
    #         # Assuming parsed_json_object is already defined
    #         json_to_xml_converter = JSONtoXMLConverter(parsed_json_object)
    #         xml_output = json_to_xml_converter.convert_to_xml()
    #
    #         # Create XML dumper
    #         xml_dumper = XMLDumper()
    #         xml_dumper.dump_object_to_xml(xml_output,output_file_path)
    #
    #
    #         print(f"JSON file {file_name} parsed and converted successfully.")
    #     except json.JSONDecodeError as e:
    #         print(f"Error in JSON file {file_name}: {e}. Skipping parsing and dumping.")


if __name__ == "__main__":
    main()
