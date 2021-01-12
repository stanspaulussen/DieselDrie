import matplotlib.pyplot as plt
from code.classes.grid import Grid
import numpy as np

def graph(grid):
    
    stations = grid.stations.values()
    tracks = grid.tracks.values()
    colors = ['.-r', '.-g', '.-b', '.-y', '.-m', '.-c','.--k']
    cursor = 0

    # get coordinates 
    for station in stations:

        connections = station.connections 

        y_A = float(station.x_coord)
        x_A = float(station.y_coord)

        for connection in connections:

            
            destination = grid.stations.get(connection)


            y_B = float(destination.x_coord)
            x_B = float(destination.y_coord)


            
            plt.scatter([x_A, x_B], [y_A, y_B])
            
            plt.plot([x_A, x_B], [y_A, y_B], '.-k')
            plt.text(x_A, y_A, station.name)
            plt.text(x_B, y_B, destination.name)

    for track in tracks:
        print("Hier komt de track")
        print(track)
        color = colors[cursor]
        cursor += 1

        track_list = list(track.stations.values())

        for i in range(len(track_list)):
            if (i + 1) in range(len(track_list)):
                y_A = float(track_list[i].x_coord)
                x_A = float(track_list[i].y_coord)

                
                y_B = float(track_list[i + 1].x_coord)
                x_B = float(track_list[i + 1].y_coord)
 
                plt.plot([x_A, x_B], [y_A, y_B], color)

            
        
            
    plt.show()

            
            