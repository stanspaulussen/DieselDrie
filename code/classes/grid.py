from .station import Station
import csv

class Grid():
    def __init__(self, sourcefile_stations, sourcefile_connections):
        self.stations = self.load_stations(sourcefile_stations)
        self.load_connections(sourcefile_connections)
        self.tracks = {}

    def load_stations(self, sourcefile):
        #comment
        stations = {}
        with open(sourcefile, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['id']] = Station(row['station'], row['id'], row['x'], row['y'])
            
        return stations

    def get_station(self, station_name):
        stations = self.stations.values()
        for station in stations:
            if station.name == station_name:
                return station

    def load_connections(self, sourcefile):
        with open(sourcefile) as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                # print(row)
                # row = row.split(',')
                station_a = self.get_station(row['station1'])
                station_b = self.get_station(row['station2'])
                length = int(row['distance'])

                station_a.add_connection(station_b, length)
                station_b.add_connection(station_a, length)