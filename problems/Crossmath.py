# Problem class for Cross Math
# The action is defined as filling one block at a time
# The action is taken in the order form left to right from top to bottom in the puzzle

from AIproblem import *
from opDictionary import ops
from copy import deepcopy

class CrossMath(AIproblem):
    def __init__(self, initialState, rules, size, evalFn=None, goal=None):
        AIproblem.__init__(self, initialState, size, evalFn, goal)
        self.rules=rules
        # Create two matrices to store the partial results for all the steps in
        # row and column operations respectively
        self.partialResults=[deepcopy(initialState)for i in range(2)]
        # Intiailize the domain as all the numbers from 1 to n^2
        self.domains={ i for i in range(1, size**2+1)}
        # Initialize the index for the block to fill
        self.idx= (0,0)

    def constraints(self, X, Y):
        # X and Y are the pairs of indices for the blocks
        # We do not need to check whether they are the same since getActions guarantee no repetitons
        # Check whether the two numbers are in same row or column
        for i in range(2):
            
            if X[i]==Y[i]:
                # Check whether the latter element is the end of row or column
                if X[not i]==self.size-1:
                    # Check whehter we obtained the number at the end of this row or column
                    return self.partialResults[i][X[0]][X[1]] == self.rules[i][X[i]][1]
                # Repeat the same condition checking for X
                elif Y[not i]==self.size-1:    
                     # Check whehter we obtained the number at the end of this row or column
                    return self.partialResults[i][Y[0]][Y[1]] == self.rules[i][Y[i]][1]
            
        return True
            
    def getActions(self,state):
        # the actions are all the possible choices of numbers to be filled in this block
        return [num for num in self.domains]
    
    def applyAction(self, state, action):
        r, c = self.idx
        
        # Iterate through rows then columns
        for i in range(2):
            # Check if the block is the start of a column or row
            if self.idx[i]==0:
                # If so we don't need to check for the constraints in the column/row
                self.partialResults[not i][r][c]=action
            else:
                # Find the indices for the preceding block in the column/row
                rprev=r-(i==0)
                cprev=c-(i==1)
                # Get the corresponding opertor between the blocks
                op=self.rules[not i][self.idx[not i]][0][self.idx[i]-1]
                # The partial result is calculated from the block and the preceding block with the
                # corresponding operation
                self.partialResults[not i][r][c]=ops[op](self.partialResults[not i][rprev][cprev],action)
                # Check whether the constraint is satisified
                if not self.constraints((rprev,cprev), self.idx):
                    return None
        # Getting out of the block means that constraints are satisified
        # Update State,domain and index
        state[r][c]=action
        self.domains-={action}
        r+=(c+1)//self.size
        c=(c+1)%self.size
        self.idx = (r,c)
        return state
    
    def undoAction(self, state):
        # Shift the index back to previous step
        r,c=self.idx
        r+=(c-1)//self.size
        c=(c-1)%self.size
        # Update the domain to again include the number removed from the puzzle
        self.domains|={state[r][c]}
        # Reset the value at the block back to 0
        state[r][c]=0
        self.idx=(r,c)

    def isGoal (self, state):
        # If there is unfilled block, then we haven't finished
        for row in state:
            if 0 in row:
                return False
        return True
