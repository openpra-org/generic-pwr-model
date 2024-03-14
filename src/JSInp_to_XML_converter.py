from opsa_mef import ModelData, FaultTreeOpenPSA, EventTree
import xml.etree.ElementTree as ET

from JSInp_parser import FaultTree


class JSONtoXMLConverter:
    def __init__(self, parsed_json_object):
        self.parsed_json_object = parsed_json_object

    def convert_to_xml(self):
        event_trees = self._convert_sequencelist_to_eventteee()
        fault_trees = self._convert_faulttreelist_to_faulttree()
        model_data = self._convert_eventlist_to_modeldata()

        # Convert each FaultTree object to XML
        xml_event_trees = event_trees.to_xml()
        xml_fault_trees = [ft.to_xml() for ft in fault_trees]
        xml_model_data = model_data.to_xml()

        # Create a root XML element to hold both fault trees and model data
        root_element = ET.Element('')

        # Append XML representation of event trees to the root element
        root_element.append(xml_event_trees)

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

    def _convert_sequencelist_to_eventteee(self):
        # Accessing sysgatelist attribute directly from parsed JSON object
        sysgatelist = self.parsed_json_object.saphiresolveinput.get('sysgatelist', [])
        # Accessing sequencelist attribute directly from parsed JSON object
        sequencelist = self.parsed_json_object.saphiresolveinput.get('sequencelist', [])

        event_tree_name = self.parsed_json_object.saphiresolveinput.get('header', {}).eventtree.name
        initiating_event_id = self.parsed_json_object.saphiresolveinput.get('header',{}).eventtree.initevent
        event_tree = EventTree(event_tree_name)
        # event_trees = []  # List to hold EventTree objects

        initial_state_data = {
            "name": "fork",
            "attributes": {"functional-event": []},  # Initialize as an empty list
            "children": []
        }
        # Initialize an empty list to hold the children states
        children_states = []


        # Iterate over both lists simultaneously
        for seqname in sysgatelist:
            id = str(seqname.id)
            event_tree.functional_events.append(id)

        event_tree.initial_state = initial_state_data

        logiclist =[]
        for sequence in sequencelist:
            seqid = str(sequence.seqid)
            event_tree.sequences.append(seqid)

            logic_list = sequence.logiclist
            logiclist.append(logic_list)

        """Compare elements within sub-lists and call appropriate function."""
        max_length = max(len(sublist) for sublist in logiclist)  # Find the maximum length
        for i in range(max_length):
            elements = [sublist[i] if i < len(sublist) else None for sublist in logiclist]

            # Convert each element to binary and consider only the first 17 digits
            binary_elements_funtionalevent_id = [self.decimal_to_binary_beid(element) if element is not None else None for element in
                                    elements]
            # print(binary_elements_beid)
            binary_elements = [self.decimal_to_binary(element) if element is not None else None for element in elements]

            # Check if all elements at this position are equal
            if any(binary_elements_funtionalevent_id[0] == element for element in binary_elements_funtionalevent_id):
                # Here you handle the case where elements differ
                initial_state_data["attributes"]["functional-event"].append(str(binary_elements_funtionalevent_id[0]))
                for elem in binary_elements_funtionalevent_id:
                    if elem != binary_elements_funtionalevent_id[0]:
                        pass
                        # Correctly navigate to "functional-event" and append
                        # initial_state_data["attributes"]["functional-event"].append(str(elem))
                self.function_for_different_elements(i)

            else:
                # Call function for different elements
                self.function_for_different_elements(i)



        return event_tree



    def decimal_to_binary(self, dec):
        """Convert decimal to binary"""
        binary = bin(dec)[2:]  # Convert decimal to binary, excluding the '0b' prefix
        return binary

    def decimal_to_binary_beid(self, dec):
        """Convert decimal to binary, extract the last 17 digits, and return their decimal representation."""
        binary = bin(dec)[2:]  # Convert decimal to binary, excluding the '0b' prefix
        last_17_binary = binary[-17:]  # Extract the last 17 digits

        # Convert the last 17 binary digits back to a decimal number
        decimal_representation = int(last_17_binary, 2) if len(last_17_binary) > 0 else 0
        return decimal_representation

    def function_for_equal_elements(self,position):
        print(f"At least 1 element at position {position} are equal")

    def function_for_different_elements(self, position):
        print(f"Elements at position {position} are different")













