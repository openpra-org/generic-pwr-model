import xml.etree.ElementTree as ET
import csv
import glob
import os


def parse_xml_file(xml_file):
    """
    Parse a single XML file to extract unique (name, label) pairs.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        set: A set of (name, label) tuples.
    """
    unique_pairs = set()
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for event in root.findall(".//define-functional-event"):
        name = event.get("name")
        label = event.find("label").text if event.find("label") is not None else None
        unique_pairs.add((name, label))

    return unique_pairs


def collect_unique_data(xml_folder):
    """
    Collect unique (name, label) pairs from all XML files in a directory.

    Args:
        xml_folder (str): Directory path containing XML files.

    Returns:
        set: A set of unique (name, label) pairs across all files.
    """
    all_unique_data = set()

    for xml_file in glob.glob(os.path.join(xml_folder, "*.xml")):
        all_unique_data.update(parse_xml_file(xml_file))

    return all_unique_data


def write_to_csv(data, output_csv):
    """
    Write unique (name, label) data to a CSV file.

    Args:
        data (set): Set of (name, label) tuples.
        output_csv (str): Path to the output CSV file.
    """
    sorted_data = sorted(data, key=lambda x: x[0])  # Sort by Name
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Label"])  # Header
        writer.writerows(sorted_data)

    print(f"Unique data extracted and saved to {output_csv}")


def write_to_readme(data, readme_file):
    """
    Write unique (name, label) data to a README.md file in ordered format.

    Args:
        data (set): Set of (name, label) tuples.
        readme_file (str): Path to the output README.md file.
    """
    sorted_data = sorted(data, key=lambda x: x[0])  # Sort by Name
    with open(readme_file, mode="w") as file:
        file.write("# Functional Events\n\n")
        file.write("| Name | Label |\n")
        file.write("|------|-------|\n")
        for name, label in sorted_data:
            file.write(f"| {name} | {label if label else 'N/A'} |\n")

    print(f"Unique data extracted and saved to {readme_file}")


def main(xml_folder, output_csv, readme_file):
    """
    Main function to parse XML files, extract unique data, and write to CSV and README.md.

    Args:
        xml_folder (str): Directory path containing XML files.
        output_csv (str): Path to the output CSV file.
        readme_file (str): Path to the output README.md file.
    """
    unique_data = collect_unique_data(xml_folder)
    write_to_csv(unique_data, output_csv)
    write_to_readme(unique_data, readme_file)


# Define paths for XML folder and output CSV file
xml_folder = '.././saphsolve_to_openpsamef_actual_models/dump/'
output_csv = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/fe_name_and_id.csv'
readme_file = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/README.md'

# Run the main function
if __name__ == "__main__":
    main(xml_folder, output_csv, readme_file)

