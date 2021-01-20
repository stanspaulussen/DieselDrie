import random
import copy
from code.classes.grid import Grid
from code.classes.track import Track
from code.classes.station import Station

MAX_TRACK_LENGTH = 24

class Random():
    def __init__(self, grid, loop_amount, track_amount, data):
        self.base_grid = grid
        self.loop_amount = loop_amount
        self.track_amount = track_amount
        self.data = data
        self.best_score = 0
        self.best_grid = None

    def create_track(self, grid, i):
        # choose random first station
        first_station = grid.stations[random.choice(list(grid.stations))]
        first_station_name = first_station.name

        # adds track
        track = Track(f"track_{str(i)}", grid)
        track.add_station(grid, first_station_name)

        return track
    
    def extend_track(self, track, grid):
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
        for i in range(self.loop_amount):
            # create clean grid
            grid = self.base_grid.copy()

            for j in range(self.track_amount):

                track = self.create_track(grid, j)

                self.extend_track(track, grid)

                grid.add_track(track)
            
            score = grid.get_quality()

            if score > self.best_score:
                self.best_score = score
                self.best_grid = copy.deepcopy(grid)



# def random_track(grid): 
#     """
#     Chooses random starting point and following stations of a track. 
#     """

#     number_of_tracks = 7

#     for i in range(number_of_tracks):
#         # choose random first station
#         first_station = grid.stations[random.choice(list(grid.stations))]
#         first_station_name = first_station.name

#         # adds track
#         track = Track(f"track_{str(i)}", grid)
#         track.add_station(grid, first_station_name)

#         # adds following stations depending on connections 
#         for i in range(24):
#             # check if it is the first station you add to the existing track, otherwise grab last station
#             if len(track.stations) == 1:
#                 print(f"first station: {first_station}")
#                 print(f"ingewikkeld ding: {list(track.stations.values())[0]}")
#                 station_connections = first_station.get_connections()
#             else:
#                 station_connections = list(track.stations.values())[-1].get_connections()

#             # chooses random connection to add to the track
#             next_station_object = random.choice(station_connections)
#             next_station = next_station_object[0].name
#             track.add_station(grid, next_station)

#         grid.add_track(track)