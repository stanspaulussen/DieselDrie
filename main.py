from code.classes import grid, station, track

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    print(test_grid)
    print(test_grid.stations)

    # Creating a track 
    test_track = track.Track('train_1')

    print("test")
    print(test_track)
    test_track.add_station("Alkmaar")
    print(test_track)

