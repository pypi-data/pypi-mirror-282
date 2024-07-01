import math
import random
from typing import List, Union, TypeVar, Callable

T = TypeVar('T')

def truncate_with_floor(number: float, digits: int = 0):
    if digits == 0:
        return math.floor(number)
    stepper = 10 ** digits
    return math.floor(number * stepper) / stepper


def product(arr: List[Union[int, float]]) -> Union[int, float]:
    return math.prod(arr)


def choose(best_choice: Callable[[List[T]], T], actions: List[T], epsilon: float = 0.5) -> T:
    return random.choice(actions) if random.random() < epsilon else best_choice(actions)


def random_choice(array: List[T]) -> T:
    return random.choice(array)


def probability(value: float) -> bool:
    if not (0.0 <= value <= 1.0):
        raise ValueError("The value should be between 0 and 1 inclusive.")
    rand_number = random.uniform(0, 1)
    return rand_number <= value


if __name__ == '__main__':
    from performer_helper import TimeIt

    with TimeIt():
        for i in range(100000):
            truncate_with_floor(random.uniform(0, 1000))
