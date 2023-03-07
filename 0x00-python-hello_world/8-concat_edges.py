#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split()[5][:-1] + " " + str.split()[8][:-1]
print(str)
