# The n Queens Problem 


from AIproblem import *
from random import *
from copy import deepcopy

#Produces a random start for the n queens
#Done so that you don't have duplicated in rows or columns
def randStart(size):
	
	possibilityList = [ num for num in range(1,size +1)]
	
	outList = []
	
	#chooses random rows from the list and adds them to the output list
	while (len(possibilityList) != 0):
		choice = randint(0,len(possibilityList)-1)
		outList.append(possibilityList[choice])
		possibilityList.pop(choice)
	
	return outList
		

class nQueens(AIproblem):
	#if doing normal search this expects to not have any intial state
	#empty rows represented by 0s
	def __init__(self, initial = None, size = 8, evalFn = None):
		if initial == None:
			self.state = ProblemState([ 0 for x in range(0,size) ],size)
		else:
			self.state = initial
		self.initial = self.state
		self.size = size
		#generates all possible row changes
		self.actions = [ x for x in range(1,size+1)]
		self.evalFn = evalFn
	
	def getActions(self,state):
		#Gets all possible actions
		#this is all actions that can be applied to the first empty row
		actions = []
		
		for x in range(0,self.size):
			if state.state[x] == 0:
				for y in self.actions:
					actions.append([x,y])
				break

		
		return actions	
		
	def getRandomAction(self,state):
		#gets a random action
		return [randint(0,self.size - 1),randint(1,self.size)]
		
	def applyAction(self,state,action):
		#applies the given action to the 
		
		newState = deepcopy(state)
		
		newState.state[action[0]] = action[1]
		
		return newState

	def reproduce(self, state):
		#produces a new state based on the current state and an input state
		
		#state.state is used to only pass on a QueenState to the reproduce function
		return nQueens(self.state.reproduce(state.state), self.size, self.evalFn)
		
	def evaluation( self, state ):
		if not self.evalFn :
			return 0
		else :
			state.evaluate( self.evalFn )
			return state.value
		
	def combine(self):
		
		return False
	
	def isGoal(self,state):

		return (state.isGoal())
	
class QueenState(ProblemState):
		def __init__( self, state, size, value=0 ):
			self.state = state
			self.value = value
			self.size = size
			
		def conflicts(self):
			#counts number of conflicts in the state
			sum = 0
			#counting across columns
			for i in range(1,self.size +1):
				num = -1
				for element in self.state:
					if element == i:
						num = num + 1
				if num > 0:
					sum = sum + num
		
			#counting across diagonals
			for i in range(0, self.size):
				for j in range(i+1,self.size):
					#flag used to get insure we only get one conflict in each diagonal. Prevents overcounting
					lflag = False
					rflag = False
					diff = j - i
					# in the same diagonal if the difference between the two state numbers is the
					# same as the abs(difference between the space between rows)
					if (self.state[i] + diff == self.state[j]) and not(rflag):
						sum = sum + 1
						rflag = True
					if (self.state[i] - diff == self.state[j]) and not(lflag):
						sum = sum + 1
						lflag = True
					if lflag and rflag:
						break
		
			return sum
		
		def reproduce(self, state):
			#creates the combined state
			split = randint(1,len(self.state))
			outState = []
			
			for i in range(0, split):
				outState.append(self.state[i])
			
			for i in range(split, len(self.state)):
				outState.append(state[i])
			
			return QueenState(outState,self.size, 0)
		
		def evaluate( self, evalFn ):
			self.value = evalFn( self.state )
		
		def isGoal(self):
			#check if everything is filled in
			for i in self.state:
				if (i == 0):
					return False
			
			#is goal if no conflicts
			return (self.conflicts() == 0)
		
		def __str__( self ) :
			# Converts the state representation to a string (nice for printing)

			return str(self.state)
'''			
def test(size):
	test = randStart(size)
	print(test)
	state = QueenState(test,size)
	print(state)
	print(state.conflicts())
	
test(4)
'''
