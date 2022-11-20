import time

ms_time_stamp = int(round(time.time() * 1000))


def raiseIndexError(v):
    ls = [1, 2, 3]
    if v > len(ls):
        raise IndexError('index error')
    return None


def raiseZeroDivisionErrorWithMessage(message: str):
    x = 0
    y = 0
    if x or y == 0:
        raise ZeroDivisionError(message)


def raiseThisException(exception):
    raise exception


def catchAndReturnMessage(message: str, main_function: callable) -> str:
    try:
        # invoke the callable
        main_function()

        # return message if exception is not raised
        # print(message)
        return message
    except Exception as err:
        print(err)
        raise
