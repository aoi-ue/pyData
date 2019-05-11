from string import Template
from oldindex import df

def subtitle():
    
    emptydict = []
    language = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
    t = Template('subtitle_$language')
    
    for i in language: 
        lan = t.substitute(language = i)
        emptydict.append(lan)
    
    print (emptydict)


subtitle() 
 
