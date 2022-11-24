import random
from typing import List, Tuple


def create_large_arr_(size=1_000) -> Tuple[List[float], List[float]]:
    arr: List[float] = []
    for _ in range(size):
        arr.append(random.random())
    return arr, sorted(arr)
    