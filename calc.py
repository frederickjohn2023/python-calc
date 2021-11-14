# import math module
from math import *

# addition function
def add(a,b):
    c = float(a) + float(b)
    print(c)

# subtraction function
def subtract(a,b):
    c =float(a) - float(b)
    print(c)

# multiplication function
def multiply(a,b):
    c = float(a) * float(b)
    print(c)

# division function
def divide(a,b):
    c = float(a) / float(b)
    print(c)

# accept expression
eq = input("input the equation: ")
ad = eq.find("+") # look for + symbol
su = eq.find("-") # look for - symbol
mu = eq.find("*") # look for * symbol
di = eq.find("/") # look for / symbol

# if + is found
if ad==1:
    # extract operands and store in list
    s  = eq.split("+")
    n1 = s[0]
    n2 = s[1]
    add(n1,n2) # send operands to function
# if - is found
elif su ==1:
    # extract operands and store in list
    s  = eq.split("-")
    n1 = s[0]
    n2 = s[1]
    subtract(n1,n2) # send operands to function
# if * is found
elif mu == 1:
    # extract operands and store in list
    s  = eq.split("*")
    n1 = s[0]
    n2 = s[1]
    multiply(n1,n2) # send operands to function
# if / is found
elif di == 1:
    # extract operands and store in list
    s = eq.split("/")
    n1 = s[0]
    n2 = s[1]
    divide(n1,n2) # send operands to function
