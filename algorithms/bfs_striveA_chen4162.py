# Name: Cheng Chen  x500: chen4162
# Team: repo-group-jikadach
# Project_part 1, Strive for A
# Algorithm: bfs search
# Topic: Tower of Hanoi
# The following class is the bfs search algorithm class which is created by Cheng Chen.


from copy import deepcopy
from collections import deque
from node_chen4162 import *

# The result retured by the bfs is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes and the depth of the valid path.
def bfs(problem):
    # Generate the initial (root) node
    node = Node(problem.initial)

    # Create some initial lists to be used later, which includes the node's set and the valid states.
    node_set = []
    all_valid_states = [node.getState()]

    # For efficiency, we check if the node is a goal state BEFORE putting on the Q (i.e. from the other side of the deque)
    if problem.isGoal(node.getState()):
        node.setParent(None)
        node.setDepth(0)
        print("The depth of the valid path is: ", 0)
        print("The number of the total nodes are: ", Node.nodeCount)
        return all_valid_states

    # Start the frontier Q by adding the root
    frontier=deque()
    frontier.append(node)

    # Keep searching the tree until there is nothing left to explore (i.e. frontier is empty)
    # OR a solution is found
    while len(frontier) > 0:
        # By using pop function we can regard the deque as a stack (LIFO). By using popleft function we can regard it as a Q (FIFO)
        node = frontier.popleft()
        node_set.append(node)
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
    print("Cannot find the meeting node. For this case, you cannot use the bfs algorithm to solve the Tower of Hanoi problem.")
    return None
