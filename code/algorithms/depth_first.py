import copy
from code.classes.track import Track
from code.classes.grid import Grid 


class Depth_first:

    def __init__(self, grid, data):
        self.grid = copy.deepcopy(grid)
        self.visited = set()
        self.data = data 
        self.stations = self.grid.stations
    

    def run(self):

        stations_list = list(self.stations)

        # run as long as there are stations in the stack
        while stations_list:

            # get first station of stack 
            first_station = self.stations[stations_list.pop(0)]
            print("\n")
            print(f"Eerste station: {first_station}")

            # visit all possibilities 
            self.visit_all_possibilities(self.visited, self.stations, first_station)
        
    
    def visit_all_possibilities(self, visited, stations, first_station):

        for connection in first_station.connections:
            if connection not in self.visited:
                self.visited.add(connection)                

                for new_connection in self.stations[connection].connections:
                    print(self.stations[new_connection])
                    self.visit_all_possibilities(self.visited, stations, self.stations[new_connection])

            

            

            

