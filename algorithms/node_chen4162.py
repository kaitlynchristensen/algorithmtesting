# Name: Cheng Chen  x500: chen4162
# Team: repo-group-jikadach
# Project_part 1
# Algorithm: bidirectional_BFS search / iterative_deepening search / bfs search (strive for A)
# Topic: Tower of Hanoi
# The following is the Node class which is created by Cheng Chen to be used in the bidirectional_BFS and iterative_deepening search algorithms applying to the Tower of Hanoi problem.


# The result retured by the bidirectional_BFS / iterative_deepening is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes, the depth of the valid path and all of the valid steps on the valid path (represented by a list of step lists).

from copy import deepcopy
from TowerOfHanoiProblem_chen4162 import *

class Node(object):

	nodeCount = 0
	old_move_set = []
	node_set = []

	def __init__( self, state, parent=None, action=None ) :
		self.state = state
		Node.nodeCount += 1
		Node.node_set.append(self)
		self.parent = parent
		self.depth = 0
		self.old_move = action

	def expand( self, problem ) :
		return [ self.makeChild( problem, action) for action in problem.getActions( self.state ) ]

	def makeChild( self, problem, action ) :
		childState = (problem.applyAction( self.state, action ))
		Node.old_move_set.append(problem.old_move)
		return Node( childState )

	def getState( self ) :
		if (self == None):
			return None
		return self.state

	def setDepth(self, depth):
		self.depth = depth

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		if (self == None):
			return None
		return self.parent

	def getDepth(self):
		if (self == None):
			return 0
		return self.depth
