from code.classes import grid, station, track
from code.visualisation import visualise
from code.algorithms import randomise, greedy
import csv

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    print("Choose your algorithm:")
    print("1: Random")
    print("2: Greedy")
    print("3: Random Greedy")

    choice = False

    while choice == False:
        num = int(input("number of chosen algorithm: "))

        if num == 1:
            choice = True
            randomise.random_track(test_grid)
        elif num == 2:
            choice = True
            greedy = greedy.Greedy(test_grid)
            greedy.run()
        elif num == 3:
            print("That algorithm is still under construction, please choose another one")
        else:
            print("That input is incorrect, please try again")

    print("The algorithm has finished, this is your score:")
    print(test_grid.get_quality())
    print("This is what the solution looks like:")
    visualise.graph(test_grid)

    # print(test_grid)
    # print(test_grid.stations)

    # # Creating track 1
    # track_1 = track.Track('train_1', test_grid)

    # track_1.add_station(test_grid, 'Delft')
    # track_1.add_station(test_grid, 'Schiedam Centrum')
    # track_1.add_station(test_grid, 'Rotterdam Centraal')
    # track_1.add_station(test_grid, 'Dordrecht')
    # track_1.add_station(test_grid, 'Rotterdam Centraal')
    # track_1.add_station(test_grid, 'Rotterdam Alexander')
    # track_1.add_station(test_grid, 'Gouda')
    # track_1.add_station(test_grid, 'Den Haag Centraal')
    # track_1.add_station(test_grid, 'Delft')
    # track_1.add_station(test_grid, 'Schiedam Centrum')
    # track_1.add_station(test_grid, 'Rotterdam Centraal')
    # track_1.add_station(test_grid, 'Rotterdam Alexander')

    # # creating track 2
    # track_2 = track.Track('train_2', test_grid)

    # track_2.add_station(test_grid, 'Alkmaar')
    # track_2.add_station(test_grid, 'Castricum')
    # track_2.add_station(test_grid, 'Beverwijk')
    # track_2.add_station(test_grid, 'Zaandam')
    # track_2.add_station(test_grid, 'Amsterdam Sloterdijk')
    # track_2.add_station(test_grid, 'Amsterdam Centraal')
    # track_2.add_station(test_grid, 'Amsterdam Amstel')
    # track_2.add_station(test_grid, 'Amsterdam Centraal')
    # track_2.add_station(test_grid, 'Amsterdam Amstel')
    # track_2.add_station(test_grid, 'Amsterdam Zuid')
    # track_2.add_station(test_grid, 'Amsterdam Sloterdijk')
    # track_2.add_station(test_grid, 'Haarlem')

    # # creating track 3
    # track_3 = track.Track('train_3', test_grid)

    # track_3.add_station(test_grid, 'Beverwijk')
    # track_3.add_station(test_grid, 'Haarlem')
    # track_3.add_station(test_grid, 'Heemstede-Aerdenhout')
    # track_3.add_station(test_grid, 'Haarlem')
    # track_3.add_station(test_grid, 'Heemstede-Aerdenhout')
    # track_3.add_station(test_grid, 'Leiden Centraal')
    # track_3.add_station(test_grid, 'Heemstede-Aerdenhout')
    # track_3.add_station(test_grid, 'Leiden Centraal')
    # track_3.add_station(test_grid, 'Alphen a/d Rijn')
    # track_3.add_station(test_grid, 'Gouda')
    # track_3.add_station(test_grid, 'Rotterdam Alexander')

    # # creating track 4
    # track_4 = track.Track('train_4', test_grid)

    # track_4.add_station(test_grid, 'Amsterdam Sloterdijk')
    # track_4.add_station(test_grid, 'Amsterdam Zuid')
    # track_4.add_station(test_grid, 'Amsterdam Amstel')
    # track_4.add_station(test_grid, 'Amsterdam Zuid')
    # track_4.add_station(test_grid, 'Schiphol Airport')
    # track_4.add_station(test_grid, 'Leiden Centraal')
    # track_4.add_station(test_grid, 'Schiphol Airport')
    # track_4.add_station(test_grid, 'Amsterdam Zuid')
    # track_4.add_station(test_grid, 'Amsterdam Amstel')
    # track_4.add_station(test_grid, 'Amsterdam Zuid')
    # track_4.add_station(test_grid, 'Amsterdam Amstel')
    # track_4.add_station(test_grid, 'Amsterdam Centraal')

    # # creating track 5
    # track_5 = track.Track('train_5', test_grid)

    # track_5.add_station(test_grid, 'Zaandam')
    # track_5.add_station(test_grid, 'Hoorn')
    # track_5.add_station(test_grid, 'Alkmaar')
    # track_5.add_station(test_grid, 'Den Helder')

    # # creating track 6
    # track_6 = track.Track('train_6', test_grid)

    # track_6.add_station(test_grid, 'Zaandam')
    # track_6.add_station(test_grid, 'Hoorn')
    # track_6.add_station(test_grid, 'Zaandam')
    # track_6.add_station(test_grid, 'Castricum')
    # track_6.add_station(test_grid, 'Alkmaar')
    # track_6.add_station(test_grid, 'Den Helder')

    # # creating track 7
    # track_7 = track.Track('train_7', test_grid)

    # track_7.add_station(test_grid, 'Schiedam Centrum')
    # track_7.add_station(test_grid, 'Delft')
    # track_7.add_station(test_grid, 'Den Haag Centraal')
    # track_7.add_station(test_grid, 'Gouda')
    # track_7.add_station(test_grid, 'Den Haag Centraal')
    # track_7.add_station(test_grid, 'Leiden Centraal')
    # track_7.add_station(test_grid, 'Schiphol Airport')
    # track_7.add_station(test_grid, 'Amsterdam Zuid')
    # track_7.add_station(test_grid, 'Schiphol Airport')
    # track_7.add_station(test_grid, 'Leiden Centraal')

    
    # # # RANDOMISE FUNCTION AANROEPEN
    # # randomise.random_track(test_grid)

    # # # goal function
    # # print(test_grid.get_quality())
    # quality = test_grid.get_quality()
    # print(quality)
    
    # # # append quality score to csv file 
    # # with open ('output.csv', 'a') as f: 
    # #     for track in test_grid.tracks:
    # #         f.write(f" {str(track)} : {test_grid.tracks[track]}")
    # #         f.write("\n")
    # #     f.write(str(quality))
    # #     f.write("\n")
    # #     f.write("\n")

    
    # # with open ('output_1line.csv', 'a') as f:
    # #     f.write("\n")
    # #     f.write(f"{str(quality)}, {str(test_grid.tracks)}")

    # # while True:
    # #     test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    # #     randomise.random_track(test_grid)

    # #     quality = test_grid.get_quality()

    # #     with open ('output_1line.csv', 'a') as f:
    # #         f.write("\n")
    # #         f.write(f"{str(quality)}, {str(test_grid.tracks)}")

    

    # # graph
    
    # visualise.graph(test_grid)

    # greedy 
    # greedy = greedy.Greedy(test_grid)
    # greedy.run()
