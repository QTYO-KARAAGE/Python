import numpy as np
import sympy

def ex1(): 
    O = np.array([0, 0, 0])
    P = np.array([1, 4, -3])
    Q = np.array([-1, 3, 2])

    print("---(1-1)---")
    print(np.linalg.norm(O-P))
    print("---(1-2)---")
    print(np.linalg.norm(P-Q))

def ex2():
    a = np.array([1,2,3])
    b = np.array([2,3,1])
    c = np.array([3,1,2])

    print("---(2-1)---")
    print(np.linalg.norm(c))
    print("---(2-2)---")
    print(a + b)
    print("---(2-3)---")
    print(a + b + c)
    print("---(2-4)---")
    print(a + 2*b - 3*c)
    print("---(2-5)---")
    print(c - b + a)

def ex3():
    a = np.array([1,1,0])
    b = np.array([2,0,2])

    print("---(3-1)---")
    print(np.linalg.norm(a))
    print("---(3-2)---")
    print(np.linalg.norm(b))
    print("---(3-3)---")
    print(np.dot(a, b))
    print("---(3-4)---")
    print(np.rad2deg(np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))))
    print("---(3-5)---")
    sympy.var('x, y, z')
    eq1 = sympy.Eq(1 * x + 1 * y + 0 * z, 0)
    eq2 = sympy.Eq(2 * x + 0 * y + 2 * z, 0)
    eq3 = sympy.Eq(x**2 + y**2 + z**2, 0)
    print(sympy.solve([eq1, eq2, eq3], [x, y, z]))

ex1()
ex2()
ex3()