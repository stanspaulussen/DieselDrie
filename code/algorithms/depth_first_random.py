"""
depth_first_random.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file contains the depth first algorithm, but choosing a random starting station. 
"""

import copy
import random
from code.classes.track import Track
from code.classes.grid import Grid 
from code.algorithms.depth_first import Depth_first

class Depth_first_random(Depth_first):

    def create_new_track(self, station_list, i, new_grid):
        """
        Chooses a random starting station for each track.
        """

        stations = list(self.grid.stations.values())

        # choose random first station
        self.first_station = random.choice(stations)

        # create track
        track = Track(f"depthfirst_{i}", new_grid)

        # add random starting station to the track
        track.add_station(new_grid, self.first_station.name)

        return track