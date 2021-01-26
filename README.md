# RailNL

## Case: RailNL

In the case RailNL the goal is to come up with the most efficiënt way to create a train system through the Netherlands. The efficiency of the train system is determined by the fraction of ridden connections (p), the number of tracks needed (T) and total minutes traveled by all tracks combined (Min). For Holland, the maximum number of tracks is 7, and each track can cover 2 hours worth of connections. For the Netherlands, a maximum of 20 tracks were allowed, each track traveling for a maximum of 3 hours. The following image shows the formula that determines the quality of the train system. 

![K = p * 10.000 - (T * 100 + Min)](https://github.com/stanspaulussen/DieselDrie/blob/main/docs/formula.png)

## Algorithms 

To try to find the best solution for this case, we implemented a number of algorithms. 

* **Randomise** Randomise generates completely random tracks. The number of tracks can be controlled by the user. The tracks run for the maximum amount of time and no quality is calculated untill the train system is formed 

* **Greedy without lookahead** For each track, greedy without lookahead picks the best first connection (based on quality formula) to start with and adds the next connection that leads to the best quality. The algorithm stops when adding a track does not lead to a higher score anymore. 

* **Greedy with lookahead** For each track, greedy with lookahead picks the best starting station not by choosing just one best connection, but by calculating the best three connections and choosing the first one as the starting station. Following, the next connections are picked in the same way, by calculating the best three following connections and picking the first one as the next station. 

* **Random Greedy** Random greedy differs from greedy without lookahead only in choosing the starting station. The starting station is not based on the best calculated connection, but is chosen randomly. After choosing this first station, random greedy behaves in the same manner as greedy without lookahead in picking the next connection. 

* **Depth First** This algorithm searches the state space in a depth first manner, calculating all possible tracks. We added heuristics in choosing the starting station. Stations with the lowest amount of connections are chosen first as starting stations. This way overlap within tracks is minimized, as dead ends are always starting stations. From this starting station, the quality of all possible tracks is calculated and only the track with the highest score is added to the train system. This process continues untill adding another track does not lead to a higher score anymore. 

* **Depth First 2** This algorithm is identical to depth first, except the speed of this algorithm is increased by using less deepcopyies.

* **Depth First 3** In this algorithm, the choice of which station to start at is perfected. Instead of choosing the station with the least amount of connections, this algorithm chooses the station with the least amount of unridden connections. It keeps up how many connections were ridden, and bases its choice on that instead of the total amount of connections. 

## Use

By running:

```
python3 main.py
```

users can choose which map they want to use (Holland or the Netherlands), how many tracks they would like to make, which algorithm they want to use and if relevant, how many times the algorithm should run. 


## Requirements

This code is written in Python 3.7. In requirements.txt all necessary packages are depicted to run the code successfully. To install these packages run: 

```
pip install -r requirements.txt 
```

or conda: 

```
conda install --file requirements.txt
```

## Structure

The list down below explains all folders and their content: 

* /code: Contains all code of the project
* /code/algorithms: Contains the algorithms
* /code/classes: Contains the three classes that form the database
* /code/visualisation: Contains code for visualisation of the solutions using matplotlib
* /data: Contains the data files necessary to fill the database and visualise the map
* /docs: Contains other documents like images and the datastructure.


## Authors 

* Stans Paulussen
* Jari Hoffmann
* Pauline van Lieshout