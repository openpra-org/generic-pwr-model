import json


def compare_json_files(file1_path, file2_path):
    # Read the content of both JSON files
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)

    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    # Compare the dictionaries
    return data1 == data2


# Example usage:
file1_path = '.././saphsolve_actual_models/EQK-BIN1_et_Grp-1_24-02-26_15-57-10.JSInp'
file2_path = '.././dumped_saphsolve_actual_models/dumped_EQK-BIN1_et_Grp-1_24-02-26_15-57-10.JSInp'

result = compare_json_files(file1_path, file2_path)
if result:
    print("The JSON files are equal.")
else:
    print("The JSON files are not equal.")
