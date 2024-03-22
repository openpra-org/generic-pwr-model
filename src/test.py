import xml.etree.ElementTree as ET
import xml.dom.minidom
import html
import copy
import pprint

# Define the initial state data
initial_state_data = {
            "name": "fork",
            "attributes": {"functional-event": ""},
            "children": []
        }
path_success_data = {
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
                    }]}
            ]
        }
    ]
}

path_failure_data = {
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

sequence_element = {
        "name": "sequence",
        "attributes": {"name": ""}
    }

def deep_copy_dict(dictionary):
    """
    Deep copy a dictionary and all nested dictionaries.
    """
    return {key: (deep_copy_dict(value) if isinstance(value, dict) else copy.deepcopy(value)) for key, value in dictionary.items()}


final_state_data = deep_copy_dict(initial_state_data)
"""fork#1"""
final_state_data["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"].append(deep_copy_dict(sequence_element))
"""end fork#1"""

"""fork#2"""
final_state_data["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"].append(deep_copy_dict(initial_state_data))

final_state_data["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
"""end fork#2"""

"""fork#3"""
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
"""end fork#3"""

"""fork#4"""
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"].append(deep_copy_dict(initial_state_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(initial_state_data))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
"""end fork#4"""

"""fork#5"""
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

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-2]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_success_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(path_failure_data))
final_state_data["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"][-1]["children"].append(deep_copy_dict(sequence_element))

"""end fork#5"""


# """sequence number"""
# final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"].append(sequence_element)
#
# print(final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2],
#       type(final_state_data["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]["children"][-1]["children"][-2]))


def dict_to_xml(dictionary):
    element = ET.Element(dictionary["name"], dictionary.get("attributes", {}))
    for child_dict in dictionary.get("children", []):
        child_element = dict_to_xml(child_dict)
        element.append(child_element)
    return element

xml_tree = dict_to_xml({"name": "initial-state", "children": [final_state_data]})
xml_string = ET.tostring(xml_tree, encoding="unicode", method="xml")

# Parse XML string to minidom Document
dom = xml.dom.minidom.parseString(xml_string)

# Beautify XML
beautified_xml = dom.toprettyxml()

# Unescape XML entities
unescaped_xml = html.unescape(beautified_xml)
file_path = "/Users/afshar-flow/Repo/Gitlab/Enhancement-of-PRA-Tools/Model-Exchange/model-converter/c.xml"
# Write unescaped XML to file
with open(file_path, "w") as xml_file:
    xml_file.write(unescaped_xml)
