import xml.etree.ElementTree as ET
import os


def modify_fault_tree_gates(root):
    """Modifies gates with a single element in <define-fault-tree> and changes <and> to <or>."""
    single_element_found = False
    for fault_tree in root.findall(".//define-fault-tree"):
        for gate in fault_tree.findall(".//define-gate"):
            if len(gate) == 1:
                first_child = gate[0]

                # Check if the gate has only one child element and if it's <and>
                if first_child.tag == 'and' and len(first_child) == 1:
                    # Change <and> to <or>
                    first_child.tag = 'or'
                    single_element_found = True  # Mark as modified

                # Add <basic-event name="BE0"/> under the gate's single element
                if len(first_child) == 1:
                    new_event = ET.Element('basic-event', name='BE0')
                    first_child.append(new_event)
                    single_element_found = True  # Track modification
    return single_element_found


def add_elements_to_model_data(root):
    """Adds the specified basic event to <model-data>."""
    model_data = root.find(".//model-data")
    if model_data is not None:
        new_basic_event = ET.Element('define-basic-event', name='BE0')
        label = ET.SubElement(new_basic_event, 'label')
        label.text = 'TEMP-BE-TO-ADD-GATES-WITH-A-SINGLE-ELEMENT'
        float_value = ET.SubElement(new_basic_event, 'float', value='0.000000E+00')
        model_data.append(new_basic_event)


def process_xml(file_path):
    """Processes a single XML file by modifying fault trees and adding model data if necessary."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Modify gates and return if any single element was found or <and> was changed
        single_element_found = modify_fault_tree_gates(root)

        # Only add to <model-data> if a single element was found or <and> was changed
        if single_element_found:
            add_elements_to_model_data(root)
            # Save the modified XML file, overwriting the original
            tree.write(file_path)
            print(f"{file_path} modified")
        else:
            print(f"{file_path} NOT modified")
    except ET.ParseError:
        print(f"Failed to parse {file_path}, skipping.")


def process_all_xml_in_folder(folder_path):
    """Processes all XML files in the specified folder."""
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xml'):
            file_path = os.path.join(folder_path, file_name)
            process_xml(file_path)


def main():
    """Main function to trigger the processing of XML files."""
    folder_path = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/'
    if os.path.exists(folder_path):
        print(f"Processing XML files in folder: {folder_path}")
        process_all_xml_in_folder(folder_path)
    else:
        print(f"Folder not found: {folder_path}")


if __name__ == "__main__":
    main()
