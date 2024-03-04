import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self):
        pass

    def parse(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            return root
        except ET.ParseError as e:
            print(f"Error parsing XML file {file_path}: {e}")
            return None
