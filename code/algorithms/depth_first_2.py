from code.algorithms.depth_first import Depth_first

import copy
from code.classes.track import Track
from code.classes.grid import Grid 

class Depth_first_2(Depth_first):
    def visit_all_possibilities(self, first_station, track, grid):
        for connection in first_station.connections:
            # add station to track

            # new_grid = copy.deepcopy(grid)
            # new_track = new_grid.tracks[track.track_name]
            if track.add_station(grid, self.stations[connection].name):

                if grid.get_quality() > self.best_score:
                    self.best_score = grid.get_quality()
                    self.grid = copy.deepcopy(grid)
                    #print(f"new best score: {self.best_score}:\n{self.grid}\n\n")
                    

                # print(self.tracks)
                # print("\n")

                self.visit_all_possibilities(self.stations[connection], track, grid)

                track.remove_last_station()
