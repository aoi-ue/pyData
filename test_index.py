import pytest
from index import np, df, excelname, todaydate, country, country_code, sub_language, audio_language, sub_code, audio_code

test_list_dict = {'country': country, 'country_code': country_code, 'sub_language': sub_language, 
                  'audio_language': audio_language, 'sub_code': sub_code, 'audio_code': audio_code}

def test1():

    for (key, value) in test_list_dict.items():
        assert len(np.unique(value)) == len(value)
        
        if len(np.unique(value)) != len(value):
            dupes = [x for n, x in enumerate(value) if x in value[:n]]
            print(dupes, key)

#Testing whether the excelname variable contains the text"csv"
def test2():
    text = "csv"
    assert text in excelname

#Checking that the dataframe is not empty
def test3():
    assert df is not df.empty