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

        self.new_grid = copy.deepcopy(self.grid)
    

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
            track.add_station(self.new_grid, first_station.name)


            # visit all possibilities 
            self.visit_all_possibilities(self.visited, self.stations, first_station, track)
        
            print(track)
        
    
    def visit_all_possibilities(self, visited, stations, first_station, track):

        for connection in first_station.connections:
            if self.stations[connection] not in self.visited:
                self.visited.add(self.stations[connection])

                # add station to track
                new_track = copy.deepcopy(track)
                new_track.add_station(self.new_grid, self.stations[connection].name)
                print(f"dit is de nieuwe track: {new_track}")


                # for new_connection in self.stations[connection].connections:
                #     if self.stations[new_connection] not in self.visited:
                #         self.visited.add(self.stations[new_connection])

                #          # add station to track
                #         track.add_station(self.new_grid, self.stations[new_connection].name)

                self.visit_all_possibilities(self.visited, stations, self.stations[connection], new_track)
            

            

            

