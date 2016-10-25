# This is an example of implementing a search algorithm using the generic Node and problem class.
# Note that an explored list is not maintained in this version of BFS.

from copy import deepcopy
from collections import deque

from node import Node

def AStar(problem):

	stateRecord = {}

	nodesGenerated = 1
	maxNodesInFrontier = 0

	# Generate the initial (root) node
	node = Node(problem.initial)

	# Record state to avoid looping
	stateRecord[node.getState().evaluate()] = 1

	# For efficiency, we check if the node is a goal state BEFORE putting on the Q
	if problem.isGoal(node.getState()):
		print("Total nodes generated: " + nodesGenerated)
		print("Max nodes in memory: " + maxNodesInFrontier)
		return node

	frontier = []

	# Start queue to hold number of unvisited children at each level
	numChildren = []

	# Continue to expand node and find a next eligible child node until a solution is found
	# or until all possible solutions have been eliminated
	while(True):
		# Generate children and push them onto frontier stack
		children = node.expand(problem)
		for child in children:
			frontier.append(child)
			nodesGenerated += 1
		maxNodesInFrontier = max(maxNodesInFrontier, len(frontier))


		numChildren.append(len(children))

		# Select a child to set as 'node'. Keep iterating until one is found or until we arrive back at the root node (in which case there is no solution)
		while(True):
			# Get number of nodes to pull off of frontier
			childrenInQueue = numChildren.pop()
			numChildren.append(childrenInQueue)

			if childrenInQueue == 0: # No children. Go back to parent node
				if node.depth == 0:
					print("No solution found")
					print("Total nodes generated: " + str(nodesGenerated))
					print("Max nodes in memory: " + str(maxNodesInFrontier))
					return None
				numChildren.pop()
				node = node.parent
				continue

			# Pull nodes off of frontier
			children = []
			for i in range(0,childrenInQueue):
				children.append(frontier.pop())

			# Use heurstic function to determine the most promising child node
			mostPromisingChild = children[0]
			mostPromisingHeuristic = problem.heuristic(children[0].state)

			for child in children:
				if problem.heuristic(child.state) < mostPromisingHeuristic:
					mostPromisingChild = child
					mostPromisingHeuristic = problem.heuristic(child.state)

			# Put the nodes that weren't selected back onto the frontier stack
			for child in children:
				if child != mostPromisingChild:
					frontier.append(child)

			# Decrement top value on stack
			childrenInQueue = numChildren.pop()
			numChildren.append(childrenInQueue - 1)

			node = mostPromisingChild

			# Check if selected child's state is in state record:
			if node.getState().evaluate() in stateRecord:
				# If it is, no need to explore it. Return to parent node
				if node.depth == 0:
					print('No solution found')
					print("Total nodes generated: " + str(nodesGenerated))
					print("Max nodes in memory: " + str(maxNodesInFrontier))
					return None
				node = node.parent

			# Otherwise add selected child's state to state record then BREAK
			else:
				stateRecord[node.getState().evaluate()] = 1

				# Check if we've reached our goal
				# If so, assemble solution
				if problem.isGoal(node.getState()):
					solution = [node.getState().state]
					nodePtr = node
					while nodePtr.depth != 0:
						nodePtr = nodePtr.parent
						solution.append(nodePtr.getState().state)
					solution.reverse()
					print("Total nodes generated: " + str(nodesGenerated))
					print("Max nodes in memory: " + str(maxNodesInFrontier))
					return solution

				break
