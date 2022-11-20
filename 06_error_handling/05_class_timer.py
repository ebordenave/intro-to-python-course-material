import time


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
