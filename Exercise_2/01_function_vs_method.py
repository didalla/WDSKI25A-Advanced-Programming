"""
Passing vs. calling
"""

# ----------------------------------------------------------------------
# Subtask A - Behaviour as an EXTERNAL function
# Task: Define a class StudentA that only stores a name and a list of
#       grades. Then write a standalone function average(student) that
#       takes such an object and returns the mean grade.
# Your Solution:


# Expected behaviour:
anna = StudentA("Anna", [80, 90, 100])
print("Subtask A:", average(anna))  # 90.0


# ----------------------------------------------------------------------
# Subtask B - Behaviour as a METHOD
# Task: Define a class StudentB that stores the same data, but this
#       time put the averaging logic INSIDE the class as a method
#       average(self) that the object calls on itself.
# Your Solution:

# Expected behaviour:
ben = StudentB("Ben", [80, 90, 100])
print("Subtask B:", ben.average())  # 90.0


# ----------------------------------------------------------------------
# Subtask C - Reflect (write your answer as a comment)
# Question: Both approaches give the same number. When would you prefer
#           each one?

print("Subtask C: agreement =", average(anna) == ben.average())  # True
