from hw_17_12_tests import index_of
import pytest

def test_index_of():
    assert index_of.index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of.index_of([2, 7, 3, 2, 4], 15) == -1
    assert index_of.index_of([2, 7, 3, 2, 4], 2, -3) == 3
    assert index_of.index_of([], 14) == -1
    assert index_of.index_of([2, 7, 3, 2, 4], 3, -999) == 2



