import sys
import os
from time import sleep

class Cracker:()
def __init__(self, file):
    self.file_name = file
    if os.path.exiists(file):
        print("File located!")
    else:
        print("File could not be found!")

cracker = Cracker("passes.txt")
