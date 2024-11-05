import xml.etree.ElementTree as ET
import csv
import glob
import os


def load_labels_from_csv(csv_file):
    """
    Load (name, label) pairs from the CSV file into a dictionary.

    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        dict: A dictionary with 'name' as keys and 'label' as values.
    """
    labels_dict = {}
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Name"]
            label = row["Label"]
            labels_dict[name] = label
    return labels_dict


def update_xml_file(xml_file, labels_dict, target_folder):
    """
    Update an XML file by adding missing labels based on the provided dictionary,
    and save it to the target folder.

    Args:
        xml_file (str): Path to the XML file in the input folder.
        labels_dict (dict): Dictionary of name-label pairs.
        target_folder (str): Directory where updated XML files will be saved.

    Returns:
        bool: True if the file was modified, False otherwise.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    modified = False

    for event in root.findall(".//define-functional-event"):
        name = event.get("name")
        if name in labels_dict:
            # Check if the label element is missing or empty
            label_element = event.find("label")
            if label_element is None:
                # Add the label element with the value from the dictionary
                label_element = ET.SubElement(event, "label")
                label_element.text = labels_dict[name]
                modified = True
            elif not label_element.text:
                # Update label text if it’s empty
                label_element.text = labels_dict[name]
                modified = True

    if modified:
        # Create target folder if it doesn't exist
        os.makedirs(target_folder, exist_ok=True)
        # Define the output path in the target folder
        target_file = os.path.join(target_folder, os.path.basename(xml_file))
        tree.write(target_file)  # Save the updated XML to the target folder
        print(f"Updated {xml_file} and saved to {target_file}")
    return modified


def update_xml_files_in_folder(input_folder, target_folder, labels_dict):
    """
    Update XML files in the input folder using the labels dictionary and save
    updated files to the target folder.

    Args:
        input_folder (str): Directory path containing XML files to be updated.
        target_folder (str): Directory where updated XML files will be saved.
        labels_dict (dict): Dictionary of name-label pairs.
    """
    for xml_file in glob.glob(os.path.join(input_folder, "*.xml")):
        update_xml_file(xml_file, labels_dict, target_folder)


def main(csv_file, input_folder, target_folder):
    """
    Main function to load labels from CSV and update XML files in the input folder,
    then save the updated files to the target folder.

    Args:
        csv_file (str): Path to the CSV file.
        input_folder (str): Directory path containing XML files to be updated.
        target_folder (str): Directory where updated XML files will be saved.
    """
    labels_dict = load_labels_from_csv(csv_file)
    update_xml_files_in_folder(input_folder, target_folder, labels_dict)


# Define paths for the CSV file, input folder, and target folder
csv_file = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/fe_name_and_id.csv'
input_folder = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/'
target_folder = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/fe_updated'

# Run the main function
if __name__ == "__main__":
    main(csv_file, input_folder, target_folder)
