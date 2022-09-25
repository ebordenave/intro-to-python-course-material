def functionSolver(function: callable) -> str:
    """If the summation of the values in the function are equivalent to the result of the given arguments then return"""
    # an addition string
    if function(1, 1) == 2.0 and function(2, 3) == 5.0 and function(4, 1) == 5.0:
        return '+'
    # If the difference of the values in the function are equivalent to the result of the given arguments then return
    # a subtraction string
    elif function(1, 1) == 0.0 and function(2, 3) == -1.0 and function(4, 1) == 3.0:
        return '-'
    # If the product of the values in the function are equivalent to the result of the given arguments then return a
    # subtraction string
    elif function(1, 1) == 1.0 and function(2, 3) == 6.0 and function(4, 1) == 4.0:
        return '*'
    # else the string is division
    return '/'


def nestedRemoval(text: str, leftPattern: str, rightPattern: str) -> str:
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    removed_list = []
    # Temporarily store indices
    temp_list = []
    # For each element in x range, x is the length of the text do the following
    for i in range(len(text)):
        # initialize var s and assign the value of the text string at the index
        s = text[i]
        if s is leftPattern:
            # if s is equal to the leftPattern, append element to temporary list
            temp_list.append(i)
        elif s is rightPattern:
            # if s is equal to the rightPattern
            if len(temp_list) > 0 and text[temp_list[-1]] is leftPattern:
                # if the length of the temporary list is greater than 0 and the index of the temp list minus 1 is
                # equal to the left pattern
                removed_list.append(temp_list[-1])
                removed_list.append(i)
                temp_list = temp_list[:-1]
            else:
                temp_list.append(i)
    ans = ''
    for i in range(len(text)):
        if i not in removed_list:
            ans = ans + text[i]

    return ans


def productSum(x: int, y: int, z: int) -> int:
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    if x * y < z:
        # if the product of x times y is less than the value of z
        product_xy = x * y
        # assign the product value to the variable named product_xy
        return product_xy
    elif x * y >= z:
        # if x times y is greater than the value of z
        sum_xy = x + y
        # assign the sum of x + y to the sum_xy variable
        return sum_xy


def resultOverrider(x: int, y: int, op: str, override: callable) -> int:
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. """
    if override:
        return override(x, y)
    elif not op:
        op = '+'
        if op == '+':
            return x + y
    else:
        if op == '-':
            return x - y
        elif op == '*':
            return x - y
        elif op == '/':
            return x // y

