"""
randomise.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file contains the randomise algorithm, which generates random tracks. 
The amount of tracks and the number of times the algorithm is run are determined 
by the user.
"""

import random
import copy
from code.classes.track import Track

MAX_TRACK_LENGTH = 24

class Random():
    """
    Generates random tracks.
    """
    def __init__(self, grid, loop_amount, track_amount, data):
        self.base_grid = grid
        self.loop_amount = loop_amount
        self.track_amount = track_amount
        self.data = data
        self.best_score = 0
        self.best_grid = None

    def create_track(self, grid, i):
        """
        Chooses first random station and adding it to the track.
        """
        # choose random first station
        first_station = grid.stations[random.choice(list(grid.stations))]
        first_station_name = first_station.name

        # adds track
        track = Track(f"track_{str(i)}", grid)
        track.add_station(grid, first_station_name)

        return track
    
    def extend_track(self, track, grid):
        """
        Keeps adding connections untill the time limit is reached and stations can not be added anymore. 
        """
        # adds following stations depending on connections 
        for i in range(MAX_TRACK_LENGTH):
            # check if it is the first station you add to the existing track, otherwise grab last station
            if len(track.stations) == 1:
                first_station = list(track.stations.values())[0]
                station_connections = first_station.get_connections()
            else:
                station_connections = list(track.stations.values())[-1].get_connections()

            # chooses random connection to add to the track
            next_station_object = random.choice(station_connections)
            next_station = next_station_object[0].name
            track.add_station(grid, next_station)
    
    def run(self):
        """
        Runs the algorithm x amount of times, generating the score of the solution each time. 
        """
        # runs algorithm x amount of times
        for i in range(self.loop_amount):
            # create clean grid
            grid = self.base_grid.copy()

            # creates x amount of tracks
            for j in range(self.track_amount):
                track = self.create_track(grid, j)
                self.extend_track(track, grid)
                grid.add_track(track)
            
            score = grid.get_quality()

            # checks if the found score is the best score
            if score > self.best_score:
                self.best_score = score
                self.best_grid = copy.deepcopy(grid)