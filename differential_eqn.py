# def euler_method(f, x0, y0, h, n):
#     x = [x0]
#     y = [y0]
    
#     for i in range(n):
#         y_next = y[-1] + h * f(x[-1], y[-1])
#         x_next = x[-1] + h
#         x.append(x_next)
#         y.append(y_next)
    
#     return x, y

# def equation(x, y):
#     return y - x

# x0 = 0
# y0 = 2
# h = 0.1
# n = 2  

# x, y = euler_method(equation, x0, y0, h, n)

# print(f"y(0.1) = {y[1]}")
# print(f"y(0.2) = {y[2]}")

# rk - 4 
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
    return y - x
x0 = 0
y0 = 2
h = 0.1
n = 2  
x,y = runge_kutta_method(equation,x0,y0,h,n)
print(f"y(0.1) = {y[1]}")
print(f"y(0.2) = {y[2]}")



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
h = 0.1
n = 2

x, y = runge_kutta_2nd_order(equation, x0, y0, h, n)

print(f"y(0.1) = {y[1]}")
print(f"y(0.2) = {y[2]}")
