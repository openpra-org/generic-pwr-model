"""
The script uses the ctypes library to load the DLL and call the SolveFromInput function from the DLL.
It uses the threading library to solve the JSON files in parallel using multiple threads.
"""
import os
import threading
from ctypes import *
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

        print(
            f"Solved {input_file_path} in {solving_time:.2f} seconds and saved as {output_file_path}")  # Print a message including solving time
    except OSError as e:
        print(f"Error solving {input_file_path}: {e}")


def solve_files_in_thread(files, input_directory, output_directory):
    for file_name in files:
        input_file_path = os.path.join(input_directory, file_name)

        # Solve the JSON file
        solve_json_file(input_file_path, output_directory)


def main():
    input_directory = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\dumped_saphsolve_actual_models"
    output_directory = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\output_dumped_saphsolve_actual_models"

    # List all JSON files in the input directory
    json_files = [file for file in os.listdir(input_directory) if file.endswith('.JSInp')]

    # Ensure the output directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # # Measure serial solution time
    serial_start_time = time.time()

    # Solve each JSON file serially
    for file_name in json_files:
        input_file_path = os.path.join(input_directory, file_name)

        # Solve the JSON file
        solve_json_file(input_file_path, output_directory)

    serial_end_time = time.time()
    serial_solution_time = serial_end_time - serial_start_time

    # Print the serial solution time
    print(f"Serial solution time: {serial_solution_time:.2f} seconds")

    # Measure parallel solution time
    parallel_start_time = time.time()

    # Determine the number of threads based on the number of CPU cores
    num_threads = os.cpu_count() or 1  # If the number of CPU cores cannot be determined, default to 1

    # Split the JSON files into chunks for each thread
    chunks = [json_files[i::num_threads] for i in range(num_threads)]

    # Create and start threads
    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=solve_files_in_thread, args=(chunk, input_directory, output_directory))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    parallel_end_time = time.time()
    parallel_solution_time = parallel_end_time - parallel_start_time

    # Print the parallel solution time
    print(f"Parallel solution time: {parallel_solution_time:.2f} seconds")


if __name__ == "__main__":
    main()
