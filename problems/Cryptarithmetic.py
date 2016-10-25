# Problem class for cryptarithmetic involes only one operation
# The action is defined as substituing one letter with a number at a time
# The aciton is taken in the order from the lowest digit to the highest
# from the number on top (vertical form) or left (horizontal from) to the number on bottom or right

from AIproblem import *
from opDictionary import ops
from copy import deepcopy

class Cryptarithmetic(AIproblem):
    def __init__(self,initialState, operator, size, vertform, evalFn=None, goal=None):
        AIproblem.__init__(self, initialState, size, evalFn, goal)
        self.domains={ i for i in range(10)}
        # size is defined as the length of the number with most digits
        self.op=operator
        self.vertform=vertform # True for vertical form, false for horizontal form
        # actions is the list that stores the executed actions
        self.actions=[]

    def getActions(self,state):
        
        # Traverse the characters in each number backwards, thus from the lowest digit to the highest digit
        # i.e. array[-1] is the last element of the list, array[-2] is the second to the last and so on 
        for i in range(1,self.size+1):
            # Traverse the symbols from top (left) to bottom (right)
            for n,symbol in enumerate(state):
               # Exclude the operators
               if isinstance(symbol,list):
                    # Exclude those numbers with shorter lengths
                    if i<=len(symbol):
                        # Apply action only to letters
                        if self.vertform:
                            # Need to account for the differnce in starting column for vertical form
                            if n>4 and n<len(state)-1:
                                j=i+4-n
                                if j<=0:
                                    continue
                            else:
                                j=i
                        else:
                            j=i
                        if isinstance(symbol[-j],str):
                            domain=self.domains
                            # Exclude 0 from the domain for the highest digit
                            if j==len(symbol):
                                domain=self.domains-{0}
                            # the actions are all the possible choices of numbers for this letter
                            # The action is denoted in the form (letter, number)
                            return [(symbol[-j],num) for num in domain]

    def applyAction(self, state, action):
        # Update the actions and domains before applying
        self.actions.append((action[0],action[1]))
        self.domains-={action[1]}
        # Iterate through the symbols in state
        for symbol in state:
            # Exclude the operators
            if isinstance(symbol,list):
                # Iterate through the list
                for i,el in enumerate(symbol):
                    # Replace the target letter with the given number in action
                    if el==action[0]:
                        symbol[i]=action[1]
        if self.constraints(state):
            return state
        else:
            self.undoAction(state)
            return None          
                            
    # The function to check for constraints in the curernt state                
    def constraints(self, state):
        # operands are the number on the left(top)/right(bottom) of the operator, list2str converts
        # them to string representations and stops before a letter thus contains only numberin the string. If the lowest digit is already
        # a letter then returns empty string
        operands=[self.list2str(state[i]) for i in [0,2]]
        if any([not operand for operand in operands]):
            # If one of the lowest digits is still letter then skip the case
            return True
        
        # For the case of vertical multiplication, we also need to consider the intermiediate results from
        # multiplying the digits in bottom operand with the value of the top of operand respectively
        if self.op=='*' and self.vertform:
            ans=[]
            results=[]
            # Carry out the operation digit by digit
            for d,digit in enumerate(list(reversed(operands[1]))):
                # Calculate the intermidiatre results for each digit in bottom operand
                results.append(str(int(digit)*int(operands[0])))
                if len(str(operands[0]))==len(state[0]):
                    # If all the digits in top operand are filled then check all the digits
                    ans.append(state[d+4])
                    if len(results[-1])!=len(ans[-1]):
                        # If the length of the result does not match that in the puzzle then constraints are not satisified
                        return False
                else:
                    # Calculate the index that corresponds to the length of the top operand
                    idx=-1*len(str(operands[0]))
                    # Truncate the lists to the corresponding size
                    results[-1]=results[-1][idx:]
                    ans.append(state[d+4][idx:])
                    if len(results[-1])<-idx:
                        # The length of result being shorter implies that idx is out of range in result, and thus we negelct some
                        # leading 0s. Now supplement the omitted 0s
                        results[-1]='0'*(-idx-len(results[-1]))+results[-1]

                if not self.compare(results[-1],ans[-1]):
                    return False
                
            # Getting out of the loop means that all intermediate results are consistant with the operations
            # Then we need to check whether they add up to the final answer
            # Update the results to reflect the different starting digit place in vertical multiplications
            
            newresults=[num+'0'*i for i, num in enumerate(results)]
            if len(operands[1])==len(state[2]) and len(operands[0])==len(state[0]):
                # If all the digits in the operands are complete then we can check all the digits in final answer
                finresult=sum([int(num) for num in newresults])
                finans=state[-1]
                return self.compare(str(finresult),finans)
            
            elif len(operands[1])==len(state[2]):
                # If only the bottom operand is completed, then letters that can affect the results are only in top operand
                # Thus the maximum length of the determined numerical result has the length of top operand
                idx=-1*len(operands[0])
            elif len(operands[0])==len(state[0]):
                # Similarly if only the top operand is completed, we only need to check to the digit corresponds to the bottom
                # operand
                idx=-1*len(operand[1])
            else:
                # Otherwise we just need to keep the length corresponds to the shorter operand
                idx=-1*min(len(operands[0]),len(operands[1]))
                
            finresult=sum([int(num[idx:]) for num in newresults])
            finans=state[-1][idx:]
            
            # Convert to string type
            finresult=str(finresult)
            # Check for ommision of leading 0s
            if len(finresult)<len(finans):
                # Append the missing 0s
                finresult='0'*(len(finans)-len(finresult))+finresult
            return self.compare(finresult,finans)
            
        # The generic case is straight forward. We just need to calculate the numeric result from the operands and
        # compare the result with the list representation in the puzzle digit by digit
        else:
            # value is the numeric value from the calculation
            value=ops[self.op](int(operands[0]),int(operands[1]))
            # Check for the subtraction with borrow case
            if value<0:
                # The vaule to borrow is just 10^n with n=#of digits (not including minus sign)
                value+=10**(len(str(value))-1)
            result=str(value)
            if len(operands[0])==len(state[0]) and len(operands[1])==len(state[2]):
                # if both the operands are complete, we can now check all the digits
                ans=state[4]
                # Before apllying the test digit by digit, we should rule out the case where result and ans have different lengths
                if len(result)!=len(ans):
                    return False
            else:
                # Otherwise, we only need to check the segment of ans that correpsonds to the length of shortest operands since higher digits
                # will involve yet defined letters
                # Calculate the index to represent the place of the highest digit of the shortest operands
                idx=-min([len(operand) for operand in operands])
                # Check whether this index is in the bound of the string
                if len(result)<-1*idx:
                    # result shorter than the indices means that some digits are ignored in the string representation. According to the general
                    # rule of arithmetic, the only possible case is when we have leading 0s. Then we need to supplement all the neglected 0s
                    result='0'*(-1*idx-len(result))+result
                else:
                    # Otherwise just extract the corresponding segment 
                    result=result[idx:]
                ans=state[4][idx:]
                
            return self.compare(result,ans)
                                     
    # compares the string representations result with list representation ans digit by digit
    def compare(self, result, ans):
        # Iterate from lowest digit
        for i in range(len(ans)):
            # We only check the integer elements and skip the letter elements
            # Iterate from lowest to highest
            if isinstance(ans[-i-1],int):
                if ans[-i-1]!=int(result[-i-1]) :
                    return False
            # Getting to the else block means that the digit is still a letter and we can skip the case
            else:
                return True
        # Getting out of the loop means that all digits in result agree with answer
        return True
    
    # The function that converts a list representation to numerical value
    def list2str(self,l):
        s=""
        # Iterate through the digits from the lowest to the highest
        for i,digit in enumerate(list(reversed(l))):
            if isinstance(digit,int):
                s=str(digit)+s
            else:
                # Stops upon the encounter of a letter
                break
        # Return empty string if the lowest digit is a letter
        return s

    
    def undoAction(self,state):
        # Pop it form the actions list
        action=self.actions.pop()
        # Update the domains
        self.domains|={action[1]}
        # Iterate through the symbols in state
        for symbol in state:
            # Exclude the operators
            if isinstance(symbol,list):
                # Iterate through the list
                for i,el in enumerate(symbol):
                    # Replace the target number with the given letter in action
                    if el==action[1]:
                        symbol[i]=action[0]

    def isGoal(self, state):
        # If there is unassigned letters in the puzzle, then we haven't finished
        # Iterate through the symbols in state
        for symbol in state:
            # Exclude the operators
            if isinstance(symbol,list):
                # Check whether there is any string type element in symbol
                if any(isinstance(el,str) for el in symbol):
                    return False
        # Getting out of the loop means that the puzzle is completely filled
        # Then we can just check whether the numerical values agree with the operations
        return self.constraints(state)
