""""``main.py`` is a Python script that demonstrates how to call the SolveFromInput function from the SolverSaphire.dll"""

from ctypes import *
import os

try:
    # Load the DLL
    mydll = cdll.LoadLibrary(r"C:\Users\egeme\Saphire 8\tools\SolverSaphire.dll")
except OSError as e:
    print("Error:", e)
    exit(1)  # Exit the script if DLL loading fails


def solve_json_file(input_file_path, output_file_path):
    try:
        # Call the SolveFromInput function from the DLL
        mydll.SolveFromInput(input_file_path, output_file_path)
        print(f"Solved {input_file_path}")  # Print a message indicating successful completion
    except OSError as e:
        print("Error:", e)
        exit(2)  # Exit the script if SolveFromInput fails


def main():
    input_directory = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\dumped_saphsolve_actual_models"
    output_directory = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\output_dumped_saphsolve_actual_models"

    # List all JSON files in the input directory
    json_files = [file for file in os.listdir(input_directory) if file.endswith('.JSInp')]

    # Solve each JSON file
    for file_name in json_files:
        input_file_path = os.path.join(input_directory, file_name)
        output_file_path = os.path.join(output_directory, f'dumped_{file_name}')

        # Solve the JSON file
        solve_json_file(input_file_path, output_file_path)


if __name__ == "__main__":
    main()
