""""
README
======
This file contains Python codes.
======
"""

""" The Newton-Raphson method """




import time
def newton(f, df, x, tol=0.001, maxiter=100):
    """
    :param f: The function to solve
    :param df: The derivative function of f
    :param x: Initial guess value of x
    :param tol: The precision of the solution
    :param maxiter: Maximum number of iterations
    :return: The x-axis value of the root,
                number of iterations used
    """
    n = 1
    while n <= maxiter:
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < tol:  # Root is very close
            return x1, n
        else:
            x = x1
            n += 1

    return None, n


if __name__ == "__main__":
    def y(x): return 5*x**3 + 3.0*x**2 - 5.
    def dy(x): return 15*x**2 + 6*x
    t0 = time.time()
    for i in range(1000):
        root, iterations = newton(y, dy, 5.0, 0.00001, 100)
    t1 = time.time()
    print("Root is:", root)
    print("Iterations:", iterations)
    print("Process time:", (t1-t0)/1000)
