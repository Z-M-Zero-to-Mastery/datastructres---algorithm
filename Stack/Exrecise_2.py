# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".

def check_paranthesis(string):
    stack = []
    # Traversing the Expression 
    for i in string:
        # If the exp[i] is a starting parenthesis then push it 
        # eg : (, {, [ 
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if i != ")":
                    return False
            if current_char == "{":
                if i != "}":
                    return False
            if current_char == "[":
                if i != "]":
                    return False
    if stack:
        return False
    return True

string = "{[]{()}}"
