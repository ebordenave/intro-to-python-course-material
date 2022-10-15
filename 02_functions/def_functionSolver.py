# You will be given a function as a parameter, the function you are given only accepts two number parameters and
# produces a float value. It is your job to figure out what mathematical operation the function you are given
# is performing by passing it many different parameters.
# The possible operations the function can perform are: add, subtract, multiply, and divide.
# The given function will only perform a single operation, it will not change after consecutive
# invocations. The function will execute the operation in the order the parameters are received.
# You must input your own values and test the expected responses to figure out the operation of
# the function. Once you have figured it out return the symbol of the operation (+, -, *, /).
# Another way to explain what has to happen, your function will receive as a function a parameter lets call
# it f(x, y), and the output of f(x, y) is z. We know that x and y are numbers, and you know
# that f(x, y) produces z, which is another number. Your job is to create a function that passes
# different numbers into f and evaluates the output z to find a pattern.
# The pattern you are looking for is to see if the function f is adding, subtracting, dividing or
# multiplying x and y. Once you find the pattern your function should return the mathematical
# symbol (+, -, *, /) that corresponds to function f’s operation. The return value should be a string.

def functionSolver(function: callable) -> str:
    # If the summation of the values in the function are equivalent to the result of the given arguments then return an addition string
    if function(1, 1) == 2.0 and function(2, 3) == 5.0 and function(4, 1) == 5.0:
        return '+'
    # If the difference of the values in the function are equivalent to the result of the given arguments then return a subtration string
    elif function(1, 1) == 0.0 and function(2, 3) == -1.0 and function(4, 1) == 3.0:
        return '-'
    # If the product of the values in the function are equivalent to the result of the given arguments then return a subtration string
    elif function(1, 1) == 1.0 and function(2, 3) == 6.0 and function(4, 1) == 4.0:
        return '*'
    # else the string is division
    return '/'

# tes
