import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math

'''
Hyperparameters
'''
initial_point = np.matrix([70,47])
final_point = np.matrix([47,30])
max_generations = 100
population = 100
commands = 50

init_north = .25
init_south = .25
init_east = .25
init_west = .25

num_parents = 20



directions = ["north", "south", "east", "west"]
north, south, east, west = np.matrix([0,1]),np.matrix([0,-1]),np.matrix([1,0]),np.matrix([-1,0])
current_pop = [None]*population
current_score = [None]*population
worst_fitness = []
mean_fitness = []
best_fitness = []

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
	parents = []
	for each in np.argpartition(current_score, num_parents)[:num_parents]:
		parents.append(current_pop[each])
	return parents
	

#returns new probabilities for next generation based on parents.
def generate_new_prob(parents):
	total = len(parents)*commands
	north, south, east, west = 0,0,0,0
	for each in range(len(parents)):
		unique, counts = np.unique(parents[each], return_counts=True)
		direction_counts = {"east":0, "west":0, "north":0, "south":0}
		direction_counts.update(dict(zip(unique, counts)))
		east+=direction_counts["east"]
		west+=direction_counts["west"]
		north+=direction_counts["north"]
		south+=direction_counts["south"]
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
	mean_fitness.append(sum(current_score)/len(current_score))
	worst_fitness.append(max(current_score))
	best_fitness.append(min(current_score))


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, sub = plt.subplots()
sub.plot(range(1, max_generations+1), worst_fitness, 'r', label='Worst Fitness')
sub.plot(range(1, max_generations+1), mean_fitness, 'g', label='Mean Fitness')
sub.plot(range(1, max_generations+1), best_fitness, 'b', label='Best Fitness')
legend = sub.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.title(r'\textbf{100 Generation Progression: 20 Parents}', fontsize=11)
plt.xlabel(r'\textbf{Generations}', fontsize=11)
plt.ylabel(r'\textbf{Fitness Score}', fontsize=11)


plt.savefig("100-20.pdf", bbox_inches='tight')

plt.show()

