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
    try:
        res = x / y
        print(res)
    except ZeroDivisionError:
        raise ZeroDivisionError(message)


def raiseThisException(exception):
    raise exception
