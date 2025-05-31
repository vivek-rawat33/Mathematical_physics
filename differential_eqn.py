import matplotlib.pyplot as plt 
import math as M
def euler_method(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        y_next = y[-1] + h * f(x[-1], y[-1])
        x_next = x[-1] + h
        x.append(x_next)
        y.append(y_next)
    
    return x, y

def equation(x, y):
    return y - x

x0 = 0
y0 = 2
h = 0.01
n = 20

x, y = euler_method(equation, x0, y0, h, n)

print(f"y(0.1) = {y[1]}")
print(f"y(0.2) = {y[2]}")


def runge_kutta_method(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x[-1] + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x[-1] + h, y[-1] + k3)
        
        y_next = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x[-1] + h
        
        x.append(x_next)
        y.append(y_next)
    
    return x, y
def equation(x, y):
    return y -x
x0 = 0
y0 = 2
h = 0.01
n = 20
x,y = runge_kutta_method(equation,x0,y0,h,n)
print(f"y(0.1) ={y[1]}")
print(f"y(0.2) ={y[2]}")


# rk - 4 
# qus 2
def runge_kutta_method(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x[-1] + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x[-1] + h, y[-1] + k3)
        
        y_next = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x[-1] + h
        
        x.append(x_next)
        y.append(y_next)
    
    return x, y
def equation(x, y):
    return y + x*M.exp(x)
x0 = 0
y0 = 1
h = 0.01
n = 200
x,y = runge_kutta_method(equation,x0,y0,h,n)
print(f"y(2) ={y[n]}")

plt.plot(x,y)
plt.scatter(x,y)
plt.show()

#qus 3
def runge_kutta_method(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x[-1] + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x[-1] + h, y[-1] + k3)
        
        y_next = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x[-1] + h
        
        x.append(x_next)
        y.append(y_next)
    
    return x, y
def equation(x, y):
    return 2*(25-y)
x0 = 0
y0 = 40
h = 0.01
n = 1000
x,y = runge_kutta_method(equation,x0,y0,h,n)
print(f"y(10) ={y[-1]}")

plt.plot(x,y)
plt.scatter(x,y)
plt.show()

#qus 4
def runge_kutta_method(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x[-1] + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x[-1] + h, y[-1] + k3)
        
        y_next = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x[-1] + h
        
        x.append(x_next)
        y.append(y_next)
    
    return x, y
def equation(x, y):
    return x-2*x*y;
x0 = 0
y0 = 2
h = 0.01
n = 500
x,y = runge_kutta_method(equation,x0,y0,h,n)
print(f"y(5) ={y[-1]}")

plt.plot(x,y)
plt.scatter(x,y)
plt.show()


#rk method 
def runge_kutta_2nd_order(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h, y[-1] + k1)
        
        y_next = y[-1] + (k1 + k2) / 2
        x_next = x[-1] + h
        
        x.append(x_next)
        y.append(y_next)
    
    return x, y

def equation(x, y):
    return y - x


x0 = 0
y0 = 2
h = 0.01
n = 20

x, y = runge_kutta_2nd_order(equation, x0, y0, h, n)

print(f"y(0.1) = {y[1]}")
print(f"y(0.2) = {y[2]}")
