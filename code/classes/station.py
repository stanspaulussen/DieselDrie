"""
station.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file contains the database of each station. 
"""

class Station():
    """
    Contains a station with coordinates and connections.
    """
    def __init__(self, name, station_id, x_coord, y_coord):
        self.name = name
        self.station_id = station_id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.connections = {}

    def add_connection(self, station, length):
        """
        Add a connection to the station.
        """
        self.connections[station.station_id] = [station, length]

    def get_connections(self):
        """
        Return a list of all connected station objects.
        """
        return list(self.connections.values())

    def __repr__(self):
        return f"{self.name}"