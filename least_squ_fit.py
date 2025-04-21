import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7,8]
# y=[12,26,33,47,52,64,75,86]
# xy=[]
# m=len(x)
# for i in range(m):
#     xy.append(x[i]*y[i])
# x2=[i**2 for i in x]
# a1= (m*sum(xy) - sum(x)*sum(y))/(m*sum(x2) - (sum(x))**2)
# a2= (sum(y) - a1*sum(x))/m
# y_pred = []


# for i in range(m):
#     y_pred.append(a1*x[i]+a2)
# print(f"intercept = {a1}")
# print(f"slope = {a2}")
# plt.scatter(x,y)
# plt.plot((min(x),max(x)),(min(y_pred),max(y_pred)))
# plt.show()

  
  
# x=[203,58,210,202,198,158,165,201,157,131,166,160,186,125,218,146]
# y=[495,173,479,504,510,416,393,442,317,311,400,337,423,344,533,344]
# xy=[]
# m=len(x)
# for i in range(m):
#     xy.append(x[i]*y[i])
# x2=[i**2 for i in x]
# a1= (m*sum(xy) - sum(x)*sum(y))/(m*sum(x2) - (sum(x))**2)
# a2= (sum(y) - a1*sum(x))/m
# y_pred = []
# for i in range(m):
#     y_pred.append(a1*x[i]+a2)
# print(f"intercept = {a1}")
# print(f"slope = {a2}")
# plt.scatter(x,y)
# plt.plot((min(x),max(x)),(min(y_pred),max(y_pred)))
# plt.show()

x=[50,70,100,120]
y=[12,15,21,25]
xy=[]
m=len(x)
for i in range(m):
    xy.append(x[i]*y[i])
x2=[i**2 for i in x]
a1= (m*sum(xy) - sum(x)*sum(y))/(m*sum(x2) - (sum(x))**2)
a2= (sum(y) - a1*sum(x))/m
y_pred = []
for i in range(m):
    y_pred.append(a1*x[i]+a2)
print(f"intercept = {a1}")
print(f"slope = {a2}")
plt.scatter(x,y)
plt.plot((min(x),max(x)),(min(y_pred),max(y_pred)))
plt.show()

