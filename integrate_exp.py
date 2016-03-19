#! /usr/bin/env python

"""
File: integrate_exp.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates the integral value of the Gaussian function on various intervals with
various mesh sizes and then outputs comparitive tables of the function values and the error
of the function.

"""

import numpy as np
import matplotlib.pylab as mp
import calculus as integrater

def exp_func(x):
    """Provides function for the module."""
    return np.exp(-x**2)

def plotter(func_array, mesh):
    """Plots a given function along with its generating mesh."""
    mp.plot(mesh, func_array, 'b-')
    mp.xlim([-10, 10])
    mp.ylim([-0.01, 1.01])
    mp.title('Gaussian Function is Even')
    mp.xlabel('x')
    mp.ylabel('Gaussian Plot')
    
def tabler():
    "Outputs two tables, one of the comparitive values and one of the comparitive errors."
    n_list = [100, 200, 300, 400, 500]
    L_list = [2, 4, 6, 8, 10]
    value_list = []
    for L in L_list:
        for n in n_list:
            value_list.append(2 * integrater.trapezoidal_matrix(exp_func, 0, L, n))
    error_list = np.sqrt(np.pi) - value_list
    print
    print '%40s' % 'Value Table'
    print
    print '%10s %10s %10s %10s %10s %10s' % ('', 'n = 100', 'n = 200', 'n = 300', 'n = 400', 'n = 500')
    print
    count = 0
    for L in L_list:
        L_line = 'L = ' + str(L)
        print '%10s %10f %10f %10f %10f %10f' % (L_line, value_list[count], value_list[count + 1], value_list[count + 2], value_list[count + 3], value_list[count + 4])
        count = count + 5
    print
    print
    print '%40s' % 'Error Table'
    print
    print '%10s %10s %10s %10s %10s %10s' % ('', 'n = 100', 'n = 200', 'n = 300', 'n = 400', 'n = 500')
    print
    count = 0
    for L in L_list:
        L_line = 'L = ' + str(L)
        print '%10s %10f %10f %10f %10f %10f' % (L_line, error_list[count], error_list[count + 1], error_list[count + 2], error_list[count + 3], error_list[count + 4])
        count = count + 5

def test_exp_func_values():
    """Ensures that the function has the correct value at x = 0."""
    apt = np.fabs(exp_func(0) - 1) < 1e-5
    msg = 'Exponential Gaussian function improperly defined. Function at value is not correct for Gaussian.'
    assert apt, msg
