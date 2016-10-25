# The intent with these search functions is to create a generic framework that can
# be applied to any problem. It should be configured so that you can use both this search and the
# Node class without modification, provided you write problem specific code in the Problem class


class Node:

        nodeCount = 0

        def __init__(self, state,  parent=None, depth=0, action=None):
                self.state = state
                self.depth=depth
                self.parent=parent
                if parent:
                        self.depth = parent.depth + 1

        def expand(self, problem):
                #print('actions:',problem.getActions(self.state))
                #return [ self.makeChild( problem, action) for action in problem.getActions( self.state ) ]
                # The following lines of code in this function are modified to accomodate pruning during applying actions
                for action in problem.getActions( self.state ):
                        child = self.makeChild( problem, action)
                        # Test for none states that come from illegal actions
                        if child.state != None:
                                yield child

        def makeChild(self, problem, action):
                Node.nodeCount += 1
                #if 0 == (Node.nodeCount % 100) :
                #       print( 'nodeCount: ',Node.nodeCount )
                childState = problem.applyAction( self.getState(), action )
                return Node( childState, self, self.depth )

        def getState(self ):
                return self.state

def bckDFS(problem) :
        # Generate the initial (root) node
        node = Node( problem.initial )
        # For efficiency, we check if the node is a goal state BEFORE putting on the Q
        if problem.isGoal( node.getState() ):
                return node

        return recdfs(node, problem)
    
def recdfs(node, problem):
        # The recursive part for DFS
        for child in node.expand(problem):
                if problem.isGoal( child.getState() ):
                        print("Hooray!!")
                        print("It takes only "+str(child.nodeCount)+" nodees to get to the solution")
                        return child
                result=recdfs(child, problem) 
                if result == None:
                        # When all the children failed to satisfy constraints, we need to
                        # undo the current action
                        problem.undoAction(child.parent.getState())
                else:
                        # When the result is not None, we have already found a solution and
                        # thus can just return the value back without continuing the iterations
                        return result
                
        # Getting out of the loop means that all possible values in the domain
        # for children are illegal. We either need to backtrack to the previous step
        # or simply cannot solve the puzzle.
        return None
