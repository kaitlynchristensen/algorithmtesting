# Name: Cheng Chen  x500: chen4162
# Team: repo-group-jikadach
# Project_part 1
# Algorithm: iterative_deepening search
# Topic: Tower of Hanoi
# The following class is the iterative_deepening search algorithm class which is created by Cheng Chen.


import itertools
import sys
from copy import deepcopy
from collections import deque
from node_chen4162 import *

# The result retured by the iterative_deepening is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes and the depth of the valid path.
def iterative_deepening(size):
    # A for loop is to make the algorithm iterative.
    for depth in itertools.count():
        # Initial setup for the Tower of Hanoi.
        peg1 = deque()
        peg2 = deque()
        peg3 = deque()
        for n in range (0, size+1):
            peg1.append(n)
        peg2.append(0)
        peg3.append(0)
        peg_set = [peg1, peg2, peg3]
        problem = TowerOfHanoi(peg_set, size)

        # Increase the limit every time.
        result = depth_limited(problem, depth)
        if (result != None):
            return result
    print("For this case, you cannot use the iterative_deepening algorithm to solve the Tower of Hanoi problem.")
    return None
    

def depth_limited(problem, limit):

    # Test if the limit equals zero. If it equals, then return None to indicate a failure.
    if (limit == 0):
        return None
    
    # Generate the initial (root) node
    node = Node(problem.initial)

    # Create some initial lists to be used later, which includes the node's set and the valid states.
    node_set = []
    all_valid_states = [node.getState()]

    # For efficiency, we check if the node is a goal state BEFORE putting on the stack (i.e. from the other side of the deque)
    if problem.isGoal(node.getState()):
        node.setParent(None)
        node.setDepth(0)
        print("The depth of the valid path is: ", 0)
        print("The number of the total nodes are: ", Node.nodeCount)
        return all_valid_states

    # Start the frontier stack by adding the root
    frontier=deque()
    frontier.append(node)

    # Keep searching the tree until there is nothing left to explore or its depth approach the limit(i.e. frontier is empty)
    # OR a solution is found
    while len(frontier) > 0:
        # By using pop function we can regard the deque as a stack (LIFO). By using popleft function we can regard it as a Q (FIFO)
        node = frontier.pop()
        node_set.append(node)

        # If the the depth of the node approaches the limit, then the algorithm stops to expand the node's children. And it just pop the next node in the frontier stack. 
        if (node.getDepth() < limit):
            # POTENTIAL IMPROVEMENT: Use a generator to feed the loop 1 element at a time
            for child in node.expand(problem):
                child.setParent(node)
                child.setDepth(node.getDepth()+1)
                
                if problem.isGoal(child.getState()):
                    for i in range(0, len(Node.old_move_set)):
                        (Node.node_set)[i+1].old_move = (Node.old_move_set)[i]

                    last_node = child
                    temp = []
                    for i in range(0, child.getDepth()):
                        temp.append(last_node.getState())
                        last_node = last_node.getParent()
                        
                    all_valid_states = all_valid_states + temp[::-1]

                    print("Find the solution.")
                    print("The depth of the valid path is: ", child.getDepth())
                    print("The number of the total nodes are: ", Node.nodeCount)
                    return all_valid_states
                frontier.append(child)
            
    # If no solution can be found, return None.
    return None

