"""
Combining objects and functional tools:
you can sort, filter and transform objects without writing a single
explicit loop. 
Use: sorted(), a comprehension, map(), and reduce(), and finally you
build an object that behaves like a function (__call__).
"""
from functools import reduce


# Given: a small Product class and a list of products.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}(${self.price:.2f})"

    def discounted(self, factor):
        # Returns a NEW product, does not mutate this one (functional style).
        return Product(self.name, self.price * (1 - factor))


catalog = [
    Product("Pen", 1.50),
    Product("Notebook", 4.00),
    Product("Backpack", 25.00),
    Product("Eraser", 0.80),
]

# ----------------------------------------------------------------------
# Subtask A - Sort with a key function
# Task: Use sorted() with a key to return the products ordered by price
#       (cheapest first). Do not mutate 'catalog'.
# Your Solution:


# ----------------------------------------------------------------------
# Subtask B - Filter with a comprehension
# Task: Build a list of the NAMES of all products that cost less
#       than 5.00.
# Your Solution:


# ----------------------------------------------------------------------
# Subtask C - Transform with map()
# Task: Use map() together with the discounted() method to apply a 20%
#       discount to every product, producing a new list of products.
# Your Solution:


# ----------------------------------------------------------------------
# Subtask D - Aggregate with reduce()
# Task: Use functools.reduce to compute the total price of the whole
#       catalog. (Compare it mentally to sum(p.price for p in catalog).)
# Your Solution:


# ----------------------------------------------------------------------
# Subtask E - An object that behaves like a function (__call__)
# Task: Define a class Discount that is created with a percentage and
#       can then be CALLED like a function on a price. This turns a
#       configurable strategy into a first-class, passable object.
# Your Solution:
