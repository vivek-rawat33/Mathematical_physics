# import matplotlib.pyplot as plt
# import math

# # Data points
# p = [i / 2 for i in range(1, 7)]
# v = [1.62, 1.00, 0.75, 0.62, 0.52, 0.46]

# # p=[i for i in range(1951,1958)]
# # v=[201,263,314,395,427,504,612]

# # Logarithmic transformation
# X = [math.log(i) for i in p]
# Y = [math.log(i) for i in v]

# # Calculate XY and X^2
# XY = [X[i] * Y[i] for i in range(len(p))]
# X2 = [i ** 2 for i in X]

# # Calculate coefficients a1 and a0
# n = len(X)
# a1 = (n * sum(XY) - sum(X) * sum(Y)) / (n * sum(X2) - sum(X) ** 2)
# a0 = (sum(Y) - a1 * sum(X)) / n

# # Predict values
# v_pred = [math.exp(a0 + a1 * (i) )for i in X]

# print(f'slope = {a1}')
# print(f'intercept = {math.exp(a0)}')
# # Plotting
# plt.scatter(p, v, label='Original Data')
# plt.plot(p, v_pred, color="r", label='Fitted Line')
# plt.legend()
# plt.show()



import matplotlib.pyplot as plt
import math
import numpy as np

# Data points
p = [1,1.2,1.4,1.6,1.8,2]
v = [5,8.7,13.2,20.5,29.5,42]

# Logarithmic transformation
X = [math.log(i) for i in p]
Y = [math.log(i) for i in v]

# Calculate XY and X^2
XY = [X[i] * Y[i] for i in range(len(p))]
X2 = [i ** 2 for i in X]

# Calculate coefficients a1 and a0
n = len(X)
a1 = (n * sum(XY) - sum(X) * sum(Y)) / (n * sum(X2) - sum(X) ** 2)
a0 = (sum(Y) - a1 * sum(X)) / n

# Create smoother curve with more points
p_smooth = np.linspace(min(p), max(p), 100)  # 100 points between min and max
X_smooth = [math.log(i) for i in p_smooth]
v_pred_smooth = [math.exp(a0 + a1 * x) for x in X_smooth]

print(f'slope = {a1}')
print(f'intercept = {math.exp(a0)}')

# Plotting
plt.scatter(p, v, label='Original Data')
plt.plot(p_smooth, v_pred_smooth, color="r", label='Fitted Line')
plt.legend()
plt.show()