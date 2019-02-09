#import all functions from test file
from byotest import *

euro_coins = [100, 50, 20, 10, 5, 2, 1]
usd_coins = [100, 50, 25, 10, 5, 2, 1]
# add 
def get_change(amount, coins=euro_coins):
    """
    Takes the payment amount and returns the change

    `amount` the amount of money that we need to provide change for

    Returns a list of coin values
    """
   
   
        
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
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
print("All tests pass!")