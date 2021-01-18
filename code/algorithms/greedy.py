import copy 
from code.classes.track import Track


class Greedy():

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid) 
        self.best_score = 0
        self.best_connection = []
        self.track = Track(f"greedy_track_0", self.grid)
        self.count = 0 
    
    def check_best_score(self, track, station, next_station):
        """
        Checks if connection generates new best score 
        """

        quality = self.grid.get_quality()
        track.remove_last_station()

        if quality > self.best_score:
            self.best_score = quality 
            self.best_connection = [station , next_station]
    
    def pick_first_connection(self):
        """
        Chooses first conenction with greatest quality 
        """

        stations = list(self.grid.stations.values())

        # add a first station to the track  
        for station in stations:
            
            connections = station.connections

            self.track = Track(f"greedy_track_{self.count}", self.grid)
            self.track.add_station(self.grid, station.name)

            # calculate quality of all connections and save the best connection
            for connection in connections: # dit kan allemaal in een functie zodat ik makkelijk RandGreedy kan maken
                next_station = stations[int(connection)].name
                self.track.add_station(self.grid, next_station)

                self.check_best_score(self.track, station, next_station)

        self.track = Track(f"greedy_track_{self.count}", self.grid)
        self.track.add_station(self.grid, self.best_connection[0].name)

        self.count += 1

        return station 


    def run(self):

        for i in range(7):

            station = self.pick_first_connection()

            while self.track.add_station(self.grid, self.best_connection[1]):

                connections = self.grid.get_station(self.best_connection[1]).connections

                # calculate quality of all connections
                for connection in connections.values():
                    next_station = connection[0].name
                    
                    # dit checkt of de max lengte niet overschreden wordt right?
                    if self.track.add_station(self.grid, next_station) is False:
                        break

                    self.check_best_score(self.track, station, next_station)
                
                print(f"beste score: {self.best_score}")
                print(f"beste connectie: {self.best_connection}")
                
        

        print(" EINDE")
        
        print(f"final_track: {self.grid.tracks}")
        print(f"quality van de tracks = {self.grid.get_quality()}") # ik heb dit nu in main dus kan weg denk ik

        return self.grid 