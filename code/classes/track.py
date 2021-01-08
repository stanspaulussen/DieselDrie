class Track():
    def __init__(self, track_id):
        self.track_id = track_id
        self.stations = {}
        self.length = None

    def add_station(self, station):
        self.stations[station.station_id] = station

    def get_stations(self):
        pass