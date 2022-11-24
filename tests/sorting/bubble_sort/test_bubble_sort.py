import pytest
from sorting.bubble_sort import bubble_sort
from sorting.bubble_sort.utils.create_large_arr import create_large_arr


@pytest.mark.parametrize(
    ('arr','expected'),
    (
        ([1,2,3,4,5], [1,2,3,4,5]),
        ([2,1,4,3,5], [1,2,3,4,5]),
        ([5,4,3,2,1], [1,2,3,4,5]),
        ([1], [1]),
        ([],[]),
        ([10,4,1],[1,4,10]),
        ([1,1,1],[1,1,1]),
        ([-10,4,1],[-10,1,4]),
        ([0,-1,-100],[-100, -1, 0]),
        ([-1_000,-10_000,-1_000_000,1],[-1_000_000,-10_000,-1_000,1]),
    )
)
def test_bubble_sort(arr, expected):
    bubble_sort(arr)
    assert arr == expected
