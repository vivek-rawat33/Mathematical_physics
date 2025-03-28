import math as M
def f(x):
    return 2*x - 3*M.sin(x) - 5 
x0 = float(input("enter the guess x_o :"))
x_1 = float(input("enter the guess x_1 :"))
e = float(input("enter the tol "))

def roots(x0,x_1,e,f):
    if(abs(f(x0))<e):
        return x0
    elif(abs(f(x_1))<e):
        return x_1
    else:
       return roots(x_1,x_1-(f(x_1)*(x_1 -x0)/(f(x_1)-f(x0))),e,f)
        
result = roots(x0,x_1,e,f)
print(result)