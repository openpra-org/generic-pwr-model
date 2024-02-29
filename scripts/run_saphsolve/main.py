from ctypes import *
import os
import time

try:
    # Load the DLL
    mydll = cdll.LoadLibrary(r"C:\Users\egeme\Saphire 8\tools\SolverSaphire.dll")
except OSError as e:
    print("Error:", e)
    exit(1)  # Exit the script if DLL loading fails


def solve_json_file(input_file_path, output_directory):
    try:
        # Generate the output file path with the .JSCut extension
        output_file_name = os.path.splitext(os.path.basename(input_file_path))[0] + ".JSCut"
        output_file_path = os.path.join(output_directory, output_file_name)

        # Measure solving time
        start_time = time.time()

        # Call the SolveFromInput function from the DLL
        mydll.SolveFromInput(input_file_path, output_file_path)

        end_time = time.time()
        solving_time = end_time - start_time

        print(f"Solved {input_file_path} in {solving_time:.2f} seconds and saved as {output_file_path}")  # Print a message including solving time
    except OSError as e:
        print(f"Error solving {input_file_path}: {e}")


def main():
    input_directory = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\dumped_saphsolve_actual_models"
    output_directory = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\output_dumped_saphsolve_actual_models"

    # List all JSON files in the input directory
    json_files = [file for file in os.listdir(input_directory) if file.endswith('.JSInp')]

    # Ensure the output directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Solve each JSON file
    for file_name in json_files:
        input_file_path = os.path.join(input_directory, file_name)

        # Solve the JSON file
        solve_json_file(input_file_path, output_directory)


if __name__ == "__main__":
    main()
