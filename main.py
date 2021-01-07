from code.classes import grid, station

if __name__ == "__main__":

    # Create a grid from our data
    test_grid = grid.Grid("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

print(test_grid)
print(test_grid.stations)
