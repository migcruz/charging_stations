# Charging Station Availability 

## Overview
This project processes charger availability reports and associates them with charging stations to compute station uptime. It reads input files containing station configurations and charger availability reports, validates data, and updates station uptime accordingly.

## Design Approach

### 1. Input file Parsing (`parse_file`)
- Reads station configurations and charger availability reports from a file.
- Splits data into station objects and charger objects. Stations have a one-to-many mapping to chargers.
- Creates instances of `Station` and `Charger`, storing them in hash tables.

### 2. Processing Reports (`process_charger_availailbity_reports`)
- Validates charger ID, start/end times, and availability flag.
- Updates the start and end times for both charger and station.
- Stores availability intervals for further analysis.
- Calls `calc_uptime()` to update the station’s uptime each time a charger report is processed. 
    - This is done by merging the current availability interval tuple list with the charger report's availability interval (if it was available). If there are overlapping availability intervals, then the overlapping time period is ignored.

## Complexity Analysis

### Time Complexity
| Function | Time Complexity | Explanation |
|----------|----------------|-------------|
| `parse_file` | O(N + M) | Iterates through station definitions (`N`) and charger reports (`M`). |
| `process_charger_availailbity_reports` | O(1) | Processes each report individually in constant time. |
| Overall Execution | O(N + M) | Linear time complexity since all elements are processed once. |

### Space Complexity
| Data Structure | Space Complexity | Explanation |
|---------------|------------------|-------------|
| `stations_dict` | O(N) | Stores `Station` objects for `N` stations. |
| `chargers_dict` | O(M) | Stores `Charger` objects for `M` chargers. |

## Testing
- Tests can easily be added by putting a new input file in ``/tests`` and adding a test case function in ``tests.py`` with the expected output.

## Key Features
- Efficient Parsing & Validation  
- Dictionary-based Storage (`stations_dict`, `chargers_dict`)  
- Automated Uptime Calculation (`calc_uptime()`)  

## Usage

### Running the app
```console
python main.py <file_path>
```
### Running tests
```console
python test_script.py
```

