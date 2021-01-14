import copy 
from code.classes.track import Track


class Greedy():

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.best_score = 0
        self.best_connection = []
        
    
    def run(self):

        stations = list(self.grid.stations.values())
        
        # add a first station to the track  
        for station in stations:
            connections = station.connections

            track = Track("greedy_track", self.grid)
            print(f"dit is het begin station: {station.name}")
            track.add_station(self.grid, station.name)

            # calculate quality of all connections and save the best connection 
            for connection in connections:
                next_station = stations[int(connection)].name
                print(f"Dit is de connectie: {next_station}")
                track.add_station(self.grid, next_station)

                quality = self.grid.get_quality()
                print(self.grid.get_quality())

                if quality > self.best_score:
                    self.best_score = quality 
                    self.best_connection = [station , next_station]
            
            print("Final score")
            print(self.best_score)
            print(self.best_connection)


       
            

    




