# This is an example of implementing a search algorithm using the generic Node and problem class.
# Note that an explored list is not maintained in this version of BFS.

from copy import deepcopy
from collections import deque

from node import Node

def BFS( problem) :

	# Generate the initial (root) node
	node = Node( problem.initial )

	# For efficiency, we check if the node is a goal state BEFORE putting on the Q
	if problem.isGoal( node.getState() ):
		return node

	# Start the frontier Q by adding the initial root node
	frontier=deque()
	frontier.append(node)

	# Keep searching the tree until there is nothing left to explore (i.e. frontier is empty)
	# OR a solution is found
	while len(frontier) > 0:
		node = frontier.popleft()
                # This will catch a call to node.expand when the child is an empty list.
                # An empty child might occur if an action is pruned away, thus no node is created.
                # It also catches a call to isGoal on an empty list (it should have its own try though)
		try:
			# POTENTIAL IMPROVEMENT: Use a generator to feed the loop 1 element at a time
			for child in node.expand(problem):
                                if problem.isGoal( child.getState() ):
                                        return child
                                else :
                                        frontier.append(child)
		except AttributeError:
                        pass
	return None
