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
            track.add_station(self.grid, station.name)

            # calculate quality of all connections and save the best connection 
            for connection in connections:
                next_station = stations[int(connection)].name
                track.add_station(self.grid, next_station)

                quality = self.grid.get_quality()
                track.remove_last_station()

                if quality > self.best_score:
                    self.best_score = quality 
                    self.best_connection = [station , next_station]

        track = Track("greedy_track", self.grid)
        track.add_station(self.grid, self.best_connection[0].name)
        track.add_station(self.grid, self.best_connection[1])
        print(f"Dit is de eerste track: {track}")
        print(f"dit is de eerste quality: {self.grid.get_quality()}")

        
        # get connections of last station 
        connections = self.grid.get_station(self.best_connection[1]).connections
        print(f"dit zijn de connecties van tweede station: {connections}")

        # calculate quality of all connections
        for connection in connections.values():
            next_station = connection[0].name
            print(f"next station: {next_station}")

            track.add_station(self.grid, next_station)
            quality = self.grid.get_quality()
            print(self.grid.get_quality())
            track.remove_last_station()

            if quality > self.best_score:
                self.best_score = quality 
                self.best_connection = [station , next_station]
        
        print(f"beste score: {self.best_score}")
        print(f"beste connectie: {self.best_connection}")
        track.add_station(self.grid, self.best_connection[1])
        
        print(f"final_track: {track}")
            




       
            

    




