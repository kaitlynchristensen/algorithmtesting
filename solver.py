import sys
import os

sys.path.append('algorithms')
sys.path.append('problems')
sys.path.append( os.path.realpath('..') + '/class-repo/projectClasses' )


from copy import deepcopy
from collections import deque
from genetic import *
from nQueens import *
from bfs import BFS
from simpleProblem import *
from SlidingPuzzleProblem import *
from astar import *
from localbeam import *
from TowerOfHanoiProblem_chen4162 import *
from bidirectional_chen4162 import *
from iterative_deepening_chen4162 import *
from Crossmath import*
from Cryptarithmetic import *
from backtrackingDFS import *
from opDictionary import *
from bfs_striveA_chen4162 import *

#Generic Solver class that everyone should use for their solver
class Solver(object):

  # The input parameters must be as is here
  def __init__( self, testCase, goal=None ):
    self.testCase = testCase
    self.goal = goal
    self.solution = None
    self.userid = 'lars1050' ### PUT THE PERSON WHO WROTE THE ALGORITHM HERE!!
    # This is a good place to create a problem instance.

    # return a solution in the specified format
    # An instance of a solver will be specific to the testCase, thus
    # the details of how to handle it will be hidden inside this method.
    def solve( self ):
      return None

    # print the solution in a user-friendly way
    def printSolution( self ):
      if self.solution:
        print(self.solution)

    # You can modify your solver class in any way, provided that above methods exist



# The result retured by the bidirectional_BFS is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes, the depth of the valid path and all of the valid steps on the valid path (represented by a list of step lists).
class SolverBidirectional(Solver):
    def __init__(self, size, goal=None):
        Solver.__init__(self, size, goal)
        self.userid = 'chen4162'
        
    def solve(self):
        peg1 = deque()
        peg2 = deque()
        peg3 = deque()
        for n in range (0, self.testCase+1):
            peg1.append(n)
        peg2.append(0)
        peg3.append(0)
        peg_set_start = [peg1, peg2, peg3]
        peg_set_end = [peg3, peg2, peg1]

        self.problem_start = TowerOfHanoi(peg_set_start, self.testCase)
        self.problem_end = TowerOfHanoi(peg_set_end, self.testCase)

        self.solution = deepcopy(bidirectional_BFS(self.problem_start, self.problem_end))
        return self.solution

    def printSolution(self):
        print("By using Bidirectional algorithm, the list that includes all states on the valid path from the initial state to the final state is: ", self.solve())

def main():
    n = int(input("Please input the number of disks you want to move in the Tower of Hanoi game: "))
    solver_bidirectional = SolverBidirectional(n)
    solver_bidirectional.printSolution()
    print ("Finished!\n")

'''
if __name__ == "__main__":
    main()
'''

# The result retured by the iterative_deepening is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes and the depth of the valid path.
class SolverIDDFS(Solver):
    def __init__(self, size, goal=None):
        Solver.__init__(self, size, goal)
        self.userid = 'chen4162'
        
    def solve(self):
        self.solution = deepcopy(iterative_deepening(self.testCase))
        return self.solution

    def printSolution(self):
        print("By using Iterative_deepening algorithm, the list that includes all states on the valid path from the initial state to the final state is: ", self.solve())

def main():
    n = int(input("Please input the number of disks you want to move in the Tower of Hanoi game: "))
    solver_IDDFS = SolverIDDFS(n)
    solver_IDDFS.printSolution()
    print ("Finished!\n")
'''
if __name__ == "__main__":
    main()
'''

class SolverGA(Solver):
  # testCase format is integer, representing number of queens
  # SolverGA.solve() returns list of n integers

  
	def __init__(self, testCase, goal = None):
		self.testCase = testCase
		self.goal = goal
		self.solution = None
		self.userid = 'rolf0090'

		def defaultEval(state):
			#counts number of conflicts in the state
			sum = 0
			#counting across columns
			for i in range(1,self.testCase +1):
				num = -1
				for element in state:
					if element == i:
						num = num + 1
				if num > 0:
					sum = sum + num
		
			#counting across diagonals
			for i in range(0, self.testCase):
				for j in range(i+1,self.testCase):
					#flag used to get insure we only get one conflict in each diagonal. Prevents overcounting
					lflag = False
					rflag = False
					diff = j - i
					# in the same diagonal if the difference between the two state numbers is the
					# same as the abs(difference between the space between rows)
					if (state[i] + diff == state[j]) and not(rflag):
						sum = sum + 1
						rflag = True
					if (state[i] - diff == state[j]) and not(lflag):
						sum = sum + 1
						lflag = True
					if lflag and rflag:
						break
		
			return self.testCase*self.testCase - sum	
		
		self.evalFn = defaultEval 
	
		self.population = []
		
		#creates the initial population for the algorithm
		for i in range(0, testCase):
			self.population.append(nQueens(QueenState(randStart(testCase),testCase),testCase,self.evalFn))
		
	def solve( self ):
		self.solution = genetic(self.population, self.evalFn).state.state
		return self.solution
		
	def printSolution( self ):
		if self.solution:
			print(self.solution)

## SolverGA Test Space
##			
##def testSolverGA():
##    print('Testing 4')
##    test4 = SolverGA(4)
##    test4.solve()
##    test4.printSolution()
##
##    print('Testing 6')
##    test6 = SolverGA(6)
##    test6.solve()
##    test6.printSolution()
##
##    print('Testing 8')
##    test8 = SolverGA(8)
##    test8.solve()
##    test8.printSolution()
##
##testSolverGA()


#Local Beam Search for the nQueen Problem
class SolverLBS4nQueen(Solver):
	def __init__(self, testCase, goal = None):
		self.testCase = testCase
		self.goal = goal
		self.solution = None
		self.userid = 'rolf0090'

		def defaultEval(state):
			#counts number of conflicts in the state
			sum = 0
			#counting across columns
			for i in range(1,self.testCase +1):
				num = -1
				for element in state:
					if element == i:
						num = num + 1
				if num > 0:
					sum = sum + num
		
			#counting across diagonals
			for i in range(0, self.testCase):
				for j in range(i+1,self.testCase):
					#flag used to get insure we only get one conflict in each diagonal. Prevents overcounting
					lflag = False
					rflag = False
					diff = j - i
					# in the same diagonal if the difference between the two state numbers is the
					# same as the abs(difference between the space between rows)
					if (state[i] + diff == state[j]) and not(rflag):
						sum = sum + 1
						rflag = True
					if (state[i] - diff == state[j]) and not(lflag):
						sum = sum + 1
						lflag = True
					if lflag and rflag:
						break
		
			return sum	
		
		self.evalFn = defaultEval
		
	def solve(self):
		self.solution = localbeam(nQueens(QueenState([0 for x in range(0,self.testCase)],self.testCase),self.testCase,self.evalFn))
		return self.solution
			
	def printSolution( self ):
		if self.solution:
			print(self.solution)

class SolverAS4nQueen(Solver):
	def __init__(self, testCase, goal = None):
		self.testCase = testCase
		self.goal = goal
		self.solution = None
		self.userid = 'chri2970'

		def defaultEval(state):
			#counts number of conflicts in the state
			sum = 0
			#counting across columns
			for i in range(1,self.testCase +1):
				num = -1
				for element in state:
					if element == i:
						num = num + 1
				if num > 0:
					sum = sum + num
		
			#counting across diagonals
			for i in range(0, self.testCase):
				for j in range(i+1,self.testCase):
					#flag used to get insure we only get one conflict in each diagonal. Prevents overcounting
					lflag = False
					rflag = False
					diff = j - i
					# in the same diagonal if the difference between the two state numbers is the
					# same as the abs(difference between the space between rows)
					if (state[i] + diff == state[j]) and not(rflag):
						sum = sum + 1
						rflag = True
					if (state[i] - diff == state[j]) and not(lflag):
						sum = sum + 1
						lflag = True
					if lflag and rflag:
						break
		
			return sum	
		
		self.evalFn = defaultEval
		
	def solve(self):
		self.solution = astar4nq(nQueens(QueenState([0 for x in range(0,self.testCase)],self.testCase),self.testCase,self.evalFn))
		return self.solution
			
	def printSolution( self ):
		if self.solution:
			print(self.solution)			
			
## Local Beam Search on nQueens test space
##def testSolverLBS4nQueen():
##     print('Testing 4')
##     test4 = SolverLBS4nQueen(4)
##     test4.solve()
##     test4.printSolution()
##
##     print('Testing 6')
##     test6 = SolverLBS4nQueen(6)
##     test6.solve()
##     test6.printSolution()
##
##     print('Testing 8')
##     test8 = SolverLBS4nQueen(8)
##     test8.solve()
##     test8.printSolution()
##
##testSolverLBS4nQueen()		
			
class SolverAS(Solver):

  # The input parameters must be as is here
	def __init__( self, testCase, goal=None ):
		self.testCase = testCase
		self.goal = goal
		self.solution = None
		self.userid = 'chri2970'

    # return a solution in the specified format
    # An instance of a solver will be specific to the testCase, thus
    # the details of how to handle it will be hidden inside this method.
	def solve( self ):
		self.solution = AStar(self.testCase)
		return self.solution

    # print the solution in a user-friendly way
	def printSolution( self ):
		if self.solution:
			count = 1
			for step in self.solution:
				print("Step " + str(count) + ": ")
				for row in step:
					for element in row:
						if element == -1:
							print('x', end=' ')
						else:
							print(element, end=' ')
					print()
				print("_______")
				count += 1

slidingPuzzleTestCase1 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[7,4,1],[5,2,6],[0,3,-1]], 3))
slidingPuzzleTestCase2 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[1,2],[0,-1]], 2))
slidingPuzzleTestCase3 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[-1,0]], 1))

class SolverbckDFS(Solver):

    # The input parameters must be as is here
	def __init__( self, testCase, goal=None ):
		self.testCase = testCase
		self.goal = goal
		self.solution = None
		self.userid = 'caixx269'
	# return a solution in the specified format
	# An instance of a solver will be specific to the testCase, thus
	# the details of how to handle it will be hidden inside this method.
	def solve( self ):
		if isinstance(self.testCase, CrossMathPuzzle ):
			size=len(self.testCase.solution)
			initial=[[0 for i in range(size)] for j in range(size)]
			xmath = Crossmath(initial,[self.testCase.rows,self.testCase.cosl],size)
			ans=bckDFS(xmath)
			if ans:
					self.solution=bckDFS(xmath).getState()
			else:
					self.solution=None
		else:
		# Have not defined a class for cryptarithmetic puzzle yet
			size=max(len(symbol) for symbol in testCase)
			for symbol in puzzle:
				if isinstance(symbol, str):
					operator=symbol
					break
			if '=' in puzzle:
				vertform=False
			elif '|' in puzzle:
				vertform =True
			else:
				print("Invalid input, expecting '=' for horizontal form or '|' for vertical form.")
				self.solution =None
				return None
			crypt=Cryptarithmetic(testCase,operator,size,vertform)
			ans=bckDFS(crypt)
			if ans:
				self.solution=ans.getState()
			else:
				self.solutoin=None                    
		return self.solution
	def printSolution( self ):
		if self.solution:
			if isinstance(self.testCase, CrossMathPuzzle):
				for row in self.solution:
					print(row)
				else:
				# Have not defined a class for cryptarithmetic puzzle yet
					if self.solution:
						print(self.solution)

# Test cases for cryptarithmetic                                     
# puzzle1=[['s','e','n','d'],'+',['m','o','r','e'],'=',['m','o','n','e','y']]
#puzzle2=[['c','o','u','n','t'],'-',['c','o','i','n'],'=',['s','n','u','b']]
#puzzle3=[['w','h','y'],'*',['n','u','t'],'|',['o','o','n','p'],['o','y','p','y'],
#         ['o','u','h','a'],'|',['o','n','e','p','o','p']]
#puzzle4=[['b','u','l','l'],'*',['b','u','s'],'=',['s','o','u','n','d','s']]


# This is the "strive for A" solver.
# The result retured by the bfs is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes and the depth of the valid path.
class SolverBFS(Solver):
    def __init__(self, size, goal=None):
        Solver.__init__(self, size, goal)
        self.userid = 'chen4162'
        
    def solve(self):
        peg1 = deque()
        peg2 = deque()
        peg3 = deque()
        for n in range (0, self.testCase+1):
            peg1.append(n)
        peg2.append(0)
        peg3.append(0)
        peg_set = [peg1, peg2, peg3]

        self.problem = TowerOfHanoi(peg_set, self.testCase)

        self.solution = deepcopy(bfs(self.problem))
        return self.solution

    def printSolution(self):
        print("By using BFS algorithm, the list that includes all states on the valid path from the initial state to the final state is: ", self.solve())

def main():
    n = int(input("Please input the number of disks you want to move in the Tower of Hanoi game: "))
    solver_bfs = SolverBFS(n)
    solver_bfs.printSolution()
    print ("Finished!\n")
'''
if __name__ == "__main__":
    main()
'''
