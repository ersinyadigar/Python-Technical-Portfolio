# ----------------------------------------------------
# Lab 7 - Using Tuples in Python
# Name: Ersin Yadigar
# Student ID: 041064136
# ----------------------------------------------------

# Question 1 - Accessing an element from a tuple

fruits = ("Apple", "Banana", "Orange", "Grapes")

print("The first fruit is:", fruits[0])   # Index 0
print("The third fruit is:", fruits[2])   # Index 2

# ----------------------------------------------------
# Question 2 - Negative indexing in a tuple

print("\nQuestion 2")

print("The last fruit is:", fruits[-1])          # Last element
print("The second last fruit is:", fruits[-2])   # Second-last element

# ----------------------------------------------------
# Question 3 - Deleting a tuple

print("\nQuestion 3")

colors = ("Red", "Green", "Blue")

print("Original tuple:", colors)

# Delete the entire tuple
del colors

print("The entire tuple has been deleted successfully.")