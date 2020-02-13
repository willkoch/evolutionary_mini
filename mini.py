import random as rand
import numpy as np
import matplotlib.pyplot as plt


#Hyperparameters
initial_point = np.matrix([2,3])
final_point = np.matrix([8,9])
max_generations = 100
min_fitness = 10

east,west,north,south = np.matrix([0,1]),np.matrix([0,-1]),np.matrix([1,0]),np.matrix([-1,0])


while generation < max_generations and fitness > min_fitness:
	




#Define a search space — something simple like integers, binary, reals, vectors, etc. is fine — or your choice!

#2d point in graph, navigating NSEW to get to the goal point. 

#Given two points on a 2d graph of 20x20 coordinates, finding the quickest route from A to B 

print(initial_point+east+north)



#Define an objective function on the search space — something easily implemented in an algorithm.

#number of instructions to reach final_point is the fitness. Less is better.
def fitness(x):
	return len(x)




#Define variation operators on elements of the search space — mutation, recombination, etc., something easily implemented in an algorithm.





#Decide on a selection operator — fitness proportional to the objective function, tournament, rank order, truncation, or your choice.




