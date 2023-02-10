import numpy as np
from numpy.linalg import solve

def ex4():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[3, 2], [0, -1]])

    print("---(4-1)---")
    print(3 * b)
    print("---(4-2)---")
    print(2 * a - b)
    print("---(4-3)---")
    print(a + b)
    print("---(4-4)---")

    def unit():
        return ([[1, 0], [0, 1]])
    def zero():
        return ([[0 , 0], [0, 0]])

    print(unit)
    print(zero)

def ex5():
    a = np.array([[1, 2], [2, 1]])
    b = np.array([[1, 1], [2, -1]])
    e = np.array([[1, 0], [0, 1]])

    print("---(5-1)---")
    print(a * b)
    print("---(5-2)---")
    print(a * e)
    a = np.array([[1, 2], [0, 1], [1, 0]])
    b = np.array([[0, 0, 1], [1, 0, 1], [1, 0, 0]])
    c = np.array([[1], [3], [0]])
    d = np.array([[0, 1, 0]])

    print("---(5-3)---")
    print("定義なし")
    print("---(5-4)---")
    print(d * c)
    print("---(5-5)---")
    print("定義なし")
    print("---(5-6)---")
    print(b * c)

def ex6():
    a = np.array([[2, 3], [5, -2]])
    right = np.array([31, 30])

    print("---(6-1)---")
    print(a)
    print("---(6-2)---")
    print(np.linalg.inv(a))
    print("---(6-3)---")
    print(solve(a, right))

ex4()  
ex5()
ex6()