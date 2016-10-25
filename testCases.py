import sys
import os

sys.path.append('algorithms')
sys.path.append('problems')
sys.path.append( os.path.realpath('..') + '/class-repo/projectClasses' )

from copy import deepcopy
from collections import deque
from SlidingPuzzleProblem import *
from astar import *
from localbeam_kc import *

size3test5 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[3,2,-1],[6,1,5],[0,4,7]],3))
size3test6 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[-1, 7, 4], [2, 0, 6], [5, 1, 3]],3))
size3test8 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[4, 7, -1], [3, 0, 6], [2, 5, 1]],3))

size4test1 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[13,6,7,9],[5,10,12,11],[0,-1,1,2],[4,14,3,8]],4))
size4test2 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[7,10,5,12],[-1,6,9,13],[0,2,11,8],[3,14,1,4]],4))
size4test3 = SlidingPuzzleProblem(SlidingPuzzleProblemState([[6,1,10,4],[0,3,7,2],[-1,8,12,14],[11,5,9,13]],4))

print("A*")
print("3x3 puzzles")
AStar(size3test5)
AStar(size3test6)
AStar(size3test8)

print("4x4 puzzles")
AStar(size4test1)
AStar(size4test2)
AStar(size4test3)

print("Local Beam")
print("3x3 puzzles")
LocalBeamKC(size3test5)
LocalBeamKC(size3test6)
LocalBeamKC(size3test8)

print("4x4 puzzles")
LocalBeamKC(size4test1)
LocalBeamKC(size4test2)
LocalBeamKC(size4test3)




