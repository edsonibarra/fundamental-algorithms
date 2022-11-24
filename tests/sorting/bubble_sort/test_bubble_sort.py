import pytest
from sorting.bubble_sort import bubble_sort

@pytest.mark.parametrize(
    'arr,expected',
    (
        ([1,2,3,4,5], [1,2,3,4,5]),
        ([2,1,4,3,5], [1,2,3,4,5]),
        ([5,4,3,2,1], [1,2,3,4,5]),
        ([1], [1]),
        ([],[]),
        ([10,4,1],[1,4,10]),
    )
)
def test_bubble_sort(arr, expected):
    bubble_sort(arr)
    assert arr == expected
