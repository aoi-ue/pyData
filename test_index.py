import pytest
from index import addition

def test1():
    assert addition(1,2) == 3
    assert addition(3,4) == 6
