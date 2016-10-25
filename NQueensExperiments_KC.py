import sys
import os

sys.path.append('algorithms')
sys.path.append('problems')
sys.path.append( os.path.realpath('..') + '/class-repo/projectClasses' )

from copy import deepcopy
from collections import deque
from astar import *
from localbeam import *
from nQueens import *
from solver import *

print("A*")
for n in range(4,100):
	print(str(n) + " queens:")
	test = SolverLBS4nQueen(n)
	test.solve()
	print()

for n in range(4,100):
	print(str(n) + " queens:")
	test = SolverAS4nQueen(n)
	test.solve()
	print()
