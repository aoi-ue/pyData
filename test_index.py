import pytest
from refactorNtest import subtitle, subtitle_length, subtitle_unique_length

a = subtitle()
dupes = [x for n, x in enumerate(a) if x in a[:n]]

def test2():
    if (subtitle_length == subtitle_unique_length) == True:
        print("Same Length")
        assert True
    else:
        print(dupes)
        assert False

