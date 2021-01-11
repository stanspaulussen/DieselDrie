from .grid import Grid 

class Track():
    def __init__(self, track_name, grid):
        self.track_name = track_name
        self.stations = {}
        self.length = 0

        grid.add_track(self)

    def add_station(self, grid, station_name):
       
        station = grid.get_station(station_name) 
        
        # self.stations[station.station_id] = station

        # check of er al stations zijn toegevoegd aan de track
        
        if self.stations == {}:
            self.stations[station.station_id] = station
            return True
        else:
            # pak last station object
            station_list = list(self.stations.values())
            last_station = station_list[-1]
            # pak connections van last station
            connections = last_station.get_connections()
            # check of huidig station daarbij zit
            print("hier komen de connecties van de last station")
            for connection in connections:
                
                print(connection[0])
                if station == connection[0]:
                    self.stations[station.station_id] = station
                    print(self.stations)
                    self.length = self.length + int(connection[1])
                    return True
            
            print("geen connectie")
            return False
 
    def get_stations(self):
        return self.stations.values()
    
    def __repr__(self):
        return f"{self.stations}"
