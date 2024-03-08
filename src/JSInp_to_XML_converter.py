from opsa_mef import ModelData, FaultTreeOpenPSA
import xml.etree.ElementTree as ET

from JSInp_parser import FaultTree


class JSONtoXMLConverter:
    def __init__(self, parsed_json_object):
        self.parsed_json_object = parsed_json_object

    def convert_to_xml(self):
        model_data = self._convert_eventlist_to_modeldata()
        fault_trees = self._convert_faulttreelist_to_faulttree()

        # Convert each FaultTree object to XML
        xml_fault_trees = [ft.to_xml() for ft in fault_trees]
        xml_model_data = model_data.to_xml()

        # Create a root XML element to hold both fault trees and model data
        root_element = ET.Element('')

        # Append XML representation of fault trees to the root element
        for xml_fault_tree in xml_fault_trees:
            root_element.append(xml_fault_tree)

        # Append XML representation of model data to the root element
        root_element.append(xml_model_data)

        return root_element

    def _convert_eventlist_to_modeldata(self):
        model_data = ModelData()

        # Accessing eventlist attribute directly from parsed JSON object
        eventlist = self.parsed_json_object.saphiresolveinput.get('eventlist', [])

        for event in eventlist:
                if event.corrgate == "0":
                    name = event.id
                    label = event.name
                    value = event.value

                    if label in ["<TRUE>", "<FALSE>", "<PASS>"]:
                        continue

                    model_data.add_basic_event(name, label=label, float_value=value)

        return model_data

    def _convert_faulttreelist_to_faulttree(self):
        faulttreelist = self.parsed_json_object.saphiresolveinput.get("faulttreelist", [])
        combined_fault_trees = []

        for ft_data in faulttreelist:
            ftheader = ft_data.ftheader  # Accessing attributes directly
            name = str(ftheader.get("ftid"))  # Accessing name attribute of ftheader
            ft = FaultTreeOpenPSA(name)

            gatelist = ft_data.gatelist
            for gate_data in gatelist:
                gate_id = str(gate_data.gateid)
                gate_type = gate_data.gatetype
                gate_inputs = gate_data.gateinput
                event_inputs = gate_data.eventinput

                if gate_type in ["or", "and"]:
                    # Check if gate_inputs is an integer (indicating it's empty)
                    if isinstance(gate_inputs, int):
                        gate_inputs = []  # Convert it to an empty list
                    else:
                        # Convert gate_inputs to a list if it's not already one
                        if not isinstance(gate_inputs, list):
                            gate_inputs = [gate_inputs]

                    # Iterate through gate_inputs and add each input individually
                    for input_name in gate_inputs:
                        input_name = str(input_name)  # Convert integer to string
                        ft.add_gate(gate_id, gate_type, input_name)
                elif "/" in gate_type:  # Custom gate type like "2/3"
                    min_required = gate_type.split("/")[0]
                    ft.add_gate(gate_id, min_required, gate_inputs)  # Use min_required as gate_type
                if event_inputs is not None:
                    # Check if gate_inputs is an integer (indicating it's empty)
                    if isinstance(event_inputs, int):
                        event_inputs = []  # Convert it to an empty list
                    else:
                        # Convert gate_inputs to a list if it's not already one
                        if not isinstance(event_inputs, list):
                            event_inputs = [event_inputs]
                    # Iterate through event_inputs and add each input individually
                    for input_name in event_inputs:
                        if input_name is not None:
                            input_name = str(input_name)
                            ft.add_basic_event(gate_id, input_name)

            combined_fault_trees.append(ft)

        return combined_fault_trees











