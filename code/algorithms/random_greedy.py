import copy
import random
from code.classes.track import Track
from code.algorithms.greedy import Greedy


class Random_greedy(Greedy):
    def pick_first_connection(self):
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