from code.classes import grid, station, track
from code.visualisation import visualise
from code.algorithms import randomise, greedy, greedy_lookahead, random_greedy
import csv

if __name__ == "__main__":

    while True: 
        try: 
            data = int(input("Which map would you like to use? Choose '1' for Holland or '2' for the Netherlands.\n"))
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

    # create a grid from our data
    test_grid = grid.Grid(data)
    
    # choose the algorithm
    print("Choose your algorithm:")
    print("1: Random")
    print("2: Greedy")
    print("3: Random Greedy")
    print("4: Greedy with Lookahead")
    print("5: Depth First")


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

            random = randomise.Random(test_grid, loop_amount, track_amount, data)
            random.run()
            test_grid = random.best_grid
        elif num == 2:
            choice = True
            
            greedy = greedy.Greedy(test_grid, data, track_amount)
            greedy.run()
            test_grid = greedy.grid
        elif num == 3:
            choice = True

            r_greedy = random_greedy.Random_greedy(test_grid, data, track_amount)
            r_greedy.run()
            test_grid = r_greedy.grid
        elif num == 4:

            choice = True
            greedy_lookahead = greedy_lookahead.Greedy_Lookahead(test_grid, data, track_amount)
            greedy_lookahead.run()
            test_grid = greedy_lookahead.grid
        elif num == 5:
            choice = True
            depth_first = depth_first.Depth_first(test_grid, data)
            depth_first.run()
            test_grid = depth_first.grid
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
