from .grid import Grid 

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
                # station heeft connectie met vorige station
                if station == connection[0]:
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
    
    def __repr__(self):
        return f"{self.track_name}: {self.stations}"
