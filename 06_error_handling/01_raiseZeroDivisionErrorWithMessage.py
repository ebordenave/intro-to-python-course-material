
def raiseZeroDivisionErrorWithMessage(message: str):
    x = 0
    y = 0
    try:
        z = x/y
    except ZeroDivisionError:
        message = 'zero division error'
        raise message
    return message
