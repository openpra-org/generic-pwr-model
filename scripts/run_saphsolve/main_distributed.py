"""
NOTE: NOT tested yet!
IMPORTANT: This script is intended to be run using the MPI4Py library and the DLL provided by Saphire 8.
This script demonstrates how to use MPI to distribute the solving of multiple JSON files to multiple processes.
The script uses the MPI4Py library to distribute the files to multiple processes and solve them in parallel.
The script uses the ctypes library to load the DLL and call the SolveFromInput function from the DLL.

"""

import os
import time
from mpi4py import MPI
from ctypes import *

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

try:
    # Load the DLL - ensure the DLL is accessible on all nodes if necessary
    mydll = cdll.LoadLibrary(r"C:\Users\egeme\Saphire 8\tools\SolverSaphire.dll")
except OSError as e:
    if rank == 0:  # Only the master node prints the error
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
        mydll.SolveFromInput(input_file_path.encode('utf-8'), output_file_path.encode('utf-8'))

        end_time = time.time()
        solving_time = end_time - start_time

        print(f"Solved {input_file_path} in {solving_time:.2f} seconds and saved as {output_file_path}")
    except OSError as e:
        print(f"Error solving {input_file_path}: {e}")


def distribute_and_solve_files(files, input_directory, output_directory):
    # Scatter files to each process
    files_per_process = comm.scatter(files, root=0)

    # Each process works on its portion of files
    for file_name in files_per_process:
        input_file_path = os.path.join(input_directory, file_name)
        solve_json_file(input_file_path, output_directory)


if __name__ == "__main__":
    input_directory = None
    output_directory = None
    json_files = None

    if rank == 0:
        input_directory ="..\.\saphsolve_actual_models"
        output_directory = "..\.\model-converter\output_saphsolve_actual_models"

        # Ensure the output directory exists; if not, create it
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # List all JSON files in the input directory
        json_files = [file for file in os.listdir(input_directory) if file.endswith('.JSInp')]

        # Divide the list of files among the available MPI processes
        files_chunked = [json_files[i::size] for i in range(size)]
    else:
        files_chunked = None

    # Scatter the file chunks to all processes
    files_chunked = comm.scatter(files_chunked, root=0)

    # Measure start time
    start_time = MPI.Wtime()

    # Each process solves its assigned files
    distribute_and_solve_files(files_chunked, input_directory, output_directory)

    # Synchronize all processes
    comm.Barrier()

    # Measure end time
    end_time = MPI.Wtime()
    if rank == 0:
        print(f"Total distributed solution time: {end_time - start_time:.2f} seconds")
