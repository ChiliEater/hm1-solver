import numpy as np
import scipy as sc
import sympy as sp
import math
from IPython.display import display, Markdown

# Prints an expression and/or string with an optional multiline toggle for large input like matrices.
def dis(str=None, expr=None, multiline=False):
    if expr == None:
        display(Markdown(str))
        return

    if str == None:
        display(expr)
        return

    if multiline:
        display(Markdown(str))
        display(expr)
    else:
        display(
            Markdown(
                "{}: {}".format(str, sp.latex(expr, mode="inline", itex=True))
            )
        )

# Converts NumPy matrix to SymPy matrix
def np_to_sym(matrix: np.ndarray):
    return sp.Matrix(matrix.tolist())

# Converts SymPy matrix to NumPy matrix
def sym_to_np(matrix: sp.Matrix):
    return np.array(matrix.tolist()).astype(np.float64)
