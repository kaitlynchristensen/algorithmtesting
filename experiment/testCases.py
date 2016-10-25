import sys
import os

sys.path.append('/../')
sys.path.append('/../algorithms')
sys.path.append('/../problems')
sys.path.append( os.path.realpath('..') + '/class-repo/projectClasses' )

from copy import deepcopy
from collections import deque
from SlidingPuzzleProblem import *
from astar import *
from localbeam import *
from TowerOfHanoiProblem_chen4162 import *
from solver import *

size3test1 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[0,4,1],[2,5,3],[-1,7,6]]))
size3test2 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[7,5,0],[3,6,4],[-1,1,2]]))
size3test3 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[5,0,4],[1,6,-1],[2,7,3]]))
size3test4 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[1,-1,7],[3,6,4],[0,2,5]]))
size3test5 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[3,2,-1],[6,1,5],[0,4,7]]))

size4test1 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[13,6,7,9],[5,10,12,11],[0,-1,1,2],[4,14,3,8]]))
size4test2 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[7,10,5,12],[-1,6,9,13],[0,2,11,8],[3,14,1,4]]))
size4test3 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[6,1,10,4],[0,3,7,2],[-1,8,12,14],[11,5,9,13]]))

size5test1 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[4, 0, 10, 14, 22], [21, 8, 20, 7, -1], [23, 15, 3, 11, 12], [18, 16, 17, 2, 9], [13, 6, 5, 1, 19]]))
size5test2 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[18, 5, 12, 21, 15], [11, 14, 8, 20, 1], [-1, 16, 2, 4, 7], [9, 22, 23, 3, 0], [6, 17, 10, 13, 19]]))
size5test3 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[13, 23, 6, 19, 21], [10, 7, 12, -1, 17], [2, 20, 3, 0, 5], [22, 11, 1, 14, 8], [15, 9, 4, 18, 16]]))

solver1 = SolverAS(size3test1)
solver1.solve()