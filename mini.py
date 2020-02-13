import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math

'''
Hyperparameters
'''
initial_point = np.matrix([2,3])
final_point = np.matrix([8,9])
max_generations = 100
population = 20
commands = 10

init_north = .25
init_south = .25
init_east = .25
init_west = .25

num_parents = 5



directions = ["north", "south", "east", "west"]
north, south, east, west = np.matrix([0,1]),np.matrix([0,-1]),np.matrix([1,0]),np.matrix([-1,0])
current_pop = [None]*population
current_score = [None]*population


#returns new position after instructions.
def travel(instructions, initial): 
	unique, counts = np.unique(instructions, return_counts=True)
	direction_counts = {"east":0, "west":0, "north":0, "south":0}
	direction_counts.update(dict(zip(unique, counts)))
	return ((direction_counts["east"]*east)+(direction_counts["west"]*west)+(direction_counts["north"]*north)+(direction_counts["south"]*south)+initial)

#distance from traveled point to objective.
def fitness(instructions):
	travel_point = travel(instructions, initial_point)
	return np.linalg.norm(final_point-travel_point)

# generates a new generation of the population.
def generate_pop(north, south, east, west):
	for pop in range(population):
		current_pop[pop] = np.random.choice(directions, commands, p=[north, south, east, west])

#returns fitness score values for each in the population that is passed to it.
def get_score():
	for each in range(population):
		current_score[each] = fitness(current_pop[each])

#returns parents from given population with lowest fitness scores (most fit)
def get_parents():
	return current_pop[np.argpartition(current_score, num_parents)[:num_parents]]
	

#returns new probabilities for next generation based on parents.
def generate_new_prob(parents):
	total = len(parents)*commands
	north, south, east, west = 0
	for each in range(parents):
		east+=parents[each].count("east")
		west+=parents[each].count("west")
		north+=parents[each].count("north")
		south+=parents[each].count("south")
	return north/total, south/total, east/total, west/total
	

#initial generation
generation = 0 
generate_pop(init_north, init_south, init_east, init_west)
#print(current_pop)
get_score()
#print(current_score)
north_p, south_p, east_p, west_p = generate_new_prob(get_parents())
while generation < max_generations:
	generate_pop(north_p, south_p, east_p, west_p)
	get_score()
	north_p, south_p, east_p, west_p = generate_new_prob(get_parents())
	generation+=1


print(current_pop, current_score)



