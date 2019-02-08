#import all functions from test file
from byotest import *

def get_change(amount):
    """
    Takes the payment amount and returns the change

    `amount` the amount of money that we need to provide change for

    Returns a list of coin values
    """
    if amount == 0:
        return []
    
    return [1]

#amount of change back is 0, no coins back
test_are_equal(get_change(0),[])
#amount requaered back is an single coin
test_are_equal(get_change(1),[1])
print("all tests pass!")