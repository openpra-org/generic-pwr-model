import xml.etree.ElementTree as ET
import xml.dom.minidom
import html

class XMLDumper:
    def __init__(self):
        pass

    def dump_object_to_xml(self, parsed_object, file_path):
        try:
            # Create ElementTree object
            tree = ET.ElementTree(parsed_object)

            # Convert ElementTree to string
            xml_string = ET.tostring(parsed_object, encoding="utf-8", xml_declaration=True)

            # Parse XML string to minidom Document
            dom = xml.dom.minidom.parseString(xml_string)

            # Beautify XML
            beautified_xml = dom.toprettyxml()

            # Unescape XML entities
            unescaped_xml = html.unescape(beautified_xml)

            # Write unescaped XML to file
            with open(file_path, "w") as xml_file:
                xml_file.write(unescaped_xml)
        except Exception as e:
            print(f"Error dumping XML object to file {file_path}: {e}")
