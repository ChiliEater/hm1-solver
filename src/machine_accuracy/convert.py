import sympy as sp
import numpy as np

def to_float(mantissa, exponent, base=10):
    return mantissa * base ** exponent

def to_scientific(num, base=10):
    exp = 0
    while (num > 1):
        num /= base
        exp += 1
    return num, base, exp