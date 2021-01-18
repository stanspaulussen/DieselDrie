import copy 
from code.classes.track import Track


class Greedy():

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid) # deze deepcopy moet uiteindelijk wel gereturnt worden denk ik
        self.best_score = 0
        self.best_connection = []
        
    
    def run(self):

        count = 0
        for i in range(7):

            stations = list(self.grid.stations.values())
            # add a first station to the track  
            for station in stations:
                
                connections = station.connections

                track = Track(f"greedy_track_{count}", self.grid)
                track.add_station(self.grid, station.name)

                # calculate quality of all connections and save the best connection
                for connection in connections: # dit kan allemaal in een functie zodat ik makkelijk RandGreedy kan maken
                    next_station = stations[int(connection)].name
                    track.add_station(self.grid, next_station)

                    quality = self.grid.get_quality()
                    track.remove_last_station()

                    if quality > self.best_score:
                        self.best_score = quality 
                        self.best_connection = [station , next_station] # ga je nu alleen maar 1 kant op die connectie checken?

            track = Track(f"greedy_track_{count}", self.grid)
            track.add_station(self.grid, self.best_connection[0].name)

            while track.add_station(self.grid, self.best_connection[1]):
                connections = self.grid.get_station(self.best_connection[1]).connections

                # calculate quality of all connections
                for connection in connections.values():
                    next_station = connection[0].name
                    
                    # dit checkt of de max lengte niet overschreden wordt right?
                    if track.add_station(self.grid, next_station) is False:
                        break
                    quality = self.grid.get_quality()
                    track.remove_last_station()

                    if quality > self.best_score:
                        self.best_score = quality 
                        self.best_connection = [station , next_station]
                
                print(f"beste score: {self.best_score}")
                print(f"beste connectie: {self.best_connection}")
                
            count += 1

        print(" EINDE")
        
        print(f"final_track: {self.grid.tracks}")
        print(f"quality van de tracks = {self.grid.get_quality()}") # ik heb dit nu in main dus kan weg denk ik