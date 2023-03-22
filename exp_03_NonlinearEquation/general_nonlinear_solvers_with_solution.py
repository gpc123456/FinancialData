""""
README
======
This file contains Python codes.
======
"""

"""
General nonlinear solvers
- with a solution
"""


import scipy.optimize as optimize
def y(x): return 5*x**3 + 3.0*x**2 - 5.
def dy(x): return 15*x**2 + 6*x


print(optimize.fsolve(y, 5., fprime=dy))
print(optimize.root(y, 5.))
