import random
from phrase import Phrase, target
from helpers import colorize, summarize

popSize = 500   #  initial population size
bestScore = 0   #  keep tab of best fitness of some evolution
generation = 1  #  start @ 1st generation
population = []

#  initialize our population 
for i in range(popSize):
    population.append(Phrase())

#  we run our generations until we evolve a perfect string
while bestScore < len(target):

    #  at every generation, check the fitness of each evolution 
    for i in range(popSize):
        population[i].getFitness()

        #  if new evolution has a better fitness than our bestScore,
        #  set the new fitness as our bestScore and print out the evolution
        if population[i].fitness > bestScore:
            bestScore = population[i].fitness
            summarize(generation, population[i].getContents(), bestScore)

    matingPool = []

    #  at each new generation, copy population over to parents 
    #  and set population to empty list
    parents = population[:]
    population = []


    for i in range(popSize):
        #  if parents[i] fitness is 0, we skip else
        #  we append parents[i] FITNESS times to our matingPool 
        for j in range(parents[i].fitness):
            matingPool.append(parents[i])   #  this will assure to have matingPool packed with the fittest parents

    for i in range(popSize):
        #  x and y has higher chance of picking evolution with a better fitness due to above loop 
        x = random.choice(range(len(matingPool)))   
        y = random.choice(range(len(matingPool)))

        #  we crossover x and y to get a new evolution
        child = matingPool[x].crossover(matingPool[y])
        child.mutate()

        population.append(child)
    
    generation += 1


# for i in range(popSize):
#     print(population[i].getContents()) 