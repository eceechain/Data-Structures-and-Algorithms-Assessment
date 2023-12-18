# balanced_parentheses.py

def is_balanced(expression):
    """
    Checks if the given expression has balanced parentheses, curly braces, and square brackets.
    Returns True if balanced, False otherwise.
    """
    stack = []  # Initialize an empty stack to track opening brackets
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack  # Expression is balanced if the stack is empty at the end


# Testing
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
