# Problem: develop a function that determines whether a text has matching parentheses.
# e.g. () is okay but (( is not okay
# input: string, output: boolean

from collections import deque

def check_matching_parentheses(input_text):
    stack = deque()
    for char in input_text:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(check_matching_parentheses("(This is an example)"))
print(check_matching_parentheses("(This (is (an) example))"))

print(check_matching_parentheses("This is an example)"))
print(check_matching_parentheses("(This is an example("))
