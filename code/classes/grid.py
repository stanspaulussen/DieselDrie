"""
grid.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file loads the data and contains the database for the combined tracks that form a train system.
"""

from .station import Station
import csv

class Grid():
    """
    Contains all stations, connections and tracks.
    """
    def __init__(self, data, load=True):

        self.data = data
        self.tracks = {}

        # loads different data depending on which map is chosen
        if load == True:
            if self.data == 1: 
                sourcefile_stations = "data/StationsHolland.csv"
                sourcefile_connections = "data/ConnectiesHolland.csv"
            else: 
                sourcefile_stations = "data/StationsNationaal.csv"
                sourcefile_connections = "data/ConnectiesNationaal.csv"

            self.stations = self.load_stations(sourcefile_stations)
            self.connections = self.load_connections(sourcefile_connections)
        else:
            self.stations = None
            self.connections = None

    def copy(self):
        """
        Copies grid.
        """

        new = Grid(None, load=False)

        new.stations = self.stations
        new.connections = self.connections

        return new

    def load_stations(self, sourcefile):
        """
        Load all stations from the input file.
        """
        # create empty dict for stations
        stations = {}

        # open sourcefile
        with open(sourcefile, 'r') as in_file:
            reader = csv.DictReader(in_file)

            # add station from each row
            for row in reader:
                stations[row['id']] = Station(row['station'], row['id'], row['x'], row['y'])
            
        return stations

    def get_station(self, station_name):
        """
        Search for a station object and return it.
        """
        # get all stations in list
        stations = self.stations.values()
        
        # search list for correct station
        for station in stations:
            if station.name == station_name:
                return station

    def load_connections(self, sourcefile):
        """
        Load all connections between stations from the sourcefile.
        """
        # create empty dict for connections
        connections = {}

        # open sourcefile
        with open(sourcefile) as in_file:
            reader = csv.DictReader(in_file)
            
            # integer for connection keys
            i = 0

            for row in reader:
                # get two stations end connection length
                station_a = self.get_station(row['station1'])
                station_b = self.get_station(row['station2'])
                length = int(row['distance'])

                # create connection in both station objects
                station_a.add_connection(station_b, length)
                station_b.add_connection(station_a, length)

                # add connection to dict
                connections[i] = [station_a, station_b]

                i += 1
        
        return connections
    
    def add_track(self, track):
        """
        Add a new track to the grid.
        """
        # add a track to the track dictionary
        self.tracks[track.track_name] = track
    
    def get_time(self):
        """
        Times the algorithm.
        """
        time = 0
        for track in list(self.tracks.values()):
            time += track.length

        return time

    def get_connected(self):
        """
        Keeps track of visited connections.
        """
        connected = 0
        visited_set = set()
        
        # iterate over each track
        for track in self.tracks.values():
            # iterate over each connection
            for connection in track.connections.values():
                con1 = f"{connection[0]}, {connection[1]}"
                con2 = f"{connection[1]}, {connection[0]}"
                # adds one if an unridden connection is now ridden
                if con1 not in visited_set and con2 not in visited_set:
                    visited_set.add(con1)
                    connected += 1

        return connected
    
    def get_quality(self):
        """
        Calculate the quality of the current grid.
        """
        # amount of tracks
        t = len(self.tracks)

        # amount of minutes travelled in all tracks combined.
        time = self.get_time()

        # calculate fraction ridden connections
        p = self.get_connected()/len(self.connections)

        # calculate quality
        k = p * 10000 - (t * 100 + time)

        return k

    def __repr__(self):
        return f"{self.tracks.values()}"