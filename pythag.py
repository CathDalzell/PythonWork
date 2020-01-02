#! /usr/bin/env python3

import math

a = 5.0
b = 7.0
tol = 0.000001

def square(x):
    return x*x

def closeEnough(x, guess):
    if abs(x - square(guess)) > tol:
        return True
    else:
        return False

def improveGuess(x, guess):
    return (x/guess + guess)/2


def sqrt(x):
    y = x
    while closeEnough(x, y):
        y = improveGuess(x, y)
    return y

def pythagorous(x, y):
    return sqrt(square(x) + square(y))

print("{0:2.4f}".format(sqrt(a)))


print("\n")

print("{0:2.4f}".format(pythagorous(a, b)))
