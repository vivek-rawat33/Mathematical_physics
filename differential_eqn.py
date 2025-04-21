import numpy as np

def euler_method(f, x0, y0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    x[0] = x0
    y[0] = y0
    
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
        x[i+1] = x[i] + h
    
    return x, y

def equation(x, y):
    return y - x

x0 = 0
y0 = 1
h = 0.1
n = 10

x, y = euler_method(equation, x0, y0, h, n)

# Print the results
print("x\t\ty")
for i in range(len(x)):
    print(f"{x[i]:.2f}\t\t{y[i]:.6f}")
