from code.classes import grid, station, track
from code.visualisation import visualise
from code.algorithms import algorithm
from code.algorithms import randomise

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    # print(test_grid)
    # print(test_grid.stations)

    # Creating track 1
    track_1 = track.Track('train_1', test_grid)

    track_1.add_station(test_grid, 'Hoorn')
    track_1.add_station(test_grid, 'Alkmaar')
    track_1.add_station(test_grid, 'Hoorn')
    track_1.add_station(test_grid, 'Alkmaar')
    track_1.add_station(test_grid, 'Zaandam')
    track_1.add_station(test_grid, 'Castricum')
    print(track_1)
    track_1.remove_last_station()

    # creating track 2
    track_2 = track.Track('train_2', test_grid)

    track_2.add_station(test_grid, 'Amsterdam Centraal')
    track_2.add_station(test_grid, 'Amsterdam Sloterdijk')
    track_2.add_station(test_grid, 'Amsterdam Zuid')
    track_2.add_station(test_grid, 'Schiphol Airport')
    track_2.add_station(test_grid, 'Leiden Centraal')
    print(track_2)
    

    # goal function
    print(test_grid.get_quality())


    # # RANDOMISE FUNCTION AANROEPEN
    # randomise.random_track(test_grid)

    # graph
    
    visualise.graph(test_grid)











    