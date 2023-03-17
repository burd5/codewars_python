"""

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

"""

# my solution

def valid_parentheses(paren_str):
    stack = []
    for parenth in paren_str:
        if parenth == '(':
            stack.append('(')
        elif parenth == ')' and len(stack) == 0:
            return False
        else:
            stack.pop()
            
    return len(stack) == 0

# clever solution

def valid_parentheses(x):
    while "()" in x:
        x = x.replace("()", "")
    return x == ""