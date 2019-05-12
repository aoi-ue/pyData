from string import Template
from index import df

def subtitle():
    
    emptydict = []
    language = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
    t = Template('subtitle_$language')
    
    for i in language: 
        lan = t.substitute(language = i)
        emptydict.append(lan)
    
    print (emptydict)

subtitle() 
 
for i in subtitle():
    print(df[i].str.strip())

subtitle_length = len(subtitle())
subtitle_unique_length = len(set(subtitle()))
