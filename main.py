"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()

# for c in ['red', 'green', 'blue', 'yellow']:
#     t.color(c)
#     t.forward(75)
#     t.left(90)
numberStr = input("Type a number:")
print ("You just typed: " + numberStr)

# Remember numberStr is as a variable of type string
# This means that we cannnot use numberStr in mathematical operations

# Convert numberStr to an integer variable called numberInt

numberInt = int(numberStr)

if numberInt > 6:
  print("You just typed a number greater than 6")
elif numberInt < 6:
  print("You just typed a number that is less than 6")
else:
  print("You just typed 6!!!")