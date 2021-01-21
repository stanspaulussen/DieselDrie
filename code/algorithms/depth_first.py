import copy
from code.classes.track import Track
from code.classes.grid import Grid 


class Depth_first:

    def __init__(self, grid, data):
        self.grid = copy.deepcopy(grid)
        self.visited = set()
        self.data = data 
        self.stations = self.grid.stations
        self.track = Track(f"depthfirst_0", self.grid )
        self.tracks = []

    
    def run(self):

        stations_list = list(self.stations)

        # run as long as there are stations in the stack
        #while stations_list:
        for i in range(1):
            self.visited = set()

            # get first station of stack 
            first_station = self.stations[stations_list.pop(0)]
            print("\n")
            print(f"Eerste station: {first_station}")
            self.visited.add(first_station)

            # add first station to track
            track = copy.deepcopy(self.track)
            new_grid = copy.deepcopy(self.grid)
            track.add_station(new_grid, first_station.name)


            # visit all possibilities 
            self.visit_all_possibilities(self.visited, self.stations, first_station, track)
        
            print(track)
        
    
    def visit_all_possibilities(self, visited, stations, first_station, track):

        for connection in first_station.connections:
            if self.stations[connection] not in self.visited:
                self.visited.add(self.stations[connection])

                # add station to track
                new_track = copy.deepcopy(track)
                while new_track.add_station(copy.deepcopy(self.grid), self.stations[connection].name):
                
                    print(new_track)
                    print("\n")

                    self.tracks.append(new_track)
            

                    self.visit_all_possibilities(self.visited, stations, self.stations[connection], new_track)



                
            

            

            

