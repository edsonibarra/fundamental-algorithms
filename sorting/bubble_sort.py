from typing import List


def bubble_sort(arr: List[float]) -> None:
    is_sorted: bool = False
    counter: int = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                swap_values(i, i + 1, arr)
                is_sorted = False
        counter += 1


def swap_values(i: int, j: int, arr: List[float]) -> None:
    arr[i], arr[j] = arr[j], arr[i]
