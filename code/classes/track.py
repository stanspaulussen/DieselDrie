from .grid import Grid
from .station import Station

class Track():
    """
    defines a track containing stations and conections and a total length
    """
    def __init__(self, track_name, grid):
        self.track_name = track_name
        self.stations = {}
        self.connections = {}
        self.length = 0

        # adds itself to the grid
        grid.add_track(self)

        if grid.data == 1:
            self.max_length = 121
        else:
            self.max_length = 181

    def add_station(self, grid, station_name):
        """
        add a new station to the track
        it must be connected to the previous stations
        """
        # get the station object
        station = grid.get_station(station_name)

        # check if the stations dictionary is empty
        if self.stations == {}:
            self.stations[0] = station
            
            return True
        else:
            # get last station object
            station_list = list(self.stations.values())
            last_station = station_list[-1]

            # get connections of last station
            connections = last_station.get_connections()

            # check if connections contains the station to add
            for connection in connections:
                # make sure total length does not exceed max
                if station == connection[0] and self.length + int(connection[1]) < self.max_length:
                    # add station to track
                    self.stations[len(self.stations)] = station

                    # add connection length to total length
                    self.length = self.length + int(connection[1])

                    # add connection to connections
                    self.connections[len(self.stations) - 2] = [last_station, station]

                    return True
            
            # no connection found
            return False
 
    def get_stations(self):
        """
        return all stations of this track
        """
        return self.stations.values()

    def get_connection(self, connection):
        """
        check if this track contains a certain connection
        """
        # check for one way
        if connection in self.connections.values():
            return True
        # check for the other way around
        elif [connection[1], connection[0]] in self.connections.values():
            return True
        return False
    
    def remove_last_station(self):
        """
        remove the last station that was added to this track
        """
        # remove station
        removed_station = self.stations.popitem()

        # remove length
        l = removed_station[1].connections[list(self.stations.values())[-1].station_id]
        self.length -= l[1]

        # remove connection
        self.connections.popitem
    
    def __repr__(self):
        return f"{self.track_name}: {self.stations}"
