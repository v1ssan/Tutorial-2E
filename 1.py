"""
You are given two lists:
 - items: list of item names
 - quantities: list of how many of each item

A function `get_price(item)` is already implemented and returns the price of the item.
Write a function that calculates and prints the total cost of all items.

Example:
If apple=$2, banana=$1, milk=$3
Total = 3*2 + 2*1 + 1*3 = 11
"""

items = ["apple", "banana", "milk"]
quantities = [3, 2, 1]

def get_price(item):
    prices = {"apple": 2, "banana": 1, "milk": 3}
    if item.lower() in prices:
        return prices[item]

    return 0
