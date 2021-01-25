import copy
from code.classes.track import Track
from code.classes.grid import Grid 


class Depth_first:

    def __init__(self, grid, data, track_amount):
        self.grid = copy.deepcopy(grid)
        self.data = data 
        self.stations = self.grid.stations
        self.track_amount = track_amount
        self.best_score = 0

    def run(self):
        station_dict = {}
        for station in self.stations:
            length = len(self.stations[station].connections)
            station_dict[station] = length

        sorted_station_list = sorted(station_dict, key=station_dict.get)

        # run as long as there are stations in the stack
        for i in range(self.track_amount):
            
            print(f"started track {i}\n")
            
            new_grid = copy.deepcopy(self.grid)

            # get first station of stack 
            first_station = self.stations[sorted_station_list.pop(0)]
            # print("\n")
            # print(f"Eerste station: {first_station}")

            # add first station to track
            track = Track(f"depthfirst_{i}", new_grid)
            track.add_station(new_grid, first_station.name)

            # visit all possibilities 
            self.visit_all_possibilities(first_station, track, new_grid)
        
            # print(track)
        
    
    def visit_all_possibilities(self, first_station, track, grid):

        for connection in first_station.connections:
            # add station to track

            new_grid = copy.deepcopy(grid)
            new_track = new_grid.tracks[track.track_name]
            while new_track.add_station(new_grid, self.stations[connection].name):

                if new_grid.get_quality() > self.best_score:
                    self.best_score = new_grid.get_quality()
                    self.grid = copy.deepcopy(new_grid)
                    print(f"new best score: {self.best_score}:\n{self.grid}\n\n")

                # print(self.tracks)
                # print("\n")

                self.visit_all_possibilities(self.stations[connection], new_track, new_grid)



                
            

            

            

