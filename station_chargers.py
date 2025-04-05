class Charger:
    def __init__(self, charger_id, station=None):
        """Initialize a charger with its ID and an empty availability list."""
        self.charger_id = charger_id
        self.availability_intervals = []  # Stores (start_time, end_time) tuples
        self.station = station
        self.start_time = None
        self.end_time = -1

    def add_availability(self, start_time, end_time):
        """Add an availability interval for the charger."""
        self.availability_intervals.append((start_time, end_time))

    def __repr__(self):
        """Return a string representation of the charger."""
        return f"Charger({self.charger_id}, Availability: {self.availability_intervals}, Station: {self.station.station_id})"

class Station:
    def __init__(self, station_id, chargers=None):
        """Initialize a station with an ID and an optional list of chargers."""
        self.station_id = station_id
        self.chargers = chargers if chargers is not None else {}  # Default to an empty list
        self.start_time = None
        self.end_time = -1
        self.uptime_intervals = []  # Stores (start_time, end_time) tuples where at least 1 charger in the station in up
        self.uptime = 0

    def add_charger(self, charger_id, charger=None):
        """Add a charger to the station."""
        self.chargers[charger_id] = charger
    
    def get_charger(self, charger_id):
        return self.chargers[charger_id]
    
    def calc_uptime(self, intervals):
        new_interval_list = intervals + self.uptime_intervals # merge both lists into new list

        new_interval_list.sort(key=lambda x: x[0])  # Sort by start time
        merged = [new_interval_list[0]]

        for start, end in new_interval_list[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end:  # Overlapping case
                merged[-1] = (last_start, max(last_end, end))  # Merge intervals
            else:
                merged.append((start, end))  # Non-overlapping, add new interval

        self.uptime_intervals = merged

        # calculate total uptime
        total_uptime = sum(end - start for start, end in self.uptime_intervals)
        self.uptime = int ((total_uptime / (self.end_time - self.start_time)) * 100)

    def __repr__(self):
        """Return a string representation of the station."""
        return f"Station({self.station_id}, Chargers: {self.chargers}, Start: {self.start_time}, End: {self.end_time}, Uptime_intervals: {self.uptime_intervals}, Uptime: {self.uptime})"
