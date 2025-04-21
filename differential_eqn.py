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
h = 0.1
n = 2  # Only calculate up to y(0.2)

x, y = euler_method(equation, x0, y0, h, n)

# Print y(0.1) and y(0.2)
print(f"y(0.1) = {y[1]:.6f}")
print(f"y(0.2) = {y[2]:.6f}")