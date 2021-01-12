class Station():
    """
    contains a single station with coordinates and connections
    """
    def __init__(self, name, station_id, x_coord, y_coord):
        self.name = name
        self.station_id = station_id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.connections = {}

    def add_connection(self, station, length):
        """
        add a connection to this station
        """
        self.connections[station.station_id] = [station, length]

    def get_connections(self):
        """
        return a list of all conected station objects
        """
        return list(self.connections.values())

    def __repr__(self):
        return f"{self.name}: {self.connections.keys()}"
