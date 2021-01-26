"""
greedy_lookahead.py
Minor Programming: Programming Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file contains the Greedy with lookahead algorithm, which searches for the best
three connections from which the first connection is eventually added to the track.
"""

import copy 
from code.classes.track import Track
from code.algorithms.greedy import Greedy


class Greedy_Lookahead(Greedy):
    """
    For each track, choosing the first connection of the best three connections found and adding it to the track. 
    """

    def pick_first_connection(self):
        """
        Picks the first connection based on the best three connections possible.
        """

        self.best_connection = []
        stations = list(self.grid.stations.values())

        # add a first station to the track  
        for station in stations:

            self.track = Track(f"greedy_track_{self.count}", self.grid)
            self.track.add_station(self.grid, station.name)

            lookahead_1 = station.connections

            # calculate quality of all connections and save the best connection
            for la1 in lookahead_1: 
                
                next_station = stations[int(la1)].name
                self.track.add_station(self.grid, next_station)
                lookahead_2 = stations[int(la1)].get_connections()
                
                for la2 in lookahead_2:
                    
                    # if adding the connection exceeds the track's max time length 
                    if self.track.add_station(self.grid, la2[0].name) is False:
                        break
                    
                    quality = self.grid.get_quality()
                    self.track.remove_last_station()
 
                    if quality > self.best_score:
                        self.best_score = quality 
                        self.best_connection = [station.name, stations[int(la1)].name, la2[0].name]
                self.track.remove_last_station()
        
        try:
            # add best connection to the track
            self.track = Track(f"greedy_track_{self.count}", self.grid)
            self.track.add_station(self.grid, self.best_connection[0])

            self.count += 1

            return station 

        except IndexError:
            return False


    def pick_next_station(self, station):
        """
        Picks the next station based on the three connections that produce the best score. 
        """

        self.best_score = 0

        stations = self.grid.stations
        # all connections of the last added added station 
        lookahead_1 = self.grid.get_station(self.best_connection[1]).connections

        for la1 in lookahead_1.values():
            next_station = la1[0].name
            
            # if adding the connection exceeds the tracks max time length 
            if self.track.add_station(self.grid, next_station) is False:
                break

            lookahead_2 = self.grid.get_station(la1[0].name).connections

            # keeps adding stations untill the time limit is reached
            for la2 in lookahead_2:
                la2 = stations.get(la2)
                if self.track.add_station(self.grid, la2.name) is False:
                    break
                
                quality = self.grid.get_quality()
                
                self.track.remove_last_station()

                # if quality improves, add station to the track
                if quality > self.best_score:
                    self.best_score = quality 
                    self.best_connection = [la2.name, la1[0].name]
                    
            self.track.remove_last_station()





