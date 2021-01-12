from .grid import Grid
from .station import Station

MAX_LENGTH = 121

class Track():
    def __init__(self, track_name, grid):
        self.track_name = track_name
        self.stations = {}
        self.connections = {}
        self.length = 0

        grid.add_track(self)

    def add_station(self, grid, station_name):
        station = grid.get_station(station_name)
        # check of er al stations zijn toegevoegd aan de track
        if self.stations == {}:
            self.stations[0] = station
            return True
        else:
            # pak last station object
            station_list = list(self.stations.values())
            last_station = station_list[-1]
            # pak connections van last station
            connections = last_station.get_connections()
            # check of huidig station daarbij zit
            for connection in connections:
                # station heeft connectie met vorige station en lengte niet te hoog
                if station == connection[0] and self.length + int(connection[1]) < MAX_LENGTH:
                    # voeg station toe aan track
                    self.stations[len(self.stations)] = station
                    # voeg lengte verbinding toe aan totale lengte track
                    self.length = self.length + int(connection[1])
                    # voeg connectie toe aan connections
                    self.connections[len(self.stations) - 2] = [last_station, station]

                    return True
            
            # geen connectie gevonden
            return False
 
    def get_stations(self):
        return self.stations.values()

    def get_connection(self, connection):
        if connection in self.connections.values():
            return True
        elif [connection[1], connection[0]] in self.connections.values():
            return True
        return False
    
    def remove_last_station(self):
        # remove station
        removed_station = self.stations.popitem()

        # remove length
        l = removed_station[1].connections[list(self.stations.values())[-1].station_id]
        self.length -= l[1]

        # remove connection
        self.connections.popitem
    
    def __repr__(self):
        return f"{self.track_name}: {self.stations}"
