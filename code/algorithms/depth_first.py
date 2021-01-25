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
        self.station_dict = self.make_station_dict()

    def run(self):

        station_list = self.create_station_list()

        # run as long as there are stations in the stack
        for i in range(self.track_amount):
            
            print(f"started track {i}\n")
            
            new_grid = copy.deepcopy(self.grid)

            track = self.create_new_track(station_list, i, new_grid)

            # visit all possibilities 
            self.visit_all_possibilities(self.first_station, track, new_grid)

            

        
    def create_new_track(self, station_list, i, new_grid):
        self.first_station = self.stations[station_list.pop(0)]
        track = Track(f"depthfirst_{i}", new_grid)
        track.add_station(new_grid, self.first_station.name)

        return track
    
    def make_station_dict(self):

        self. station_dict = {}

        for station in self.stations:
            length = len(self.stations[station].connections)
            self.station_dict[station] = length
        
        return self.station_dict
                
    
    def create_station_list(self):

        sorted_station_list = sorted(self.station_dict, key=self.station_dict.get)

        return sorted_station_list

    def visit_all_possibilities(self, first_station, track, grid):

        for connection in first_station.connections:
            # add station to track

            new_grid = copy.deepcopy(grid)
            new_track = new_grid.tracks[track.track_name]
            while new_track.add_station(new_grid, self.stations[connection].name):

                if new_grid.get_quality() > self.best_score:
                    self.best_score = new_grid.get_quality()
                    self.grid = copy.deepcopy(new_grid)
                    #print(f"new best score: {self.best_score}:\n{self.grid}\n\n")

                # print(self.tracks)
                # print("\n")

                self.visit_all_possibilities(self.stations[connection], new_track, new_grid)
        



                
            

            

            

