from code.classes import grid, station, track
from code.algorithms import algorithm

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    print(test_grid)
    print(test_grid.stations)

    # Creating a track 
    test_track = track.Track('train_1')

    print(test_track)
    test_track.add_station(test_grid, 'Hoorn')
    test_track.add_station(test_grid, 'Alkmaar')

    print(test_track)

    # goal function
    print(test_grid.get_quality(test_track))


