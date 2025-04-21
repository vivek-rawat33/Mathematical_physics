
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