f = lambda x: x**3 - 3*x - 5 
g = lambda x: 3*x**2 -3

def newton_Rapshon(f,g,x_o,e):
    if abs(f(x_o))<e:
        return x_o
    else:
        return newton_Rapshon(f,g,(x_o - (f(x_o)/g(x_o))),e)

e = float(input("enter the tol "))
x_o = float(input("enter the initial guess "))
result = newton_Rapshon(f,g,x_o,e)
print(result)