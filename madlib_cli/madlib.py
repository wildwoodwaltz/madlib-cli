import re

def read_template(file):

    with open(file) as madlib:
        return(madlib.read())


def parse_template(template):
    
    stripped = re.sub(r'{[^}]*}', '{}', template)
    parts = tuple(re.findall(r'{(.*?)}', template))
    return(stripped,parts)

def merge(template, words):

    madlib = template.format(*words)
    return madlib


print('''
******************************************
**      WELCOME TO PYTHON MADLIBS       **
**                                      **
**    Please follow the user prompts    **
**    to create your very own mad lib   **
**                                      **
**   type 'quit' to "QUIT" at any time  **                               
******************************************
''')
