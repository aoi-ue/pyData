from string import Template
from index import df

def subtitle():
    
    emptydict = []
    language = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu', 'japanese']
    t = Template('subtitle_$language')
    
    for i in language: 
        lan = t.substitute(language = i)
        emptydict.append(lan)
        
    return emptydict

subtitle_length = len(subtitle())
subtitle_unique_length = len(set(subtitle()))