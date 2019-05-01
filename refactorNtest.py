from string import Template 


def subtitle():
    
    emptydict = []
    
    language = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
    t = Template('\'subtitle_$language\': strip_spaces')
    
    for i in language: 
        lan = {t.substitute(language = i)}
        emptydict.append(lan)
    
    return emptydict


def additional(a,b):
    return a + b
