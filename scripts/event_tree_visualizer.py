import xml.etree.ElementTree as ET
import graphviz

def parse_event_tree(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initiating event and functional events
    event_tree = {}
    initiating_event = root.find('.//define-initiating-event')
    if initiating_event is not None:
        event_tree['initiating_event'] = initiating_event.get('name')

    functional_events = root.findall('.//define-functional-event')
    event_tree['functional_events'] = [fe.get('name') for fe in functional_events]

    sequences = root.findall('.//define-sequence')
    event_tree['sequences'] = [seq.get('name') for seq in sequences]

    return event_tree

def visualize_event_tree(event_tree, output_file='event_tree'):
    dot = graphviz.Digraph(comment='Event Tree')

    # Add the initiating event
    dot.node('IE', event_tree['initiating_event'], shape='box')

    # Add functional events
    for i, fe in enumerate(event_tree['functional_events'], start=1):
        dot.node(f'FE{i}', fe, shape='ellipse')
        dot.edge('IE', f'FE{i}', label='Success')
        dot.edge('IE', f'FE{i}', label='Failure')

    # Add sequences at the end
    for i, seq in enumerate(event_tree['sequences'], start=1):
        dot.node(f'SEQ{i}', seq, shape='diamond')

    dot.render(output_file, format='png')

if __name__ == "__main__":
    xml_file = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/converted_EQK-BIN1_et_Grp-1_24-02-26_15-57-10.xml'  # replace with your XML file path
    event_tree = parse_event_tree(xml_file)
    visualize_event_tree(event_tree)
