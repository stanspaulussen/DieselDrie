"""
depth_first_3.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffmann and Stans Paulussen

This file contains the depth first algorithm. This algorithm chooses the first station
of a track which has the least amount of connections. After that, it explores all possible
configurations of the track and adds the best one to the grid.
"""

import copy
from code.classes.track import Track

class Depth_first:
    """
    Depth first algorithm that chooses first station of a track which has the least amount of connections.
    """
    def __init__(self, grid, data, track_amount):
        self.grid = copy.deepcopy(grid)
        self.data = data 
        self.stations = self.grid.stations
        self.track_amount = track_amount
        self.best_score = 0
        self.station_dict = self.make_station_dict()

    def run(self):
        """
        Runs the algorithm.
        """
        station_list = self.create_station_list()

        # runs the amount of tracks the user wants
        for i in range(self.track_amount):
            print(f"started track {i}\n")
            new_grid = copy.deepcopy(self.grid)

            # chooses starting station and creates new track
            track = self.create_new_track(station_list, i, new_grid)

            # explores all possible configurations of track and adds the best one to the grid
            self.visit_all_possibilities(self.first_station, track, new_grid)

    def create_new_track(self, station_list, i, new_grid):
        """
        Chooses starting station based on the least amount of connections and adds it to a new track.
        """
        self.first_station = self.stations[station_list.pop(0)]
        track = Track(f"depthfirst_{i}", new_grid)
        track.add_station(new_grid, self.first_station.name)

        return track
    
    def make_station_dict(self):
        """
        Makes dictionary of the station and their amount of connections.
        """
        self.station_dict = {}

        # interates over stations and puts the amount of connections in the dict
        for station in self.stations:
            length = len(self.stations[station].connections)
            self.station_dict[station] = length
        
        return self.station_dict
                
    def create_station_list(self):
        """
        Sorts the station dict based on the amount of connections (value). 
        """
        sorted_station_list = sorted(self.station_dict, key=self.station_dict.get)

        return sorted_station_list

    def visit_all_possibilities(self, first_station, track, grid):
        """
        Tries all possible configurations starting at the first station and only adds the configuration with the best score.
        """
        # loops over connections of station
        for connection in first_station.connections:
            # keeps adding untill the max length of a track is reached
            if track.add_station(grid, self.stations[connection].name):
                # calculates the quality of adding the station and remembers it if it is the best score yet
                if grid.get_quality() > self.best_score:
                    self.best_score = grid.get_quality()
                    self.grid = copy.deepcopy(grid)
                    print(f"new best score: {self.best_score}:\n{self.grid}\n\n")

                # repeat untill there are no more configurations left
                self.visit_all_possibilities(self.stations[connection], track, grid)
                track.remove_last_station()
        