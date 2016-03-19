#! /usr/bin/env python

"""
File: interpolate_exp_cos.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates an interpolant approximation to the given function at the given point.

"""

import numpy as np

def exp_cos_func(q):
    """Approximates interpolant approximation to the function."""
    mesh = np.linspace(-1, 1, q+1)
    f = np.exp(- mesh**2)*np.cos(2 * np.pi * mesh)
    x_point = -0.45
    step = 2 / float(q+1)
    k_val = int(1-x_point / step)
    approximation = f[k_val] + ((f[k_val+1] - f[k_val])/(mesh[k_val+1] - mesh[k_val])) * (x_point - mesh[k_val])
    exact = f = np.exp(- x_point**2)*np.cos(2 * np.pi * x_point)
    return approximation, exact - approximation

def test_approx():
    """Ensures that the approximation is accurate at q = 8"""
    apt = np.fabs(exp_cos_func(8)[1]) < 0.1
    msg = 'Approximation not accurate.'
    assert apt, msg
