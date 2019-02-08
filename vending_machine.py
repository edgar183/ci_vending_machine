#import all functions from test file
from byotest import *

def get_change(amount):
    return []

#amount of change back is 0, no coins back
test_are_equal(get_change(0),[])
print("all tests pass!")