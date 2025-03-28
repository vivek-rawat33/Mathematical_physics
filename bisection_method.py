# def f(x):
#     return x**3 - x - 1

# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# e = float(input("Enter the tolerance: "))

# def bisection(a, b, e):
#     i = 1
#     condition = True
#     while condition:
#         c = (a + b) / 2
#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c
#         i += 1
#         condition = abs(f(c)) > e
#     print(f"Root is {c}, value of function at c is {f(c)} the number of iterations is {i}")

# if f(a) * f(b) > 0:
#     print("No root exists within the given interval.")
# else:
#     bisection(a, b, e)

# def f(x):
#     return x**n - 5
# n=int(input("enter the power:"))
# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# e = float(input("Enter the tolerance: "))

# def bisection(a, b, e):
#     i = 1
#     condition = True
#     while condition:
#         c = (a + b) / 2
#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c
#         i += 1
#         condition = abs(f(c)) > e
#     print(f"Root is {c}, value of function at c is {f(c)} the number of iterations is {i}")

# if f(a) * f(b) > 0:
#     print("No root exists within the given interval.")
# else:
#     bisection(a, b, e)


import math as M
def f(x):
    return x*M.sin(x) + M.cos(x)

a = float(input("Enter the value of a: "))
b = M.pi
e = float(input("Enter the tolerance: "))

def bisection(a, b, e):
    i = 1
    condition = True
    while condition:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
        condition = abs(f(c)) > e
    print(f"Root is {c}, value of function at c is {f(c)} the number of iterations is {i}")

if f(a) * f(b) > 0:
    print("No root exists within the given interval.")
else:
    bisection(a, b, e)