

from node import *
import random
from copy import deepcopy


def weightedRandom(list, weightList):
	#Chooses a random element of a list based on its associated weight list
	total = sum(weightList)
	randnum = random.uniform(0,total)
	current = 0
	for i in range(0,len(list)):
		if current + weightList[i] >= randnum:
			return list[i]
		current = current + weightList[i]
		
	#Should never reach here.
	return []

#Genetic Algorithm based on book psuedocode

# NOTE FOR SELF
# NEED to redo code to better respect modularity. Other problems will work with a little modification but could be better

def genetic(problemPop, evalFn, genLimit = 10000000, mutationProb = 0.05):
	#Will stop after (default) 2500 generations or when it finds the goal state
	currentPop = problemPop
	
	for i in range(0,genLimit):
		#print(i)
		newPop = []
		
		for problem in currentPop:
			if problem.evaluation(problem.state) == 0:
				#This should never be called
				#Indicates that no evalFn was supplied
				return None
		
		fitnessVals = [ problem.state.value for problem in currentPop ]
		
		for j in range(0, len(currentPop)):
			parentA = weightedRandom(currentPop, fitnessVals)
			parentB = weightedRandom(currentPop, fitnessVals)
			
			child = parentA.reproduce(parentB.state)
			
			if (random.uniform(0,1) <= mutationProb):
				child.state = child.applyAction(child.state, child.getRandomAction(child.state))
				
			newPop.append(deepcopy(child))
			
		currentPop = deepcopy(newPop)
		
		#Fitness limit for stopping is having attained goal state
		for x in currentPop:
			if x.isGoal(x.state):
				#print("Finished on Genereation ", i)
				return x
				
	#finding fittest state to return
	current = None
	currentVal = -1
	
	for i in range(0,len(currentPop)):
		currentPop[i].evaluation
		compare = currentPop[i].state.value
		if compare > currentVal:
			current = currentPop[i]
			currentVal = compare
	
	return current
			
