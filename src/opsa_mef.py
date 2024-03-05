import xml.etree.ElementTree as ET


class OPSAMEF:
    def __init__(self):
        self.initiating_event = None
        self.event_tree = None
        self.fault_trees = []
        self.model_data = None

    def to_xml(self):
        opsa_mef_element = ET.Element('opsa-mef')

        if self.initiating_event:
            initiating_event_element = ET.SubElement(opsa_mef_element, 'define-initiating-event',
                                                     {'name': self.initiating_event.name,
                                                      'event-tree': self.event_tree.name})

        if self.event_tree:
            event_tree_element = self.event_tree.to_xml()
            opsa_mef_element.append(event_tree_element)

        for fault_tree in self.fault_trees:
            fault_tree_element = fault_tree.to_xml()
            opsa_mef_element.append(fault_tree_element)

        if self.model_data:
            model_data_element = self.model_data.to_xml()
            opsa_mef_element.append(model_data_element)

        return opsa_mef_element


class EventTree:
    def __init__(self, name):
        self.name = name
        self.functional_events = []
        self.sequences = []
        self.initial_state = None

    def to_xml(self):
        event_tree_element = ET.Element('define-event-tree', {'name': self.name})

        for functional_event in self.functional_events:
            functional_event_element = ET.SubElement(event_tree_element, 'define-functional-event',
                                                     {'name': functional_event})

        for sequence in self.sequences:
            sequence_element = ET.SubElement(event_tree_element, 'define-sequence', {'name': sequence})

        if self.initial_state:
            initial_state_element = ET.SubElement(event_tree_element, 'initial-state')
            self._build_initial_state_xml(self.initial_state, initial_state_element)

        return event_tree_element

    def _build_initial_state_xml(self, state, parent_element):
        fork_element = ET.SubElement(parent_element, 'fork', {'functional-event': state['functional_event']})
        for path in state['paths']:
            path_element = ET.SubElement(fork_element, 'path', {'state': path['state']})
            collect_formula_element = ET.SubElement(path_element, 'collect-formula')
            self._build_formula_xml(path['formula'], collect_formula_element)

        for child_state in state.get('children', []):
            self._build_initial_state_xml(child_state, parent_element)

    def _build_formula_xml(self, formula, parent_element):
        if isinstance(formula, dict):
            if '.root' in formula['name']:
                gate_name, reference = formula['name'].split('.')
                gate_element = ET.SubElement(parent_element, 'gate', {'name': gate_name})
                reference_element = ET.SubElement(gate_element, reference)
            else:
                gate_element = ET.SubElement(parent_element, 'gate', {'name': formula['name']})
                self._build_formula_xml(formula['child'], gate_element)
        elif isinstance(formula, str):
            basic_event_element = ET.SubElement(parent_element, 'basic-event', {'name': formula})
        elif isinstance(formula, list):
            for sub_formula in formula:
                self._build_formula_xml(sub_formula, parent_element)


class FaultTree:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def to_xml(self):
        fault_tree_element = ET.Element('define-fault-tree', {'name': self.name})

        for element in self.elements:
            element_type = element['type']
            element_name = element['name']
            element_element = ET.SubElement(fault_tree_element, element_type, {'name': element_name})

            if 'label' in element:
                label_element = ET.SubElement(element_element, 'label')
                label_element.text = element['label']

            if 'value' in element:
                float_element = ET.SubElement(element_element, 'float', {'value': element['value']})

        return fault_tree_element


class ModelData:
    def __init__(self):
        self.parameters = []
        self.basic_events = []

    def to_xml(self):
        model_data_element = ET.Element('model-data')

        for parameter in self.parameters:
            parameter_element = ET.SubElement(model_data_element, 'define-parameter', {'name': parameter['name']})
            float_element = ET.SubElement(parameter_element, 'float', {'value': parameter['value']})

        for basic_event in self.basic_events:
            basic_event_element = ET.SubElement(model_data_element, 'define-basic-event', {'name': basic_event['name']})
            label_element = ET.SubElement(basic_event_element, 'label')
            label_element.text = basic_event['label']
            float_element = ET.SubElement(basic_event_element, 'float', {'value': basic_event['value']})

        return model_data_element
