#import all functions from test file
from byotest import *

# Create a dictionary with denomination of coin and its quantity as key, value
euro_coins = {200:20, 100:20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20}
usd_coins = {100:20, 50:20, 25:20, 10:20, 5:20, 2:20, 1:20}
    
def get_change(amount, coins=euro_coins):
    """
    Takes the payment amount and returns the change

    `amount` the amount of money that we need to provide change for

    Returns a list of coin values
    """
        
    change = []
    # Unlike a list, looping through a dictionary does not keep the order.
    # Therefore we use `sorted()` to sort the order. This will sstart with the
    # lowest by default, so we use `reverse=True` to start with the highest
    # denomination. The `while` ends when the domination quantity reaches 0.
    # An exception is thrown if there are insufficient coins to give change.
    for demonination in sorted(coins.keys(), reverse=True):
        while demonination <= amount and coins[demonination] > 0:
            amount -= demonination
            coins[demonination] -= 1
            change.append(demonination)
    if amount != 0:
        raise Exception("Insufficient coins to give change.")
    return change

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
# change in more then one coin
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(7),[5,2])
# return more than 2 coins
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])

test_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}),"Insufficient coins to give change.")
print("All tests pass!")