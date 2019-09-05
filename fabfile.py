from fabric.api import *
from fabric.colors import red, green

def textgreen():
    print(green("This text is green!"))

def textred():
    print(red("This text is red!"))
