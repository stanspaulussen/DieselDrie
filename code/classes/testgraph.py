import matplotlib.pyplot as plt
from .grid import Grid 

def graph(grid):
    
    stations = grid.stations.values()
    
    # get coordinates 
    for station in stations:
        print("station")
        print(station)
        connections = station.connections 
        print("KIJK")
        print(connections)
        x_A = station.x_coord
        y_A = station.y_coord 

        for connection in connections:
            print(" nu komt de connectie")
            print(connection)
            
            destination = grid.stations.get(connection)
            print(destination)

            x_B = destination.x_coord
            y_B = destination.y_coord
            print(x_B)
            print(y_B)

            plt.plot([x_A, x_B], [y_A, y_B], '.-k')
            
    plt.show()

            
            