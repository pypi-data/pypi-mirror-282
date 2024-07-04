import time
from typing import Optional


def timeit(func, min_time=0):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time >= min_time:
            print(f"Function '{func.__name__}' took {end_time - start_time} seconds to execute.")
        return result

    return wrapper


class TimeIt:
    start_time:float
    end_time:float
    execution_time:float
    round:Optional[int]

    def __init__(self, round: Optional[int] = None):
        self.round = round

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        if self.round is not None:
            print(f"Execution time: {round(self.execution_time, self.round)} seconds")
        else:
            print(f"Execution time: {self.execution_time} seconds")
