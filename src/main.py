import os
import json
from JSInp_parser import JSONParser
from JSInp_dumper import JSONDumper
from XML_parser import XMLParser
from XML_dumper import XMLDumper
from JSInp_to_XML_converter import JSONtoXMLConverter
import xml.etree.ElementTree as ET

def main():
    # # Input and output directories for JSON files
    global parsed_json_object
    json_input_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/saphsolve_actual_models/'
    json_output_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_saphsolve_actual_models/'

    # Input and output directories for XML files
    # xml_input_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/openpsamef_synthetical_models/'
    # xml_output_directory = '/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/dumped_openpsamef_synthetical_models/'

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

    # Assuming parsed_json_object is already defined
    json_to_xml_converter = JSONtoXMLConverter(parsed_json_object)
    xml_output = json_to_xml_converter.convert_to_xml()
    print(xml_output)
    for element in xml_output:
        print(ET.tostring(element))

    # Create XML dumper
    xml_dumper = XMLDumper()
    xml_dumper.dump_object_to_xml(xml_output, "/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/b.xml")
    print(f"XML file {xml_output} parsed and dumped successfully.")

if __name__ == "__main__":
    main()
