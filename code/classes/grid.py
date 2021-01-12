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
        connections = {}
        with open(sourcefile) as in_file:
            reader = csv.DictReader(in_file)
            i = 0

            for row in reader:
                station_a = self.get_station(row['station1'])
                station_b = self.get_station(row['station2'])
                length = int(row['distance'])

                station_a.add_connection(station_b, length)
                station_b.add_connection(station_a, length)

                connections[i] = [station_a, station_b]
                i += 1
        
        print("connections:")
        print(connections)
        return connections
    
    def add_track(self, track):
        self.tracks[track.track_name] = track
    
    def get_quality(self):
        print("quality")
        
        # aantal trajecten t
        t = len(self.tracks)
        print(f"t: {t}")

        # aantal minuten min
        time = 0
        for track in list(self.tracks.values()):
            time += track.length
        print(f"time: {time}")

        # fractie bereden verbindingen p
        station_tracker = []
        for track in list(self.tracks.values()):
            for station in list(track.stations.values()):
                if station not in station_tracker:
                    station_tracker.append(station)
        
        p = (len(station_tracker)-1)/len(self.connections)
        print(f"p: {p}")

        k = p*10000 - (t*100 + time)
        print(f"k: {k}")

    def __repr__(self):
        return f"{self.stations.values()}:: {self.tracks.values()}"
    
    