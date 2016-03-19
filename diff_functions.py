#! /usr/bin/env python

"""
File: diff_functions.py

Copyright (c) 2016 Taylor Patti

License: MIT

Plots and compares the vectorized approximation and analytical derivatives of functions.

"""

import numpy as np
import matplotlib.pyplot as mp
import calculus as differentiator

def f(x):
    return np.log(x + 1 / float(100))

def f_prime(x):
    return 1 / (x + 1 / float(100))

def g(x):
    return np.cos(np.exp(10*x))

def g_prime(x):
    return -10 * np.exp(10 * x) * np.sin(np.exp(10 * x))

def h(x):
    return x**x

def h_prime(x):
    return np.log(x) * x**x + x * x**(x-1)

def graph(func, f_prime, a, b, n):
    """Graphs both a functions vectorized approximation and analytical derrivative."""
    x = np.linspace(a, b, n)
    f_prime = f_prime(x)
    diff_mesh, f_diff = differentiator.diff(func, a, b, 1000)[0], differentiator.diff(func, a, b, 1000)[2]
    mp.plot(x, f_prime, 'ko')
    mp.plot(diff_mesh, f_diff, 'b-')
    mp.xlim([a - 0.01, b + 0.01])
    mp.xlabel('x')
    mp.ylabel('y')

def test_np_funcs():
    """Tests the np implementation of these functions as defined above for the value of x = 0."""
    apt = np.fabs(g(0) - np.cos(1)) < 1e-3
    msg = 'Improperly defined functions.'
    assert apt, msg
    
def test_derrivatives():
    """Ensures that the value of the derrivative of x^3 is good at x = 3 as per the vectorized derrivative function."""
    apt = np.fabs(differentiator.diff(h, 2, 3.01, 1000)[1][-1] - 56.6625)
    msg = 'Derrivative is imporperly calculated.'
    assert apt, msg