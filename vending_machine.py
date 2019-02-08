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
    
    return [amount]

#amount of change back is 0, no coins back
test_are_equal(get_change(0),[])
#amount requaered back is an single coin
test_are_equal(get_change(1),[1])
# get change for every single coin accepted
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
print("all tests pass!")