# This example is a simplistic "puzzle" in which the objective is to fill an nxn grid
# such that each row and each column contains exactly 1 instance of each of the numbers 1-n.
# It is a demonstration of how to code a puzzle solver using a generic BFS framework,
# as well as the generic classes of ProblemState and AIproblem

from copy import deepcopy

from AIproblem import *

class SimpleProblemState( ProblemState ):
  
        def __init__( self, state, size, value=0 ) :
                # Using attributes and initialization from parent class ProblemState
                ProblemState.__init__( self, state, size, value )

        def isFilled( self ) :
                # Determines if the puzzle is completely filled, which is indication
                # that no more actions are legal and it might be a solution.
                # If have n rows and n columns, all filled.
                if ( self.size == len( self.state) ):
                        if ( len( self.state[self.size-1]) == self.size ):
                                return True
                return False

        def fillNextBox( self, element ) :
                # This puzzle works by appending to the end of the list, forming a new row as needed.
                # This logic is specific to the state representation for this puzzle.
                flat = flatten(self.state)
                idx = len(flat)
                row = idx // self.size
                col = idx % self.size
                # if it is the first element of a new row, the number is added as a list
                if ( 0 == col ):
                        self.state.append( [element] )
                else :
                        self.state[row].append( element )
                        
        def isGoal( self ) :
                # Checking for a goal state is specific to the state representation for this puzzle.
                # In other puzzles, one might need only compare the current state to a provided goal state.

                # If the state is empty, not done yet
                if not self.isFilled():
                        return False

                # We have a completely filled in board. Check if there are any
                # duplicates across columns or rows
                for row in self.state :
                        if len(list(set(row))) < self.size :
                                return False
                for col in range(self.size):
                        if len( list(set([ row[col] for row in self.state ] ) )) < self.size :
                                #print('State ',state,' not goal')
                                return False
                        
                # If we got here, the board is complete and legal
                return True

        def __str__( self ) :
                # Converts the state representation to a string (nice for printing)
                printString = ''
                for r in self.state :
                  printString = printString + str(r) + '\n'
                return printString
              

class SimpleProblem(AIproblem):
        def __init__(self, initial, size, evalFn=None, goal=None):
                # Using the attributes and initialization of the AIproblem class
                AIproblem.__init__( self, initial, size, evalFn, goal )

                # For this example, an action is the filling in of a single box
                # thus, the set of legal actions for all states is all numbers 1 to n
                self.actions = [ i for i in range(1,self.size+1) ]
                
        def getActions( self, state ) :
                # Because all actions are legal for this example, they were generated once
                # in init, then are passed along here.
                # It might be that you generate only legal actions here, OR you generate all
                # actions, then test for legality in applyAction()
                if state.isFilled():
                        return []
                return self.actions

        def applyAction ( self, state, action ) :
                # It is very important that you generate a new variable with deepcopy for the new state
                # This code is problem specific. An action is applied by adding a number to the next box
                newState = deepcopy(state)
                newState.fillNextBox( action )
                return newState

        def isGoal ( self, state ):
                # This puzzle does not have a predefined goal state, thus passing along the task of
                # determining if this state is a goal state to the state itself. Note that then you could
                # change the way you represent a state and this can remain unchanged.
                return state.isGoal()

# This flattens a singly nested list.
def flatten( Alist ):
	z = []
	for el in Alist:
		z.extend(el)
	return z





