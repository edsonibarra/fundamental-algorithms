import pytest
from sorting.bubble_sort import bubble_sort
from tests.sorting.bubble_sort.utils.create_large_arr_ import create_large_arr_

big_arr_1, sorted_big_arr_1 = create_large_arr_()
big_arr_2, sorted_big_arr_2 = create_large_arr_()
big_arr_3, sorted_big_arr_3 = create_large_arr_()
big_arr_4, sorted_big_arr_4 = create_large_arr_()
big_arr_5, sorted_big_arr_5 = create_large_arr_()
big_arr_6, sorted_big_arr_6 = create_large_arr_()
big_arr_7, sorted_big_arr_7 = create_large_arr_()
big_arr_8, sorted_big_arr_8 = create_large_arr_()
big_arr_9, sorted_big_arr_9 = create_large_arr_()
big_arr_11, sorted_big_arr_11 = create_large_arr_()
big_arr_12, sorted_big_arr_12 = create_large_arr_()
big_arr_13, sorted_big_arr_13 = create_large_arr_()
big_arr_14, sorted_big_arr_14 = create_large_arr_()
big_arr_15, sorted_big_arr_15 = create_large_arr_()
big_arr_16, sorted_big_arr_16 = create_large_arr_()
big_arr_17, sorted_big_arr_17 = create_large_arr_()
big_arr_18, sorted_big_arr_18 = create_large_arr_()
big_arr_19, sorted_big_arr_19 = create_large_arr_()
big_arr_20, sorted_big_arr_20 = create_large_arr_()
big_arr_21, sorted_big_arr_21 = create_large_arr_(size=4_000)
big_arr_22, sorted_big_arr_22 = create_large_arr_(size=4_000)
big_arr_23, sorted_big_arr_23 = create_large_arr_(size=4_000)
big_arr_24, sorted_big_arr_24 = create_large_arr_(size=4_000)
big_arr_25, sorted_big_arr_25 = create_large_arr_(size=4_000)
big_arr_26, sorted_big_arr_26 = create_large_arr_(size=4_000)
big_arr_27, sorted_big_arr_27 = create_large_arr_(size=4_000)
big_arr_28, sorted_big_arr_28 = create_large_arr_(size=4_000)
big_arr_29, sorted_big_arr_29 = create_large_arr_(size=4_000)
big_arr_30, sorted_big_arr_30 = create_large_arr_(size=4_000)


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
        (big_arr_1, sorted_big_arr_1),
        (big_arr_2, sorted_big_arr_2),
        (big_arr_3, sorted_big_arr_3),
        (big_arr_4, sorted_big_arr_4),
        (big_arr_5, sorted_big_arr_5),
        (big_arr_6, sorted_big_arr_6),
        (big_arr_7, sorted_big_arr_7),
        (big_arr_8, sorted_big_arr_8),
        (big_arr_9, sorted_big_arr_9),
        (big_arr_11, sorted_big_arr_11),
        (big_arr_12, sorted_big_arr_12),
        (big_arr_13, sorted_big_arr_13),
        (big_arr_14, sorted_big_arr_14),
        (big_arr_15, sorted_big_arr_15),
        (big_arr_16, sorted_big_arr_16),
        (big_arr_17, sorted_big_arr_17),
        (big_arr_18, sorted_big_arr_18),
        (big_arr_19, sorted_big_arr_19),
        (big_arr_20, sorted_big_arr_20),
        (big_arr_21, sorted_big_arr_21),
        (big_arr_22, sorted_big_arr_22),
        (big_arr_23, sorted_big_arr_23),
        (big_arr_24, sorted_big_arr_24),
        (big_arr_25, sorted_big_arr_25),
        (big_arr_26, sorted_big_arr_26),
        (big_arr_27, sorted_big_arr_27),
        (big_arr_28, sorted_big_arr_28),
        (big_arr_29, sorted_big_arr_29),
        (big_arr_30, sorted_big_arr_30),
    )
)
def test_bubble_sort(arr, expected):
    bubble_sort(arr)
    assert arr == expected
