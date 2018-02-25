import random
import string
from fuzzywuzzy import fuzz


#creating the template for the individuals that will be evolved
class individual:

    def __init__(self, length):
            #randomly choose a letter until length is reached
        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = 0
            #prints individuals string and fitness
    def __str__(self):
        return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness)

#global measures
in_str = None
in_str_len = None

#number of individuals in the initial population
population = 20

#how many generations to create
generations = 2500

#the genetic algorithm
def ga():

    individuals = init_individuals(population, in_str_len)

    for generation in range(generations):

        print ('Generation: ' + str(generation))
        #all the functions below take individuals as the argument
        individuals = fitness(individuals)
        individuals = selection(individuals)
        individuals = crossover(individuals)
        individuals = mutation(individuals)

        if any(individual.fitness >= 95 for individual in individuals):

               print ('Winner winner chicken dinner')
               exit(0)

#creating the population of individuals    
def init_individuals(population, length):
        
        return [individual(length) for _ in range (population)]

#the objective function
def fitness(individuals):

    for individual in individuals:

        individual.fitness = fuzz.ratio(individual.string, in_str)

    return individuals

def selection(individuals):

        #returns a list of individuals from largest to smallest in order of fitness
    individuals = sorted(individuals, key=lambda agent: agent.fitness, reverse = True)
    print ('\n'.join(map(str, individuals)))
        #takes the top 20 percent of the individuals
    individuals = individuals[:int(0.2 * len(individuals))]

    return individuals

def crossover(individuals):

    offspring = []
    
    for _ in range((population - len(individuals)) // 2):

                    #randomly chooses two parents, crosses over
                   parent1 = random.choice(individuals)
                   parent2 = random.choice(individuals)
                   child1 = individual(in_str_len)
                   child2 = individual(in_str_len)
                   split = random.randint(0, in_str_len)
                   child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
                   child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

                    #adds to the offspring list which is then added to the overall population
                   offspring.append(child1)
                   offspring.append(child2)


    individuals.extend(offspring)

    return individuals


def mutation(individuals):

    for individual in individuals:

        for idx, param in enumerate(individual.string):

            if random.uniform(0.0, 1.0) <= 0.1:

                individual.string = individual.string[0:idx] + random.choice(string.ascii_letters) + individual.string[idx+1:in_str_len]

    return individuals

#refers to file itself
if __name__ == '__main__':

                   in_str = 'JohnFisher'
                   in_str_len = len(in_str)
                   ga()
                   
    
                         
    

    




               

        
