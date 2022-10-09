# This function will be given 2 values, x, and y, which will be integers. It will also have two optional values
# op and override. This function is expected to return an integer. Op will be a string representing a mathematical
# operation ('+', '-', '*', '/') to be performed between x and y. If op is not defined it should default to addition.
# Override is a function that accepts two integers and returns an integer as a value. If override is not defined
# it this function should return the result of x and y computed with the op value or there sum if op is not provided.
# If override is specified this function should always return the result of the invocation of override with x
# and y passed into it.

def resultOverrider(x: int, y: int, op: str, override: callable) -> int:
    if override:
        return override(x, y)
    elif not op:
        op = '+'
        if op == '+':
            return x + y
    else:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x - y
        elif op == '/':
            return x // y


resultOverrider(2, 3, '+', None)
