import matplotlib.pyplot as plt
import math as M

# x = [1, 1.2, 1.4, 1.6, 1.8, 2]
# y = [5, 8.7, 13.2, 20.5, 29.5, 42]
# Xlog=[]
# Ylog=[]
# m = len(x)

# for i in range(m):
#     Xlog.append(M.log(x[i]))
#     Ylog.append(M.log(y[i]))
# xy = [Xlog[i] * Ylog[i] for i in range(m)]
# x2 = [xi**2 for xi in Xlog]

# a1 = (m * sum(xy) - sum(Xlog) * sum(Ylog)) / (m * sum(x2) - (sum(Xlog))**2)
# a2 = (sum(Ylog) - a1 * sum(Xlog)) / m

# Ylog_pred = [a1 * Xlog[i] + a2 for i in range(m)]
# y_pred = [M.exp(yi) for yi in Ylog_pred]

# print(f"intercept = {a1}")
# print(f"slope = {M.exp(a2)}")

# plt.scatter(x, y, label='Data points')
# plt.plot(x, y_pred)
# plt.show()


#qus2
# year=[1951,1952,1953,1954,1955,1956,1957]
# product =[201,263,314,395,427,504,612]
# x=year
# y = product
# Xlog=[]
# Ylog=[]
# m = len(x)

# for i in range(m):
#     Xlog.append(M.log(x[i]))
#     Ylog.append(M.log(y[i]))
# xy = [Xlog[i] * Ylog[i] for i in range(m)]
# x2 = [xi**2 for xi in Xlog]

# a1 = (m * sum(xy) - sum(Xlog) * sum(Ylog)) / (m * sum(x2) - (sum(Xlog))**2)
# a2 = (sum(Ylog) - a1 * sum(Xlog)) / m

# Ylog_pred = [a1 * Xlog[i] + a2 for i in range(m)]
# y_pred = [M.exp(yi) for yi in Ylog_pred]

# print(a1)
# print( {M.exp(a2)})

# plt.scatter(x, y, label='Data points')
# plt.plot(x, y_pred)
# plt.show()

#qus3
p=[0.5,1.0,1.5 , 2.0,2.5 , 3.0]
v=[1.62,1.00,0.75,0.62,0.52,0.46]
x=p
y=v
Xlog=[]
Ylog=[]
m = len(x)

for i in range(m):
    Xlog.append(M.log(x[i]))
    Ylog.append(M.log(y[i]))
xy = [Xlog[i] * Ylog[i] for i in range(m)]
x2 = [xi**2 for xi in Xlog]

a1 = (m * sum(xy) - sum(Xlog) * sum(Ylog)) / (m * sum(x2) - (sum(Xlog))**2)
a2 = (sum(Ylog) - a1 * sum(Xlog)) / m

Ylog_pred = [a1 * Xlog[i] + a2 for i in range(m)]
y_pred = [M.exp(yi) for yi in Ylog_pred]

print(a1)
print(M.exp(a2))

plt.scatter(x, y, label='Data points')
plt.plot(x, y_pred)
plt.show()
