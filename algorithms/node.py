
from AIproblem import *

class Node(object):

	nodeCount = 0
	recordPath = True

	def __init__( self, state, parent=None, action=None ) :
		self.state = state

		# makeChild always passes self as parent, thus a static class flag
		# is being used to indicate whether it needs to be kept or not.
		# Set flag in AIproblemClass with Node.recordPath = True
		if ( Node.recordPath ) :
			self.parent = parent
		else :
			parent = None
		self.depth = 0
		Node.nodeCount += 1
		if parent:
			self.depth = parent.depth + 1

	def expand( self, problem ) :
		return [ self.makeChild( problem, action) for action in problem.getActions( self.state ) ]

        # Added the passing of self for parent information, including depth
	def makeChild( self, problem, action ) :
		childState = problem.applyAction( self.state, action )
		return Node( childState, self )

	def getState( self ) :
		return self.state