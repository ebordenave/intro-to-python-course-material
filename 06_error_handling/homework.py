import time


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


def catchCleanupAndThrow(main_supplier: callable, index_supplier: callable, zero_supplier: callable,
                         cleanup: callable) -> str:
    # try main_supplier
    try:
        return main_supplier()
    except IndexError:
        return index_supplier()
    except ZeroDivisionError:
        return zero_supplier()
    finally:
        cleanup()


class Timer:
    def __init__(self, time_out: int):
        self.__start_time = None
        self.__time_taken = -1
        self.__time_out = time_out

    def get_total_time(self):
        return self.__time_taken

    def __enter__(self):
        self.__start_time = int(round(time.time() * 1000))
        self.__time_taken = -1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__start_time is None:
            return
        ms_time_stamp = int(round(time.time() * 1000))
        self.__time_taken = ms_time_stamp - self.__start_time
        self.__start_time = None
        if self.__time_taken > self.__time_out:
            raise TimeoutError()
