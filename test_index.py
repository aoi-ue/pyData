import pytest
from index import subtitlelist
from refactorNtest import subtitle_length, subtitle_unique_length


def test2():

    a = subtitlelist
    dupes = [x for n, x in enumerate(a) if x in a[:n]]

    if (subtitle_length == subtitle_unique_length) == True:
        print("No Duplicates")
        assert True
    else:
        print(dupes)
        assert False
        
test2()

