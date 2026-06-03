"""
Common mistakes when using lists as attributes
"""

# ----------------------------------------------------------------------
# Subtask A - The mutable default argument trap
# Task: Below is a Cart whose __init__ uses items=[] as a default.
#       Create two SEPARATE empty carts, add one item to each, and
#       print both. Explain what you observe, then fix it.

class BuggyCart:
    def __init__(self, items=[]):
        self.items = items

    def add(self, item):
        self.items.append(item)


a = BuggyCart()
b = BuggyCart()
a.add("apple")
b.add("banana")
print("Subtask A (buggy):", a.items, b.items)
# Result: ['apple', 'banana'] ['apple', 'banana']
# Why: the default [] is created ONCE when the function is defined and
# is SHARED by every call that uses the default. Both carts point at
# the same list.

# Your Solution to fix this:


# ----------------------------------------------------------------------
# Subtask B - Class attribute vs. instance attribute
# Task: Below, 'tags' is defined at CLASS level, so it is shared by all
#       instances. Give two players different tags and observe. Then fix
#       it so each player owns its own list.

class BuggyPlayer:
    tags = []

    def __init__(self, name):
        self.name = name

    def tag(self, label):
        self.tags.append(label)


p1 = BuggyPlayer("Mario")
p2 = BuggyPlayer("Luigi")
p1.tag("fast")
p2.tag("jumper")
print("Subtask B (buggy):", p1.tags, p2.tags)
# Surprise: ['fast', 'jumper'] ['fast', 'jumper'] - same shared list.

# Your Solution to fix this: 

# ----------------------------------------------------------------------
# Subtask C - Aliasing a list passed in from outside
# Task: A Playlist is created from an existing list of songs. Store it,
#       then mutate the ORIGINAL list afterwards and observe that the
#       playlist changed too. Then fix it by copying on the way in.

class BuggyPlaylist:
    def __init__(self, songs):
        self.songs = songs             # <-- stores a reference, not a copy


original = ["song1", "song2"]
pl = BuggyPlaylist(original)
original.append("song3")               # mutate the outside list later
print("Subtask C (buggy):", pl.songs)
# Surprise: ['song1', 'song2', 'song3'] - the outside change leaked in.

# Your Solution to fix this:


# ----------------------------------------------------------------------
# Subtask D - Reflect (write your answer as a comment)
# Question: All three bugs share one root cause. What is it?
