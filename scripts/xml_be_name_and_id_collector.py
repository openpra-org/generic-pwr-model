import xml.etree.ElementTree as ET
import csv
import glob
import os


def parse_xml_file(xml_file):
    """
    Parse a single XML file to extract unique (name, label, value) triples.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        set: A set of (name, label, value) tuples.
    """
    unique_triples = set()
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for event in root.findall(".//model-data/define-basic-event"):
        name = event.get("name")
        label = event.find("label").text if event.find("label") is not None else "N/A"
        value = event.find("float").get("value") if event.find("float") is not None else "N/A"
        unique_triples.add((name, label, value))

    return unique_triples


def collect_unique_data(xml_folder):
    """
    Collect unique (name, label, value) triples from all XML files in a directory.

    Args:
        xml_folder (str): Directory path containing XML files.

    Returns:
        list: A sorted list of unique (name, label, value) triples across all files.
    """
    all_unique_data = set()

    for xml_file in glob.glob(os.path.join(xml_folder, "*.xml")):
        all_unique_data.update(parse_xml_file(xml_file))

    return sorted(all_unique_data, key=lambda x: x[0])  # Sort by Name


def write_to_csv(data, output_csv):
    """
    Write unique (index, name, label, value) data to a CSV file.

    Args:
        data (list): List of (name, label, value) tuples.
        output_csv (str): Path to the output CSV file.
    """
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Name", "Label", "Value"])  # Header
        for idx, (name, label, value) in enumerate(data, start=1):
            writer.writerow([idx, name, label, value])

    print(f"Unique data extracted and saved to {output_csv}")


def write_to_readme(data, readme_file):
    """
    Write unique (index, name, label, value) data to a README.md file in ordered format.

    Args:
        data (list): List of (name, label, value) tuples.
        readme_file (str): Path to the output README.md file.
    """
    with open(readme_file, mode="w") as file:
        file.write("# Basic Events Data\n\n")
        file.write(f"Total Entries: {len(data)}\n\n")
        file.write("| Index | Name | Label | Value |\n")
        file.write("|-------|------|-------|-------|\n")
        for idx, (name, label, value) in enumerate(data, start=1):
            file.write(f"| {idx} | {name} | {label} | {value} |\n")

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


# Define paths for XML folder and output files
xml_folder = '.././saphsolve_to_openpsamef_actual_models/dump/'
output_csv = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/be_name_and_id.csv'
readme_file = '.././saphsolve_to_openpsamef_actual_models/generic_PWR_V1.2/README_be_name_and_id.md'

# Run the main function
if __name__ == "__main__":
    main(xml_folder, output_csv, readme_file)
