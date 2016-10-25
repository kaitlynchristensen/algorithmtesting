#Generic Problem Class. Will be inherited and modified by all problems
#Lays out standard structure so problems can be used by multiple solving algorithms

from AIproblem import *
from copy import deepcopy

class SlidingPuzzleProblemState(ProblemState):
	def __init__(self, state, size, evalFn=True, value=0):
		ProblemState.__init__(self, state, size, value)
		self.evalFn = evalFn

	def evaluate(self, evalFn=None): # encodes state to a unique integer
		self.value = 0
		digits = len(str(len(self.state) * len(self.state[0])))
		index = 0

		for row in range(len(self.state)):
			for col in range(len(self.state[0])):
				self.value += (self.state[row][col] + 1) * 10**(index * digits)
				index += 1

		return self.value

	def isGoal(self):
		index = 0
		for x in range(len(self.state)):
			for y in range(len(self.state[0])):
				if self.state[x][y] != index and index != len(self.state) * len(self.state[0]) - 1:
					return False
				index = index + 1

		return True

	# def heuristic(self, state):
	# 	actions = self.getActions(state)

	# 	if actions == null:
	# 		return null

	# 	bestAction = actions[0]
	# 	bestActionDist = 0

	# 	for (row, col, direction) in actions:
	# 		value = state[row][col]
	# 		destRow = value / len(state)
	# 		destCol = value - (destRow) * len(state[0])

	# 		if abs(destRow - row) + abs(destCol - col) > bestActionDist:
	# 			bestAction = (row, col, direction)
	# 			bestActionDist = abs(destRow - row) + abs(destCol - col)

	# 	return bestAction

	def __str__(self):
        # Converts the state representation to a string (nice for printing)
		printString = ''
		for r in self.state:
			printString = printString + str(r) + '\n'
		return printString


class SlidingPuzzleProblem(AIproblem):
	def __init__(self, initialState):
		self.initial = initialState
	
	def getActions(self, state):
		emptyLocRow = -1
		emptyLocCol = -1
		# find empty location
		for row in state.state:
			if -1 in row:
				emptyLocRow = state.state.index(row)
				emptyLocCol = row.index(-1)
				break

		if emptyLocRow == -1:
			return "Bad State Puzzle State: one value must be 'empty' (contain -1)"

		actions = []

		if emptyLocCol < len(self.initial.state[0]) - 1:
			actions.append((emptyLocRow, (emptyLocCol + 1), 'l'))
		if emptyLocCol > 0:
			actions.append((emptyLocRow, (emptyLocCol - 1), 'r'))
		if emptyLocRow < len(self.initial.state) - 1:
			actions.append(((emptyLocRow + 1), emptyLocCol, 'u'))
		if emptyLocRow > 0:
			actions.append(((emptyLocRow - 1), emptyLocCol, 'd'))
		
		return actions

	def applyAction(self, state, action):
		(row, col, direction) = action

		newState = deepcopy(state)

		if direction == 'r':
			newState.state[row][col + 1] = newState.state[row][col]
		elif direction == 'l':
			newState.state[row][col - 1] = newState.state[row][col]
		elif direction == 'u':
			newState.state[row - 1][col] = newState.state[row][col]
		else: # direction == 'd'
			newState.state[row + 1][col] = newState.state[row][col]

		newState.state[row][col] = -1

		return newState
		
	def isGoal(self, state):
		return state.isGoal()

	def heuristic(self, state):
		sum = 0
		for row in range(len(state.state)):
			for col in range(len(state.state[row])):
				val = state.state[row][col]
				destRow = val / len(state.state)
				destCol = val - (destRow) * len(state.state[0])
				sum += abs(destRow - row) + abs(destCol - col)
		return sum

	def evaluation(self, state):
		state.evaluate()

