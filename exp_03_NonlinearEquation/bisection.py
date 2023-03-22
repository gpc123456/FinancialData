""""
README
======
This file contains Python codes.
======
"""

""" The bisection method """




import time
def bisection(f, a, b, tol=0.1, maxiter=10):
    """
    :param f: The function to solve
    :param a: The x-axis value where f(a)<0
    :param b: The x-axis value where f(b)>0
    :param tol: The precision of the solution
    :param maxiter: Maximum number of iterations
    :return: The x-axis value of the root,
                number of iterations used
    """
    c = (a+b)*0.5  # Declare c as the midpoint ab
    n = 1  # Start with 1 iteration
    while n <= maxiter:
        c = (a+b)*0.5
        if f(c) == 0 or abs(a-b)*0.5 < tol:
            # Root is found or is very close
            return c, n

        n += 1
        if f(c) < 0:
            a = c
        else:
            b = c

    return c, n


if __name__ == "__main__":
    def y(x): return 5*x**3 + 3.0*x**2 - 5.
    t0 = time.time()
    for i in range(1000):
        root, iterations = bisection(y, -5, 5, 0.00001, 100)
    t1 = time.time()
    print("Root is:", root)
    print("Iterations:", iterations)
    print("Process time:", (t1-t0)/1000)
