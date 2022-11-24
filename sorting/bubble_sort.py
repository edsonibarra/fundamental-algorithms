from typing import List


def bubble_sort(arr: List[int]) -> None:
    is_sorted: bool = False
    counter: int = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                swap_values(i, i + 1, arr)
                is_sorted = False
        count += 1


def swap_values(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
