#! /usr/bin/env python

"""
File: interpolate_exp_cos.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module calculates an interpolant approximation to the given function
for a given mesh of values, and recalculates until the mesh
is sufficiently fine. It then plots the function as indicated
by the sin_maker function.

"""

import numpy as np
import matplotlib.pyplot as mp

def sin_maker(n=10, eps=0.2):
    """Creates a mesh and evaluates a function with the mesh
    such that the benefit of increasing the mesh size is negligible
    for the reciprocal argument of the sin function plus an epsilon
    value as given in the arguments to the function."""
    mesh1 = np.linspace(0, 1, n+1) + eps
    mesh2 = np.linspace(0, 1, n+11) + eps
    sin1 = np.sin(1 / mesh1)
    sin2 = np.sin(1 / mesh2)
    while np.fabs(max(sin1) - max(sin2)) > 0.1:
        n = n + 10
        mesh1 = np.linspace(0, 1, n+1) + eps
        mesh2 = np.linspace(0, 1, n+11) + eps
        sin1 = np.sin(1 / mesh1)
        sin2 = np.sin(1 / mesh2)
    return mesh1, sin1

def graph():
    """calls the sin_maker function and plots the graph"""
    mesh, sinf = sin_maker()
    mp.plot(mesh, sinf, 'ko')
    mp.xlim([0, 1.2 + 0.01])
    mp.ylim([-0.01, 1.01])
    mp.title('Sin Interpolating Function Reciprocal Argument')
    mp.xlabel('x')
    mp.ylabel('sin of inverse x + epsilon')