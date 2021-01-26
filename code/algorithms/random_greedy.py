"""
random_greedy.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file contains the random greedy algorithm, which chooses a random starting 
connection for each track and keeps adding the next best connection (greedy) to 
the track untill the time limit is reached.
"""

import copy
import random
from code.classes.track import Track
from code.algorithms.greedy import Greedy


class Random_greedy(Greedy):
    """
    Chooses random starting connection for each track and continues to add connections to the track based on the greedy algorithm.
    """

    def __init__(self, grid, data, track_amount, loop_amount):
        Greedy.__init__(self, grid, data, track_amount)

        self.loop_amount = loop_amount
        self.best_grid_score = 0
        self.best_grid = None
        self.base_grid = copy.deepcopy(grid)
    
    def pick_first_connection(self):
        """
        Picks the first connection of the track randomly.
        """

        stations = list(self.grid.stations.values())

        # # choose random first station
        first_station = random.choice(stations)
        first_station_name = first_station.name

        self.track = Track(f"greedy_track_{self.count}", self.grid)
        self.track.add_station(self.grid, first_station_name)

        connections = list(first_station.connections.values())

        next_station = random.choice(connections)

        self.best_connection = [None, next_station[0].name]

        self.count += 1

        return None
    
    def run(self):
        """
        Runs the algorithm x amount of times, generating the score of the solution each time. 
        """

        for j in range(self.loop_amount):
            if j % 500 == 0:
                print(f"loop {j}")
            
            self.grid = self.base_grid.copy()
            self.best_score = 0
            self.count = 0

            for i in range(self.track_amount):

                station = None
                
                # choose first connection
                self.pick_first_connection()

                # make sure a track doesn't exceed its max length
                while self.track.add_station(self.grid, self.best_connection[1]):
                    # add connection to the track with greatest quality 
                    self.pick_next_station(station)
            
            quality = self.grid.get_quality()
            if quality > self.best_grid_score:
                self.best_grid_score = quality
                print(f"new best score: {self.best_grid_score}")
                self.best_grid = copy.deepcopy(self.grid)