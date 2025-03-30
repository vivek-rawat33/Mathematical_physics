# import math
# import matplotlib.pyplot as plt
# x = [i * math.pi / 180 for i in range(361)]
# n = int(input("Enter the value of n: "))

# def sin_approx(x_values, n):
#     y_values = []
#     x_value =[]
#     for x in x_values:
#         sum = 0
#         for i in range(n):
#             sum += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
#         y_values.append(sum) 
#         x_value.append(x)
#     return y_values,x_value
# result,x_value = sin_approx(x, n)

# sin_plot = [math.sin(i) for i in x]
# plt.scatter(x_value, result ,color='red',label='approx')
# plt.plot(x, sin_plot, color='black' ,label='actual')
# plt.legend()
# plt.show()


# n = int(input("Enter the value of n: "))
# step =0.5
# x = [i*step for i in range(-10,11)]
# def exponential(x_values, n):
#     y_values = []
#     x_value =[]
#     for x in x_values:
#         sum = 0
#         for i in range(n):
#             sum += (x**i)/math.factorial(i)
#         y_values.append(sum) 
#         x_value.append(x)
#     return y_values,x_value
# result,x_value = exponential(x, n)
# e = [math.exp(i) for i in x]
# plt.scatter(x, result ,color='red',label='approx')
# plt.plot(x, e, color='black' ,label='actual')
# plt.legend()
# plt.grid(True)
# plt.show()



# x = [i * math.pi / 180 for i in range(361)]
# n = int(input("Enter the value of n: "))

# def cos_approx(x_values, n):
#     y_values = []
#     x_value =[]
#     for x in x_values:
#         sum = 0
#         for i in range(n):
#             sum += (((-1)**i)*x**(2*i))/(math.factorial(2*i))
#         y_values.append(sum) 
#         x_value.append(x)
#     return y_values,x_value
# result,x_value = cos_approx(x, n)

# sin_plot = [math.cos(i) for i in x]
# plt.scatter(x_value, result ,color='red',label='approx')
# plt.plot(x, sin_plot, color='black' ,label='actual')
# plt.legend()
# plt.show()


import math
import matplotlib.pyplot as plt
x = [i * 0.1 for i in range(-9, 10)]
n = int(input("Enter the number of terms for the expansion (n): "))
def log_approx(x_values, n):
    y_values = []
    for x in x_values:
        if x <= -1: 
            y_values.append(float('nan'))
        else:
            sum = 0
            for i in range(1, n + 1):
                sum += ((-1) ** (i + 1)) * (x ** i) / i
            y_values.append(sum)
    return y_values
result = log_approx(x, n)
actual = [math.log(1 + i) if i > -1 else float('nan') for i in x]
plt.scatter(x, result, color='red', label='Approximation')
plt.plot(x, actual, color='black', label='Actual log(1+x)')
plt.xlabel('x')
plt.ylabel('log(1+x)')
plt.legend()
plt.grid(True)
plt.title('Taylor Series Approximation of log(1+x)')
plt.show()