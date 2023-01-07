import sympy as sp
import numpy as np

def limits(mantissa_length, exp_min, exp_max, base=10):
    x_max = (1 - base ** -mantissa_length) * base ** exp_max
    x_min = base ** (exp_min - 1)
    return x_min, x_max

def absolute_error(approximation, exact):
    return abs(approximation - exact)

def relative_error(approximation, exact):
    if (exact == 0):
        return 0
    return abs(approximation - exact) / abs(exact)

def eps(digits, base=10):
    return 0.5 * base ** (1 - digits)

def condition(func, derivative, x):
    return abs(derivative(x)) * abs(x) / abs(func(x))