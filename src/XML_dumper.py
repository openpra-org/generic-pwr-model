import xml.etree.ElementTree as ET

class XMLDumper:
    def __init__(self):
        pass

    def dump_object_to_xml(self, parsed_object, file_path):
        try:
            tree = ET.ElementTree(parsed_object)
            tree.write(file_path, encoding="utf-8", xml_declaration=True)
        except Exception as e:
            print(f"Error dumping XML object to file {file_path}: {e}")
