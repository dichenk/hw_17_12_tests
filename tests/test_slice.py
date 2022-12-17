from hw_17_12_tests import slice
import pytest

def test_slice():
    assert slice.my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    assert slice.my_slice([], 12, 14) == []
    assert slice.my_slice([1, 2, 3, 4, 5, 6], -4, 11111111) == [3, 4, 5, 6]
    assert slice.my_slice([1, 2, 3, 4, 5, 6], -9999) == [1, 2, 3, 4, 5, 6] 
