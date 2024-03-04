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

    def to_xml(self):
        event_tree_element = ET.Element('define-event-tree', {'name': self.name})

        for functional_event in self.functional_events:
            functional_event_element = ET.SubElement(event_tree_element, 'define-functional-event',
                                                     {'name': functional_event})

        for sequence in self.sequences:
            sequence_element = ET.SubElement(event_tree_element, 'define-sequence', {'name': sequence})

        return event_tree_element


class FaultTree:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def to_xml(self):
        fault_tree_element = ET.Element('define-fault-tree', {'name': self.name})

        for element in self.elements:
            element_element = ET.SubElement(fault_tree_element, element['type'], {'name': element['name']})
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
