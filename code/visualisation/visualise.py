"""
visualise.py
Minor Programming: Theory
By: Pauline van Lieshout, Jari Hoffman and Stans Paulussen

This file allows for visualisation of the traintracks.

X and y coordinates are swapped in the input file and corrected in this file. 
"""


import matplotlib.pyplot as plt
from code.classes.grid import Grid
import numpy as np


def graph(grid):
    """
    Creates a graph based on the current state of the grid stations, connections and tracks.
    """
    
    # retrieves stations and tracks 
    stations = grid.stations.values()
    tracks = grid.tracks.values()

    # gets coordinates of stations
    for station in stations:

        # gets coordinates of the first station of a connection (station A)
        x_A = float(station.y_coord)
        y_A = float(station.x_coord)
        plt.text(x_A, y_A, f" {station.name}", fontsize=8)

        connections = station.connections 

        # gets coordinates of the second station of a connection (station B)
        for connection in connections:
            
            destination = grid.stations.get(connection)

            x_B = float(destination.y_coord)
            y_B = float(destination.x_coord)

            # plots the stations and their connections in graph
            plt.plot([x_A, x_B], [y_A, y_B], '.-k', linewidth=0.5)

    # adds styling to track plot 
    colors = ['.:k', '.-r', '.:g', '.-b', '.:y', '.-m', '.:c']
    line_widths = [8, 7, 6, 5, 4, 3, 2]
    cursor = 0

    # goes through tracks
    for track in tracks:

        # styling of tracks
        color = colors[cursor % 7]
        line_width = line_widths[cursor % 7]
        cursor += 1

        track_list = list(track.stations.values())

        # goes through track connections
        for i in range(len(track_list)):
            if (i + 1) in range(len(track_list)):

                # gets coordinates of track connections
                x_A = float(track_list[i].y_coord)
                y_A = float(track_list[i].x_coord)
                x_B = float(track_list[i + 1].y_coord)
                y_B = float(track_list[i + 1].x_coord)
                
                # plots tracks
                plt.plot([x_A, x_B], [y_A, y_B], color, alpha=0.7, linewidth=line_width)
            
    plt.show()

            
            