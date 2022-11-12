def raiseZeroDivisionErrorWithMessage(message: str):
    x = 0
    y = 0
    if x or y == 0:
        raise ZeroDivisionError(message)


raiseZeroDivisionErrorWithMessage("nope")
