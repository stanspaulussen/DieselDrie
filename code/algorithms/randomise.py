import random 
from code.classes.grid import Grid
from code.classes.track import Track
from code.classes.station import Station


def random_track(grid): 
    """
    Chooses random starting point and following stations of a track. 
    """

    # choose random first station
    first_station = grid.stations[random.choice(list(grid.stations))]
    first_station_name = first_station.name

    # adds track
    track = Track("track_0", grid)
    track.add_station(grid, first_station_name)

    # adds following stations depending on connections 
    for i in range(8):
        print("GO")
        # check if it is the first station you add to the existing track, otherwise grab last station
        if len(track.stations) == 1:
            station_connections = first_station.get_connections()
        else:
            station_connections = grid.stations[list(track.stations.keys())[-1]].get_connections()

        # chooses random connection to add to the track
        next_station_object = random.choice(station_connections)
        next_station = next_station_object[0].name
        print("volgende station")
        print(next_station)
        track.add_station(grid, next_station)

    grid.add_track(track)

    print(grid.get_quality())



    
    





