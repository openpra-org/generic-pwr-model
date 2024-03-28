# Model-Converter
This repository is foundation for model conversion between SAPHSOLVE and OpenPSA MEF, specific
target is SCRAM.

## SAPHSOLVE Model Parsing


## OpenPSA MEF Model Parsing


## SAPHSOLVE Model Conversion to OpenPSA MEF
**SCRAM** accepts basic event and gate names as strings,
it does not accept only numbers even if the number are in string format like *"1"*.
So, some initials are added while converting the SAPHSOLVE model to SCRAM (OpenPSA MEF) model.

- **BE** for Basic Event
- **G** for Gate
- **S** for Sequence
- **INIT** for Initiating Event
- **FE** for Functional Event
- **FT** for Fault Tree
## OpenPSA MEF Model Conversion to SAPHSOLVE
