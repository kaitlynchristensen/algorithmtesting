# Name: Cheng Chen  x500: chen4162
# Team: repo-group-jikadach
# Project_part 1
# Algorithm: bidirectional_BFS search
# Topic: Tower of Hanoi
# The following class is the bidirectional_BFS search algorithm class which is created by Cheng Chen.


from copy import deepcopy
from collections import deque
from node_chen4162 import *

# The result retured by the bidirectional_BFS is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes, the depth of the valid path and all of the valid steps on the valid path (represented by a list of step lists).
def bidirectional_BFS(problem_start, problem_end):
    # Generate the start and end (root) nodes as the initial nodes.
    node_start = Node(problem_start.state)
    node_end = Node(problem_end.state)

    # Create some initial lists to be used later, which includes the start/end side node's set, both sides' steps and both sides' valid states.
    start_node_set = []
    end_node_set = []
    all_steps = []
    all_steps_start = []
    all_steps_end = []
    all_valid_states = []
    all_valid_states_start = [node_start.getState()]
    all_valid_states_end = [node_end.getState()]

    # For efficiency, we check if the node is a goal state BEFORE putting on the Q (i.e. if the state of the start_side root is equal to the state of the end_side root)
    if node_start.getState() == node_end.getState():
        node_start.setParent(None)
        node_start.setDepth(0)
        node_end.setParent(None)
        node_end.setDepth(0)
        print("Find the meeting node.")
        print("The list of all valid steps on the valid path is: ", all_steps)
        print("The depth of the valid path is: ", 0)
        print("The number of the total nodes are: ", Node.nodeCount)
        return all_valid_states_start

    # Start the frontier Qs by adding the start_side and end_side roots
    frontier_start = deque()
    frontier_start.append(node_start)
    frontier_end = deque()
    frontier_end.append(node_end)
   
    # Keep searching the tree until there is nothing left to explore (i.e. both sides' frontiers are empty)
    # OR a solution is found
    while len(frontier_start) > 0 or len(frontier_end) > 0:

        # By using popleft function we can regard it as a Q (FIFO)
        if len(frontier_start) > 0:
            node_start = frontier_start.popleft()
            start_node_set.append(node_start)

        # By using popleft function we can regard it as a Q (FIFO)
        if len(frontier_end) > 0:
            node_end = frontier_end.popleft()
            end_node_set.append(node_end)

        # Implementing the BFS algorithm from the start side.
        for child_start in node_start.expand(problem_start):
            child_start.setParent(node_start)
            child_start.setDepth(node_start.getDepth()+1)
            
            for node1 in end_node_set:
                if child_start.getState() == node1.getState():

                    for i in range(0, len(Node.old_move_set)):
                        (Node.node_set)[i+2].old_move = (Node.old_move_set)[i]
                      
                    last_node1 = child_start
                    temp_start1 = []
                    for i in range(0, child_start.getDepth()):
                        all_steps_start.append(Node.node_set[Node.node_set.index(last_node1)].old_move)
                        temp_start1.append(last_node1.getState())
                        last_node1 = last_node1.getParent()
                    temp_start1.remove(temp_start1[0])
                    all_valid_states_start = all_valid_states_start + temp_start1[::-1]

                    last_node2 = node1
                    temp_start2 = []
                    for j in range(0, node1.getDepth()):
                        all_steps_end.append((Node.node_set[Node.node_set.index(last_node2)].old_move)[::-1])
                        temp_start2.append(last_node2.getState())
                        last_node2 = last_node2.getParent()
                    all_valid_states_end = temp_start2 + all_valid_states_end
                        
                    all_steps = all_steps_start[::-1] + all_steps_end
                    all_valid_states = all_valid_states_start + all_valid_states_end

                    print("Find the meeting node.")
                    print("The list of all valid steps on the valid path is: ", all_steps)
                    print("The depth of the valid path is: ", child_start.getDepth() + node1.getDepth())
                    print("The number of the total nodes are: ", Node.nodeCount)
                    return all_valid_states
            frontier_start.append(child_start)

        # Implementing the BFS algorithm from the end side.
        for child_end in node_end.expand(problem_end):
            child_end.setParent(node_end)
            child_end.setDepth(node_end.getDepth()+1)
                        
            for node2 in start_node_set:
                if child_end.getState() == node2.getState():

                    for i in range(0, len(Node.old_move_set)):
                        (Node.node_set)[i+2].old_move = (Node.old_move_set)[i]
                      
                    last_node1 = child_end
                    temp_end1 = []
                    for i in range(0, child_end.getDepth()):
                        all_steps_end.append((Node.node_set[Node.node_set.index(last_node1)].old_move)[::-1])
                        temp_end1.append(last_node1.getState())
                        last_node1 = last_node1.getParent()
                    temp_end1.remove(temp_end1[0])
                    all_valid_states_end = temp_end1 + all_valid_states_end

                    last_node2 = node2
                    temp_end2 = []
                    for j in range(0, node2.getDepth()):
                        all_steps_start.append(Node.node_set[Node.node_set.index(last_node2)].old_move)
                        temp_end2.append(last_node2.getState())
                        last_node2 = last_node2.getParent()
                    all_valid_states_start = all_valid_states_start + temp_end2[::-1]
                        
                    all_steps = all_steps_start[::-1] + all_steps_end
                    all_valid_states = all_valid_states_start + all_valid_states_end

                    print("Find the meeting node.")
                    print("The list of all valid steps on the valid path is: ", all_steps)
                    print("The depth of the valid path is: ", node2.getDepth() + child_end.getDepth())
                    print("The number of the total nodes are: ", Node.nodeCount)
                    return all_valid_states
            frontier_end.append(child_end)

    # If no solution can be found, return None.
    print("Cannot find the meeting node. For this case, you cannot use the bidirectional_BFS algorithm to solve the Tower of Hanoi problem.")
    return None

