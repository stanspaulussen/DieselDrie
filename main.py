from code.classes import grid, station, track, testgraph
from code.algorithms import algorithm

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    # print(test_grid)
    # print(test_grid.stations)

    # Creating a track 
    test_track = track.Track('train_1', test_grid)


    test_track.add_station(test_grid, 'Hoorn')
    test_track.add_station(test_grid, 'Alkmaar')
    test_track.add_station(test_grid, 'Zaandam')
    test_track.add_station(test_grid, 'Den Helder')


    # goal function
    print(test_grid.get_quality())

    # graph
    
    graph(test_grid)


