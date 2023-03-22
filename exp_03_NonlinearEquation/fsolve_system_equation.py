import scipy.optimize as optimize


def f(x):
    return [
        x[0]+x[0]*x[1]-2,
        x[0]-x[1]-2
    ]


print(optimize.root(f, [0, -1]))
