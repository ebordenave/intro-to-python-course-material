import time

ms_time_stamp = int(round(time.time() * 1000))


class Timer:
    def __init__(self, time_out: int):
        self.time_out = time_out

    def get_total_time(self) -> int:
        return self.total_time

    def __enter__(self) -> Timer:
        return Timer

    def __exit__(self, exc_type, exc_value, traceback):
        # self.something_here.close()
        # option 1 ^
        # print('ok')
        # return False
        # option 2 ^
