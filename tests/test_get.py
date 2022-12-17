from hw_17_12_tests import get
import pytest

def test_get():
    assert get.get([1, 2, 3], 1, "a") == 2
    assert get.get([4, 5, 6], 7, "val") == "val"
    assert get.get([4, 5, 6], 999) == None


