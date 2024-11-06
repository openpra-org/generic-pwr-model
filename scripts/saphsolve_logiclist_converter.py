import json
import os


class LogicListConverter:
    def decimal_to_binary_id(self, dec):
        """Convert decimal to binary, extract the last 17 digits, and return their decimal representation."""
        binary = bin(dec)[2:]  # Convert decimal to binary, excluding the '0b' prefix
        last_17_binary = binary[-17:]  # Extract the last 17 digits

        # Convert the last 17 binary digits back to a decimal number
        decimal_representation = int(last_17_binary, 2) if len(last_17_binary) > 0 else 0
        return decimal_representation

    def convert_logiclist_to_binary(self, logiclist):
        binary_logiclist = []

        for sublist in logiclist:
            binary_sublist = []
            for decimal_number in sublist:
                # Check the length of the decimal number before conversion
                suffix = 'f' if len(str(decimal_number)) == 6 else 's'
                binary_number = self.decimal_to_binary_id(decimal_number)
                binary_sublist.append(suffix + str(binary_number))
            binary_logiclist.append(binary_sublist)

        return binary_logiclist


def update_sequencelist(input_filepath, output_filepath):
    # Read the input JSON file
    with open(input_filepath, 'r') as f:
        data = json.load(f)

    # Extract the "sequencelist"
    sequencelist = data.get("saphiresolveinput", {}).get("sequencelist", [])

    # Initialize the converter
    converter = LogicListConverter()

    # Convert the "logiclist" elements to binary
    for sequence in sequencelist:
        if 'logiclist' in sequence:
            # Wrap logiclist in a list of lists for uniform processing
            sequence['logiclist'] = converter.convert_logiclist_to_binary([sequence['logiclist']])[0]

    # Write the updated "sequencelist" to the output JSON file
    with open(output_filepath, 'w') as f:
        json.dump(data, f, indent=4)


def process_directory(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.JSInp'):
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, os.path.splitext(filename)[0] + '.json')
            update_sequencelist(input_filepath, output_filepath)
            print(f'Processed {input_filepath} -> {output_filepath}')


def main():
    input_dir = '.././saphsolve_actual_models/generic_PWR_V1.2/'
    output_dir = '.././saphsolve_actual_models/generic_PWR_V1.2/logiclist_info'

    process_directory(input_dir, output_dir)


if __name__ == "__main__":
    main()
