from code.algorithms.depth_first import Depth_first

import copy
from code.classes.track import Track
from code.classes.grid import Grid 

class Depth_first_3(Depth_first):

    def run(self):

        # run as many times as there are tracks to be made 
        for i in range(self.track_amount):
            
            print(f"started track {i}\n")
            
            # create a copy of the grid 
            new_grid = copy.deepcopy(self.grid)

            # initialize a new track with first station already added
            track = self.create_new_track(i, new_grid)

            if track:
                # visit all possibilities 
                self.visit_all_possibilities(self.first_station, track, new_grid)
                self.update_station_dict()

            #stop adding tracks if all connections are used 
            else:
                break

            
    
    def create_new_track(self, i, new_grid):
        """
        Create a new track and pick a station with the fewest available connections to be the starting point of the track.
        Stop making new tracks if no more connections are available 
        """
        for key in self.station_dict:
            # skip a station if it has less or more than 1 open connection 
            if self.station_dict[key] != 1:
                continue 
            # create a new track and add the station with fewest available connections as starting station 
            else:
                self.first_station = self.stations[key]
                track = Track(f"depthfirst_{i}", new_grid)
                track.add_station(new_grid, self.first_station.name)
                return track   
        return False 
        

    
    def update_station_dict(self):
        """
        Updates the dictionary which stores all available connections of the stations after a track is made. 
        """

        # define the last added track to the grid 
        last_track = list(self.grid.tracks.values())[-1]

        # define the amount of stations in the track 
        track_length = len(last_track.stations)

        for station in last_track.stations:
            # substract 1 connection from dict if the station is either the first or last station of the track
            if station == 0 or station == track_length - 1:
                value = self.station_dict[last_track.stations[station].station_id]
                self.station_dict[last_track.stations[station].station_id] = value - 1
            # substract two connections from dict if station is in the middle of the track
            else:
                value = self.station_dict[last_track.stations[station].station_id]
                self.station_dict[last_track.stations[station].station_id] = value - 2 
        

        


        
    

        
