"""
greedy.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file contains the Greedy without lookahead algorithm, which picks the best first 
connection of a track and only adds the connection that leads to the best score.
"""

import copy 
from code.classes.track import Track

class Greedy():
    """
    For each track, chooses the best connection and keeps adding connections that lead to the best score.
    """
    def __init__(self, grid, data, track_amount):
        self.grid = copy.deepcopy(grid)
        self.data = data
        self.track_amount = track_amount
        self.best_score = 0
        self.best_connection = []
        self.track = Track(f"greedy_track_0", self.grid)
        self.count = 0
    
    def check_best_score(self, track, station, next_station):
        """
        Checks if connection generates new best quality score.
        """
        # calculate quality of grid with this connection 
        quality = self.grid.get_quality()

        self.track.remove_last_station()

        # if quality improves, add station to the track
        if quality > self.best_score:
            self.best_score = quality 
            self.best_connection = [station, next_station]

    def pick_first_connection(self):
        """
        Chooses first conenction of track with greatest quality.
        """
        stations = list(self.grid.stations.values())
        self.best_connection = []

        # add a first station to the track  
        for station in stations:

            self.track = Track(f"greedy_track_{self.count}", self.grid)
            self.track.add_station(self.grid, station.name)

            connections = station.connections

            # calculate quality of all connections and save the best connection
            for connection in connections: 

                next_station = stations[int(connection)].name
                self.track.add_station(self.grid, next_station)

                self.check_best_score(self.track, station, next_station)

        # if adding another track does not lead to a better quality, stop algorithm
        if self.best_connection == []:
            return False

        # add best connection to the track
        self.track = Track(f"greedy_track_{self.count}", self.grid)
        self.track.add_station(self.grid, self.best_connection[0].name)
        self.count += 1

        return self.best_connection[0].name

    def pick_next_station(self, station):
        """
        Chooses next station in track based on highest quality.
        """
        # all connections of the last added added station 
        connections = self.grid.get_station(self.best_connection[1]).connections

        for connection in connections.values():
            next_station = connection[0].name

            # if adding the connection exceeds the track's max time length 
            if self.track.add_station(self.grid, next_station) is False:
                break

            # calculate quality of connection 
            self.check_best_score(self.track, station, next_station)

    def run(self):
        """
        Generates a grid with a maximum of seven tracks composed of the most profitable connections.
        """
        for i in range(self.track_amount):
            # choose first connection 
            station = self.pick_first_connection()

            if station == False:
                return self.grid
            else:
                # make sure a track doesn't exceed its max length
                while self.track.add_station(self.grid, self.best_connection[1]):
                    # add connection to the track with greatest quality 
                    self.pick_next_station(station)
            
        print(self.grid)
        return self.grid 