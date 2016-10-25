from node import *
from AIproblem import *
from copy import deepcopy

from collections import deque

#being done by David Rolfe for the A

#Performs the Local Beam Search as descibed in the book
#Difference is that it doesn't start with random search states and instead expands from
#the initial state. This fits with the representation of the problems we have better

#Idea is that it runs like A* search except that it only keeps the best k nodes at any one time to reduce memory footprint

# Eval Function is passed through problem 

def astar4nq(problem, k = 20):

	nodesGenerated = 1
	maxNodesInFrontier = 0
	
	#initial node
	node = Node(problem.initial)
	
	#check for if initial node is goal
	if (problem.isGoal(problem.initial)):
		return node
	
	#use priority queue to hold best nodes
	priorityQueue = deque()
	priorityQueue.append((0,node))

	#core loop
	while len(priorityQueue) > 0:

		node = priorityQueue.popleft()[1]

		try:
			for child in node.expand(problem):
				nodesGenerated += 1
				if problem.isGoal( child.getState() ):

					print("Total nodes generated: " + str(nodesGenerated))
					print("Max nodes in memory: " + str(maxNodesInFrontier))

					return child.getState()
				else:
					#evaluates the state
					problem.evaluation(child.getState())
					value = child.getState().value + child.depth
					
					#Adds all the expanded according to the heuristic value
					if len(priorityQueue) > 0:
						for i in range(0,len(priorityQueue)):
							if value < priorityQueue[i][0]:
								priorityQueue.insert(i,(value, child))
								maxNodesInFrontier = max(len(priorityQueue), maxNodesInFrontier)
								break
						else:
							priorityQueue.append((value,child))
							maxNodesInFrontier = max(len(priorityQueue), maxNodesInFrontier)
					else:
						priorityQueue.append((value,child))
						maxNodesInFrontier = max(len(priorityQueue), maxNodesInFrontier)
					#removes the worst nodes until we only have k left 
					# if len(priorityQueue) > k:
					# 	for j in range(k, len(priorityQueue)):
					# 		priorityQueue.pop()
					
							
		except AttributeError:
			pass
	print("failed to find goal state")

	print("Total nodes generated: " + str(nodesGenerated))
	print("Max nodes in memory: " + str(maxNodesInFrontier))

	return None