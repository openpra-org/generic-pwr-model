# Generic PWR SPAR Model

This repository includes generic PWR v1.2 model in various formats.

Since 1995, Idaho National Laboratory (INL) has developed Standardized Plant Analysis Risk (SPAR) models for the United States (US) Nuclear Regulatory Commission (NRC) to provide critical risk-informed input to the regulatory process.

At present, the model considers various initiating events, including seismic activity, internal flooding, internal fires, hurricanes, high winds, ISLOCA (Interfacing Systems LOCA), upset conditions leading to transients, large break LOCA, loss of CCW (Component Cooling Water), loss of DC bus, loss of feedwater, loss of offsite power, large steam line breaks, medium break LOCA, steam generator tube ruptures, small LOCA, tornadoes, and excessive LOCA.
`v1.0` of the model includes 56 event trees linked with 140 fault trees.


## Additional Documentation

- E. M. Aras, A. S. Amin Aly Farag, S. T. Wood, and J. T. Boyce, “Refining Processing Engines from SAPHIRE: Initialization of Fault Tree/Event Tree Solver,” Idaho National Laboratory (INL), Idaho Falls, ID (United States), INL/RPT-23-75066-Rev000, Oct. 2023. doi: 10.2172/2203095.
- C. Smith, “Generic Pressurized Water Reactor Model for SAPHIRE,” INL/EXT-21-62553-Rev000, 1804754, Apr. 2021. doi: 10.2172/1804754.
- S. Wood, J. Boyce, E. Aras, A. Farag, and M. Diaconeasa, “Advancing SAPHIRE: Transitioning from Legacy to State-of-Art Excellence,” in Advanced Reactor Safety (ARS), Las Vegas, NV: American Nuclear Society, 2024, pp. 532–541. doi: 10.13182/T130-43357.
- E. Aras, S. Wood, J. Boyce, A. Farag, and M. Diaconeasa, “Enhancing the SAPHIRE Solve Engine: Initial Progress and Efforts,” in Advanced Reactor Safety (ARS), Las Vegas, NV: American Nuclear Society, 2024, pp. 542–551. doi: 10.13182/T130-43361.
- E. M. Aras, “Enhancement Methodology for Probabilistic Risk Assessment Tools through Diagnostics, Optimization, and Parallel Computing,” Doctor of Philosophy, North Carolina State University, Raleigh, North Carolina, 2024. [Online]. Available: https://repository.lib.ncsu.edu/items/bb05f7f5-1cff-4beb-9312-331bc94b0b95
- A. Farag, S. Wood, A. Earthperson, E. Aras, J. Boyce, and M. Diaconeasa, “Evaluating PRA Tools for Accurate and Efficient Quantifications: A Follow-Up Benchmarking Study Including FTREX,” in Advanced Reactor Safety (ARS), Las Vegas, NV: American Nuclear Society, 2024, pp. 573–582. doi: 10.13182/T130-43377.
- E. M. Aras, S. T. Wood, A. S. A. A. Farag, and J. T. Boyce, “Diagnostics and Strategic Plan for Advancing the SAPHIRE Engine,” Idaho National Laboratory, Idaho Falls, ID, INL/COM-23-74428, Aug. 2023. [Online]. Available: https://inldigitallibrary.inl.gov/sites/sti/sti/Sort_67446.pdf
- M. Hamza, A. Tezbasaran, E. Aras, A. S. Farag, and M. A. Diaconeasa, “Model Exchange Methodology Between Probabilistic Risk Assessment Tools: SAPHIRE and CAFTA Case Study,” in 18th International Probabilistic Safety Assessment and Analysis (PSA 2023), Knoxville, TN: American Nuclear Society, 2023, pp. 150–158.

## About

| #   | Input Model      | Description                                                                 | # MCS     | Probability | Seq. |
|-----|------------------|-----------------------------------------------------------------------------|-----------|-------------|------|
| 1   | EQK-BIN1         | SEISMIC EVENT IN BIN 1 (0.1 - 0.3g) OCCURS (BIN PGA 0.17)                   | 610,016   | 2.085E-09   | 85   |
| 2   | EQK-BIN2         | SEISMIC EVENT IN BIN 2 (0.3 - 0.5g) OCCURS (BIN PGA 0.39)                   | 811,575   | 2.430E-07   | 85   |
| 3   | EQK-BIN3         | SEISMIC EVENT IN BIN 3 (0.5 - 0.75g) OCCURS (BIN PGA 0.61)                  | 802,392   | 2.336E-06   | 85   |
| 4   | EQK-BIN4         | SEISMIC EVENT IN BIN 4 (0.75 - 1.0g) OCCURS (BIN PGA 0.87)                  | 598,505   | 2.857E-06   | 85   |
| 5   | EQK-BIN5         | SEISMIC EVENT IN BIN 5 (1.0 - 1.5g) OCCURS (BIN PGA 1.22)                   | 440,041   | 2.348E-06   | 85   |
| 6   | EQK-BIN6         | SEISMIC EVENT IN BIN 6 (1.5 - 3.0g) OCCURS (BIN PGA 2.12)                   | 177,330   | 6.006E-07   | 85   |
| 7   | EQK-BIN7         | SEISMIC EVENT BIN 7 (> 3.0g) OCCURS                                         | 2         | 9.623E-09   | 1    |
| 8   | FLI-4160VACA     | IF - 4160V AC ROOM A                                                        | 363,408   | 2.551E-09   | 29   |
| 9   | FLI-4160VACB     | IF - 4160V AC ROOM B                                                        | 364,430   | 2.563E-09   | 29   |
| 10  | FLI-AFW-ROOM     | IF - AFW PUMP ROOMS                                                         | 126,120   | 2.109E-08   | 29   |
| 11  | FLI-CCW-ROOM     | IF - CCW PUMP ROOMS                                                         | 283,639   | 2.941E-08   | 29   |
| 12  | FLI-CCW-ROOMA    | IF - CCW PUMP ROOM A                                                        | 631,309   | 1.065E-09   | 29   |
| 13  | FLI-CCW-ROOMB    | IF - CCW PUMP ROOM B                                                        | 636,421   | 1.066E-09   | 29   |
| 14  | FLI-CVC-ROOM     | IF - CVC PUMP ROOM                                                          | 277,526   | 3.958E-10   | 29   |
| 15  | FLI-RHR-ROOM     | IF - RHR PUMP ROOM                                                          | 36,008    | 1.071E-10   | 29   |
| 16  | FLI-SWS-ROOM     | IF - SWS PUMP ROOMS                                                         | 190,025   | 2.997E-07   | 29   |
| 17  | FLI-SWS-ROOMA    | IF - SWS PUMP ROOM A                                                        | 182,124   | 1.402E-08   | 29   |
| 18  | FLI-SWS-ROOMB    | IF - SWS PUMP ROOM B                                                        | 188,786   | 1.409E-08   | 29   |
| 19  | FRI-AB-AFWAB     | FIRE IN AUXILIARY BUILDING CAUSING FAILURE AFW MDP A AND B                  | 420,246   | 1.243E-08   | 29   |
| 20  | FRI-AB-CCWBC     | FIRE IN AUXILIARY BUILDING CAUSING FAILURE CCW TRAINS A&C                   | 528,190   | 7.673E-10   | 29   |
| 21  | FRI-AB-LOOP      | FIRE IN AUX BUILDING CAUSES LOOP                                            | 29,283    | 1.098E-08   | 33   |
| 22  | FRI-AB-LOOP-DIVA | FIRE IN AUX BUILDING CAUSES LOOP AND LOSS OF DIV A AC                       | 45,325    | 3.138E-06   | 33   |
| 23  | FRI-AB-LOOP-DIVB | FIRE IN AUX BUILDING CAUSES LOOP AND LOSS OF DIV B AC                       | 46,090    | 3.159E-06   | 33   |
| 24  | FRI-AB-RHRA      | FIRE IN AUXILIARY BUILDING CAUSING FAILURE RHR TRAIN A                      | 647,063   | 2.114E-09   | 29   |
| 25  | FRI-AB-SIS       | FIRE IN AUXILIARY BUILDING CAUSING FAILURE SIS TRAINS                       | 659,428   | 5.416E-08   | 29   |
| 26  | FRI-AB-SLOCA     | FIRE IN AUXILIARY BUILDING CAUSES SPURIOUS PORV OPENING                     | 14,257    | 5.499E-07   | 8    |
| 27  | FRI-MCR          | FIRE IN MAIN CONTROL ROOM CAUSES AN EVACUATION                              | 3,464     | 9.081E-06   | 6    |
| 28  | FRI-SWS-BLD      | FIRE IN SERVICE WATER BUILDING FAILING SWS                                  | 71,923    | 9.331E-08   | 29   |
| 29  | HCN-BIN1         | HURRICANE WIND EVENT BIN 1 (111 MPH - 135 MPH)                              | 1,703,431 | 4.868E-09   | 63   |
| 30  | HCN-BIN2         | HURRICANE WIND EVENT BIN 2 (136 MPH - 165 MPH)                              | 1,064,448 | 2.181E-09   | 63   |
| 31  | HCN-BIN3         | HURRICANE WIND EVENT BIN 3 (166 MPH - 200 MPH)                              | 475,235   | 9.346E-10   | 63   |
| 32  | HCN-BIN4         | HURRICANE WIND EVENT BIN 4 (> 200 MPH)                                      | 230,212   | 4.737E-10   | 63   |
| 33  | HWD-96MPH        | HIGH WIND (<110 MPH) EVENT OCCURS                                           | 2,558,791 | 2.264E-08   | 63   |
| 34  | ISL-RHR-CL       | ISLOCA RHR COLD LEG                                                         | 217       | 3.063E-11   | 2    |
| 35  | ISL-RHR-HL       | ISLOCA RHR HOT LEG                                                          | 3         | 2.063E-08   | 2    |
| 36  | L4160ACA         | LOSS OF 4160 VAC BUS A                                                      | 160,390   | 2.207E-07   | 29   |
| 37  | L4160ACB         | LOSS OF 4160 VAC BUS B                                                      | 162,204   | 2.220E-07   | 29   |
| 38  | LLOCA            | LARGE BREAK LOCA                                                            | 20,119    | 3.617E-07   | 3    |
| 39  | LOCCW            | TOTAL LOSS OF CCW                                                           | 778,360   | 8.245E-08   | 29   |
| 40  | LODCA            | LOSS OF 125 VDC BUS A                                                       | 156,714   | 4.249E-08   | 29   |
| 41  | LODCB            | LOSS OF 125 VDC BUS B                                                       | 160,549   | 4.271E-08   | 29   |
| 42  | LOMFW            | LOSS OF MAIN FEEDWATER                                                       | 1,550,153 | 7.502E-08   | 18   |
| 43  | LOOPGR           | LOSS OF OFFSITE POWER (GRID-RELATED)                                        | 1,111,725 | 7.913E-07   | 33   |
| 44  | LOOPPC           | LOSS OF OFFSITE POWER (PLANT-CENTERED)                                      | 851,575   | 7.619E-08   | 33   |
| 45  | LOOPSC           | LOSS OF OFFSITE POWER (SWITCHYARD-CENTERED)                                 | 1,253,736 | 7.286E-07   | 33   |
| 46  | LOOPWR           | LOSS OF OFFSITE POWER (WEATHER-RELATED)                                     | 1,014,915 | 5.660E-07   | 33   |
| 47  | LSSB             | LARGE STEAM LINE BREAK (UNISOLABLE INSIDE CONTAINMENT)                      | 216,762   | 1.872E-07   | 16   |
| 48  | MLOCA            | MEDIUM BREAK LOCA                                                           | 67,620    | 9.332E-06   | 5    |
| 49  | SGTR             | STEAM GENERATOR TUBE RUPTURE                                                | 1,039,329 | 2.668E-06   | 12   |
| 50  | SLOCA            | SMALL BREAK LOCA                                                            | 309,917   | 2.453E-05   | 8    |
| 51  | TOR-BIN1         | TORNADO EVENT BIN-1 (136- 165 MPH)                                          | 128,067   | 5.355E-12   | 63   |
| 52  | TOR-BIN2         | TORNADO EVENT BIN-2 (166- 200 MPH)                                          | 126,084   | 2.614E-11   | 63   |
| 53  | TOR-BIN3         | TORNADO EVENT BIN-3 (> 200 MPH)                                             | 95,064    | 1.296E-10   | 63   |
| 54  | TRANS            | TRANSIENT                                                                   | 4,178,502 | 1.525E-07   | 29   |
| 55  | XLOCA            | EXCESSIVE LOCA                                                              | 1         | 1.000E-07   | 1    |
|     | **TOTAL**        |                                                                             | 28,559,059|             | 1965 |

