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
        num = input("number of chosen algorithm: ")

        # TODO: check if string or int

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

    # TODO: create output file

    # # # append quality score to csv file 
    # # with open ('output.csv', 'a') as f: 
    # #     for track in test_grid.tracks:
    # #         f.write(f" {str(track)} : {test_grid.tracks[track]}")
    # #         f.write("\n")
    # #     f.write(str(quality))
    # #     f.write("\n")
    # #     f.write("\n")
    
    # #     with open ('output_1line.csv', 'a') as f:
    # #         f.write("\n")
    # #         f.write(f"{str(quality)}, {str(test_grid.tracks)}")
