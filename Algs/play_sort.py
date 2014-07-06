import random
import unittest

from sort import *

data = [29,100,130,4,6,13,19,20]

for step in shell_sort_steps(data):    
    print("#", step, "shell_sort")