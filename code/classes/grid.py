from .station import Station
import csv

class Grid():
    def __init__(self, sourcefile_stations, sourcefile_connections):
        self.stations = self.load_stations(sourcefile_stations)
        self.connections = self.load_connections(sourcefile_connections)
        self.tracks = {}

    def load_stations(self, sourcefile):
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
        connections = 0
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

                connections += 1
        
        return connections
    
    def add_track(self, track):
        self.tracks[track.track_name] = track
    
    def get_quality(self):
        # aantal trajecten t
        t = len(self.tracks)
        print(t)

        # aantal minuten min
        time = 0
        for track in list(self.tracks.values()):
            time += track.length
            print(time)

        # fractie bereden verbindingen p
        station_tracker = []
        for track in list(self.tracks.values()):
            for station in list(track.stations.values()):
                if station not in station_tracker:
                    station_tracker.append(station)
        
        p = (len(station_tracker)-1)/self.connections
        print(p)

        k = p*10000 - (t*100 + time)
        print(k)

    def __repr__(self):
        return f"{self.stations.values()}:: {self.tracks.values()}"
    
    