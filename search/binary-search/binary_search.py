from typing import List


def binary_search(array: List[int], target: int) -> int:
    print('looking for ',target)
    left: int = 0
    right: int = len(array) - 1
    found: bool = False
    while not found and left < right:
        pivot_index = left + right // 2
        if target == array[pivot_index]:
            return pivot_index
        elif target < array[pivot_index]:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    return -1
            
def main():
    array = [1,2,3,4,5,6,7]
    print(array)
    print(binary_search(array=array, target=2))
    print(binary_search(array=array, target=1))
    print(binary_search(array=array, target=4))
    print(binary_search(array=array, target=8))

main()