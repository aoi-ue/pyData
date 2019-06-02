import pytest
from refactor_test import subtitle_length, subtitle_unique_length, subtitle_list

def test2():

    a = subtitle_list
    dupes = [x for n, x in enumerate(a) if x in a[:n]]

    if (subtitle_length == subtitle_unique_length) == True:
        #print("No Duplicates")
        assert True
    else:
        #print(dupes)
        assert False