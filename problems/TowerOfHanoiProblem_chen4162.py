# Name: Cheng Chen  x500: chen4162
# Team: repo-group-jikadach
# Project_part 1
# Algorithm: bidirectional_BFS search / iterative_deepening search / bfs search (strive for A)
# Topic: Tower of Hanoi
# The following is the Tower of Hanoi problem class which is created by Cheng Chen to be solved by bidirectional_BFS algorithm and iterative_deepening search algorithm.

# The result retured by the bidirectional_BFS / iterative_deepening is a list that includes all of the states on the valid path from the initial state to the final state.
# In the list descipted above, every state is represented as a list of 3 stacks. Each stack represents a peg. The number in the stack means the disks with different size. 0 means no disk, 1 means the largest. The bigger the number is, the smaller the disk's size is.
# And I also output the number of nodes, the depth of the valid path and all of the valid steps on the valid path (represented by a list of step lists).

from copy import deepcopy
from collections import deque
from AIproblem import AIproblem


class TowerOfHanoi(AIproblem):
    
    def __init__(self, initialState, size):
        AIproblem.__init__(self, initialState, size)

        self.moves_set = [[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]
        self.valid_moves = []
        self.old_move = [0, 0]
        self.old_state_set = [initialState]
        self.state = initialState
        self.final_state = initialState[::-1]

    def getRandomAction( self, state ):
        # randomly produce a single action applicable for this state
        return None

    def getActions(self, state):
        self.state = deepcopy(state)
        move_set_copy = deepcopy(self.moves_set)
        from_peg = deque('0')
        to_peg = deque('0')

        for move in self.moves_set:
            from_peg = deepcopy(self.state[move[0]-1])
            to_peg = deepcopy(self.state[move[1]-1])

            if (len(from_peg)>0 and len(to_peg)>0):
                if (from_peg[-1] > 0):
                    if to_peg[-1] >= from_peg[-1]:
                        move_set_copy.remove(move)
                else:
                    move_set_copy.remove(move)

            helper_state = deepcopy(self.state)
            (helper_state[move[1]-1]).append((helper_state[move[0]-1]).pop())
            if (helper_state in self.old_state_set):
                move_set_copy.remove(move)

        self.valid_moves = deepcopy(move_set_copy)
        return self.valid_moves

    def applyAction(self, state, action):
        self.state = deepcopy(state)
        if (action in self.valid_moves):
            from_peg = self.state[action[0]-1]
            to_peg = self.state[action[1]-1]
            if len(from_peg) > 0:
                to_peg.append(from_peg.pop())
            self.old_move = deepcopy(action)
            self.old_state_set.append(self.state)
            return self.state
        else:
            return None

    def evaluation( self, state ):
        if not self.evalFn :
            return 0
        else :
            state.evaluate( state.evalFn )

    def isGoal ( self, state ):
        # Determine if current state is goal
        if (state == self.final_state):
            return True
        return False
