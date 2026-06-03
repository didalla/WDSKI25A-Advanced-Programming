"""
Work with "dunders" (double-underscore names)
"""

# ----------------------------------------------------------------------
# Build the class by implementing each special method below.
#
# Subtask A - __init__ : store the x and y components.
# Subtask B - __repr__ : a clear developer-facing text form, e.g.
#             "Vector2D(1, 2)". (Used when you print a list of vectors.)
# Subtask C - __add__  : adding two vectors returns a NEW Vector2D with
#             component-wise sums, so that v1 + v2 works.
# Subtask D - __eq__   : two vectors are equal when both components match,
#             so that v1 == v2 works.
# Subtask E - __mul__  : multiplying a vector by a number scales both
#             components, so that v * 3 works.
# Subtask F - __abs__  : abs(v) returns the vector's length (magnitude).

class Vector2D:

    pass
    # Add all special methods here to make it behave like 
    # displayed in the outputs below


# ----------------------------------------------------------------------
# Tests / expected behaviour
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print("Subtask B:", [v1, v2])        # [Vector2D(1, 2), Vector2D(3, 4)]
print("Subtask C:", v1 + v2)         # Vector2D(4, 6)
print("Subtask D:", v1 == Vector2D(1, 2))  # True
print("Subtask E:", v1 * 3)          # Vector2D(3, 6)
print("Subtask F:", abs(v2))         # 5.0
