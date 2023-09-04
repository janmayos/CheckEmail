import re
from termcolor import colored

pat = re.compile(r"[a-zA-Z_]{1}[a-zA-Z1-9_-]*@+[a-zA-Z_]+.[a-zA-Z_]+")

with open("correos.txt") as file:
    for linea in file:
        if re.fullmatch(pat, linea.rstrip()):
            print(colored(f"'{linea.rstrip()}'\tMAIL!", 'green'))
        else:
            print(colored(f"'{linea.rstrip()}'\tNO MAIL", 'red'))
