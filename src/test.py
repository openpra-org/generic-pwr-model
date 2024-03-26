import xml.etree.ElementTree as ET
import xml.dom.minidom
import html
import copy
import pprint


initial_state_data = {
    "name": "fork",
    "attributes": {"functional-event": ""},
    "children": [
        {
            "name": "path",
            "attributes": {"state": "Success"},
            "children": [
                {
                    "name": "collect-formula",
                    "children": [
                        {
                            "name": "not",
                            "children": [{
                                "name": "gate",
                                "attributes": {"name": ""}
                            }]
                        }
                    ]
                }
            ]
        },
        {
            "name": "path",
            "attributes": {"state": "Failure"},
            "children": [
                {
                    "name": "collect-formula",
                    "children": [
                        {
                            "name": "gate",
                            "attributes": {"name": ""}
                        }
                    ]
                }
            ]
        }
    ]
}

sequence_element = {
        "name": "sequence",
        "attributes": {"name": ""}
    }

def deep_copy_dict(dictionary):
    """
    Deep copy a dictionary and all nested dictionaries.
    """
    return {key: (deep_copy_dict(value) if isinstance(value, dict) else copy.deepcopy(value)) for key, value in dictionary.items()}

def append_initial_state_data(final_state_data, fork_level, initial_state_data, deep_copy_dict, success_path):
    current_fork = final_state_data
    if fork_level < 2:
        current_fork = current_fork["children"][-2 if success_path else -1]
    else:
        for _ in range(fork_level - 1):
            current_fork = current_fork["children"][-2]["children"][-1]["children"][-2 if success_path else -1]
    current_fork["children"].append(deep_copy_dict(initial_state_data))
    return final_state_data


"""fork#1 with 2 end sequences"""
final_state_data = deep_copy_dict(initial_state_data)
"""end fork#1"""

"""fork#2 with 4 end sequences"""
final_state_data["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
"""end fork#2"""

"""fork#3 with 8 end sequences"""
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
"""end fork#3"""

"""fork#4 with 16 end sequences"""
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
"""end fork#4"""

"""fork#5 with 32 end sequences"""
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
"""end fork#5"""

"""fork#6 with 64 end sequences"""
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
"""end fork#6"""


"""fork#7 with 128 end sequences"""

"""end fork#7"""

def dict_to_xml(dictionary):
    element = ET.Element(dictionary["name"], dictionary.get("attributes", {}))
    for child_dict in dictionary.get("children", []):
        child_element = dict_to_xml(child_dict)
        element.append(child_element)
    return element

def prettify_xml(xml_string):
    dom = xml.dom.minidom.parseString(xml_string)
    return dom.toprettyxml()

def write_xml_to_file(xml_string, file_path):
    with open(file_path, "w") as xml_file:
        xml_file.write(xml_string)

xml_tree = dict_to_xml({"name": "initial-state", "children": [final_state_data]})
xml_string = ET.tostring(xml_tree, encoding="unicode", method="xml")

# Prettify XML
prettified_xml = prettify_xml(xml_string)
# Unescape XML entities
unescaped_xml = html.unescape(prettified_xml)

file_path = "/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/c.xml"
write_xml_to_file(prettified_xml, file_path)
