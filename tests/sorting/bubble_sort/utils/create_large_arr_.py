import random
from typing import List


def create_large_arr_(size=1_000) -> List[int]:
    arr: List[int] = []
    for _ in range(size):
        arr.append(random.random())
    return arr, sorted(arr)
    