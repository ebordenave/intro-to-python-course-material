def raiseZeroDivisionErrorWithMessage(message: str):
    x = 0
    y = 0
    try:
        res = x / y
        print(res)
    except ZeroDivisionError:
        raise ZeroDivisionError(message)
