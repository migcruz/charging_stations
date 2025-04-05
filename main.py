import json
import sys
from station_chargers import Station, Charger

stations_dict = {}  # Dictionary to store station objects
chargers_dict = {}  # Dictionary to store charger objects

charger_reports = []  # List to store charger availability reports
charger_reports_dict = {}

def process_charger_availailbity_reports(charger_report):

    status = 0

    parts = charger_report.split()  # Splits by spaces

    # Assigning parts to variables
    try:
        charger_id = int(parts[0])
    except ValueError:
        print("ERROR")
        return 1

    try:
        start_time = int(parts[1])
    except ValueError:
        print("ERROR")
        return 1
    
    try:
        end_time = int(parts[2])
    except ValueError:
        print("ERROR")
        return 1
    
    try:
        available = json.loads(parts[3].lower()) 
    except json.JSONDecodeError:
        print("ERROR")
        return 1

    charger_obj = chargers_dict[charger_id]

    # update start and end times for both the station object and the charger object
    if charger_obj.start_time is None or start_time < charger_obj.start_time:
        charger_obj.start_time = start_time

    if charger_obj.station.start_time is None or start_time < charger_obj.station.start_time:
        charger_obj.station.start_time = start_time
        
    if end_time > charger_obj.end_time:
        charger_obj.end_time = end_time
    
    if end_time > charger_obj.station.end_time:
        charger_obj.station.end_time = end_time

    # calculate availability
    if available:
        interval_list = []
        interval = (start_time, end_time)
        charger_obj.availability_intervals.append(interval)

        interval_list.append(interval)
        charger_obj.station.calc_uptime(interval_list) # update the station uptime each time one of its chargers data is processed.
    
    return status

def parse_file(file_path):

    status = 0

    with open(file_path, "r") as file:
        section = None

        for line in file:
            line = line.strip()

            if not line:  # Skip empty lines
                continue

            if line == "[Stations]":
                section = "stations"
                continue
            elif line == "[Charger Availability Reports]":
                section = "chargers"
                continue
            
            if section == "stations":
                parts = line.split()
                station_id = int(parts[0])
                station_obj = Station(station_id)

                station_chargers = list(map(int, parts[1:]))  # Convert numbers to int

                for charger_id in station_chargers:
                    charger_obj = Charger(charger_id, station=station_obj)
                    station_obj.add_charger(charger_id, charger=charger_obj)
                    chargers_dict[charger_id] = charger_obj

                stations_dict[station_id] = station_obj
                
            elif section == "chargers":
                charger_reports.append(line)  # Store full report as a string

    # If any of the data structures are empty, error out
    if not charger_reports or not stations_dict or not chargers_dict:
        print("ERROR")
        return 1

    for report in charger_reports:
        status = process_charger_availailbity_reports(report)
        if status:
            return status

    # Print to stdout
    for station_id, station_obj in stations_dict.items():
        print(station_id, station_obj.uptime)
    
    # Dev debug
    # for charger_id, charger_obj in chargers_dict.items():
    #     print("Chargers", charger_obj)

    # for station_id, station_obj in stations_dict.items():
    #     print("Stations", station_obj)

    return status

def main():
    """Main function to run the script."""

    status = 0
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    status = parse_file(file_path)

    sys.exit(status)

if __name__ == "__main__":
    main()
