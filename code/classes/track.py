from .grid import Grid 

class Track():
    def __init__(self, track_name):
        self.track_name = track_name
        self.stations = {}
        self.length = None

    def add_station(self, grid, station_name):
       
        station = grid.get_station(station_name) 
        
        self.stations[station.station_id] = station
 
    def get_stations(self):
        return self.stations.values()
    
    def __repr__(self):
        return f"{self.stations}"
