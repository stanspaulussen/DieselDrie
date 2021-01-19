from code.classes import grid, station, track
from code.visualisation import visualise
from code.algorithms import randomise, greedy, greedy_lookahead
import csv

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    print("Choose your algorithm:")
    print("1: Random")
    print("2: Greedy")
    print("3: Random Greedy")
    print("4: Greedy with Lookahead")

    choice = False

    while choice == False:

        while True:
            try: 
                num = int(input("number of chosen algorithm: "))
            except ValueError:
                print("That input is incorrect, please try again and type an integer")
                continue 
            else:
                break 

        if num == 1:
            choice = True
            while True:
                try:
                    loop_amount = int(input("How many loops should the algorithm do?\n"))
                except ValueError:
                    print("That input is incorrect, please try again and type an integer")
                    continue
                else:
                    break
            while True:
                try:
                    track_amount = int(input("How many tracks should the algorithm make?\n"))
                except ValueError:
                    print("That input is incorrect, please try again and type an integer")
                    continue
                else:
                    break
            random = randomise.Random(test_grid, loop_amount, track_amount)
            random.run()
            test_grid = random.best_grid
        elif num == 2:
            choice = True
            greedy = greedy.Greedy(test_grid)
            greedy.run()
            test_grid = greedy.grid
        elif num == 3:
            print("That algorithm is still under construction, please choose another one")
        elif num == 4:
            choice = True
            greedy_lookahead = greedy_lookahead.Greedy_Lookahead(test_grid)
            greedy_lookahead.run()
            test_grid = greedy_lookahead.grid
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
