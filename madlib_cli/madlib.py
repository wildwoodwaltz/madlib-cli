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

# def user_prompt(parts):
#     madlib_list = [None]
#     idx = 0
#     for word in parts:
#         if idx == 0:
#             response = input(f"Please type in a {word} and hit enter/return")
#             madlib_list[idx]=response
#         elif idx <= len(parts):
#             response = input(f"Ok, now give us one {word}")
#             madlib_list[idx]=response
#     create_madlib(madlib_list)
        
# def create_madlib(madlib):
#     with open('lib_laugh_love.txt', 'x') as user_lib:
#         user_lib.write(madlib)

# print('''
# ******************************************
# **      WELCOME TO PYTHON MADLIBS       **
# **                                      **
# **    Please follow the user prompts    **
# **    to create your very own mad lib   **
# **                                      **    
# **      You will get several prompts    **
# **    asking for various grammar parts  **
# **     such as Noun, Verb, Pronoun, Pet **
# **      Please respond to the inputs    **
# **                accordingly.          **
# **                                      **
# **      Enter in 'start' to begin       **
# **   type 'quit' to "QUIT" at any time  **                               
# ******************************************
# ''')

# def run_or_not():
#     i_o = input().lower()
#     if i_o == 'quit':
#         quit()
#     elif i_o == 'start':
#         user_prompt()
#     else:
#         print("Please either 'start' or 'quit'")

# run_or_not()