#program to check whether the parenthesis are closed or not.
#checking balanced parenthesis with the help of stack
#each time opening parenthesis(brackets) are encountered, it is pushed into stack
#and when closing parenthesis is encountered it is checked with the top of the stacks and pop it out
#if stack is empty - then balanced or unbalanced

open_list = ["(","[","{"]
close_list = [")","]","}"]

#function to check the parenthesis
def check(mystring):
    stack = []
    for i in mystring:
        if i in open_list:
            stack.append(i) #as i has encountered open bracke adding in the stack
        elif i in close_list:
            pos = close_list.index(i) #position = 1 
            if ((len(stack)>0) and (open_list[pos] == stack[len(stack) - 1] )):
                stack.pop()
            else:
                return "unbalanced"
        
    if len(stack) == 0:
        return "balanced"
    else:
        return "unbalanced"
    
string = "(12/2"
print(check(string))
