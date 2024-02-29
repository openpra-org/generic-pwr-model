""""``main.py`` is a Python script that demonstrates how to call the SolveFromInput function from the SolverSaphire.dll"""

from ctypes import *

try:
    # Load the DLL
    mydll = cdll.LoadLibrary("C:\\Users\\egeme\\Saphire 8\\tools\\SolverSaphire.dll")
except OSError as e:
    print("Error:", e)
    exit(1)  # Exit the script if DLL loading fails

try:
    # Call the SolveFromInput function from the DLL
    JSInp_file_path = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\saphsolve_actual_models\EQK-BIN1_et_Grp-1_24-02-26_15-57-10.JSInp"
    JSCut_file_path = r"C:\Users\egeme\Desktop\repo\Gitlab\Enhancement-of-PRA-Tools\Model-Exchange\model-converter\saphsolve_actual_models\EQK-BIN1_et_Grp-1_24-02-26_15-57-10.JSCut"
    mydll.SolveFromInput(JSInp_file_path, JSCut_file_path)
    print("Done")  # Print a message indicating successful completion
except OSError as e:
    print("Error:", e)
    exit(2)  # Exit the script if SolveFromInput fails

# from ctypes import*
# # give location of dll
# mydll = cdll.LoadLibrary("C:\\Users\\egeme\\Saphire 8\\tools\\SolverSaphire.dll")
# mydll.SolveFromInput("C:\\Users\\egeme\\Downloads\\LLOCA.JSInp", "C:\\Users\\egeme\\Downloads\\LLOCA.JSCut")
# print("Done2")