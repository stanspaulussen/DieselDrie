import copy
from code.classes.track import Track
from code.classes.grid import Grid 


class Depth_first:

    def __init__(self, grid, data):
        self.grid = copy.deepcopy(grid)
        self.data = data 
        self.stations = self.grid.stations
        self.track = Track(f"depthfirst_0", self.grid )
        self.tracks = []

    
    def run(self):

        stations_list = list(self.stations)

        # run as long as there are stations in the stack
        #while stations_list:
        for i in range(1):

            # get first station of stack 
            first_station = self.stations[stations_list.pop(0)]
            print("\n")
            print(f"Eerste station: {first_station}")

            # add first station to track
            track = copy.deepcopy(self.track)
            new_grid = copy.deepcopy(self.grid)
            track.add_station(new_grid, first_station.name)


            # visit all possibilities 
            self.visit_all_possibilities(self.stations, first_station, track)
        
            print(track)


    def visit_all_possibilities(self, stations, first_station, track):

        for connection in first_station.connections:

            # add station to track
            new_track = copy.deepcopy(track)
            while new_track.add_station(copy.deepcopy(self.grid), self.stations[connection].name):
            
                print(new_track)
                print("\n")
    
                self.visit_all_possibilities(stations, self.stations[connection], new_track)



                
            

            

            

