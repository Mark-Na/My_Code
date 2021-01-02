from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

valid_colours = ("red","green","yellow","blue","magenta","cyan","white")
msg = input("What would you like to print?: ")
color = input("What color?: ")
if color not in valid_colours:
    color = "magenta"
ascii_art = figlet_format(msg)
init()
colored_ascii = colored(ascii_art,color)
print(colored_ascii)