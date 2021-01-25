from code.algorithms.depth_first import Depth_first
from code.algorithms.depth_first_2 import Depth_first_2


import copy
from code.classes.track import Track
from code.classes.grid import Grid 

class Depth_first_3(Depth_first_2):

    def run(self):

        # run as long as there are stations in the stack
        for i in range(self.track_amount):
            
            print(f"started track {i}\n")

            station_list = self.create_station_list()
            
            new_grid = copy.deepcopy(self.grid)

            track = self.create_new_track(station_list, i, new_grid)

            # visit all possibilities 
            self.visit_all_possibilities(self.first_station, track, new_grid)

            self.update_station_dict(self.grid)
    
    def create_new_track(self, station_list, i, new_grid):
        print(f"dit is de station list: {station_list}")
        print(f"dit is de ongesorteerde lijst: {self.station_dict}")

        while self.station_dict[station_list[0]] <= 0:
            print("eerste station heeft 0 of 2 open verbindingen")
            self.stations[station_list.pop(0)]            
    
        print("eerste station heeft goed aantal verbindingen")
        self.first_station = self.stations[station_list.pop(0)]
        print(f"dit is het eerste station: {self.first_station}")
        track = Track(f"depthfirst_{i}", new_grid)
        track.add_station(new_grid, self.first_station.name)


        return track
    
    def update_station_dict(self, final_grid):

        last_track = list(final_grid.tracks.values())[-1]

        print(f"Laatste track: {last_track}")
        track_length = len(last_track.stations)

        for station in last_track.stations:
            if station == 0:
                print(f"eerste station is: {last_track.stations[station]}")
                value = self.station_dict[last_track.stations[station].station_id]
                new_value = value - 1
                self.station_dict[last_track.stations[station].station_id] = new_value

            elif station == track_length - 1:
                print(f"laatste  station is: {last_track.stations[station]}")
                value = self.station_dict[last_track.stations[station].station_id]
                new_value = value - 1
                self.station_dict[last_track.stations[station].station_id] = new_value
            else:
                print(f"dit is het station: {last_track.stations[station]}")
                value = self.station_dict[last_track.stations[station].station_id]
                new_value = value - 2
                self.station_dict[last_track.stations[station].station_id] = new_value
        
        print(f"FINAL DICT: {self.station_dict}")

        


        
    

        
