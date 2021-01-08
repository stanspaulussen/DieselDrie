from .grid import Grid 

class Track():
    def __init__(self, track_id):
        self.track_id = track_id
        self.stations = {}
        self.length = None

    def add_station(self, station_name):
        grid = Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
        station = grid.get_station(station_name) 
        
        self.stations[station.station_id] = station
 
    def get_stations(self):
        pass
    
    def __repr__(self):
        return f"{self.stations}"
