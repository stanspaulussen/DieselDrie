from .station import Station
import csv

class Grid():
    """
    contains all stations, connections and tracks
    """
    def __init__(self, sourcefile_stations, sourcefile_connections):
        self.stations = self.load_stations(sourcefile_stations)
        self.connections = self.load_connections(sourcefile_connections)
        self.tracks = {}

    def load_stations(self, sourcefile):
        """
        load all stations from the input file
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
        search for a station object and return it
        """
        # get all stations in list
        stations = self.stations.values()
        
        # search list for correct station
        for station in stations:
            if station.name == station_name:
                return station

    def load_connections(self, sourcefile):
        """
        load all connections between stations from the sourcefile
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
        add a new track to the grid
        """
        # add a track to the track dictionary
        self.tracks[track.track_name] = track
    
    def get_quality(self):
        """
        calculate the quality of the current grid
        """
        # print("quality:")
        
        # amount of tracks
        t = len(self.tracks)
        # print(f"t: {t}")

        # total time
        time = 0
        for track in list(self.tracks.values()):
            time += track.length
        # print(f"time: {time}")

        # fraction used connections
        connection_list = list(self.connections.values())
        connected = 0
        allready_visited = []
        
        # iterate over each track
        for track in self.tracks.values():
            # iterate over each connection
            for connection in connection_list:
                # check if connection is used in track
                if track.get_connection(connection) and connection not in allready_visited:
                    connected += 1
                    # add track to allready_visited to not check again
                    allready_visited.append(connection)
        
        # calculate fraction
        p = connected/len(self.connections)
        # print(f"p: {p}")

        # calculate quality
        k = p*10000 - (t*100 + time)
        # print(f"k: {k}")

        return k

    def __repr__(self):
        return f"{self.stations.values()}:: {self.tracks.values()}"
