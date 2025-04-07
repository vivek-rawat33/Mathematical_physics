import matplotlib.pyplot as plt
import math as M
x=[i for i in range(1,9)]
y=[12,26,33,47,52,64,75,86]
sigma_y=[3,2,3,4,4,2,1,2]
xy_sigma=[]
weight_squ=[]
x_2=[]
y_sigma2=[]
x_sigma2=[]
x2_sigma2=[]
for i in range(len(x)):
    xy_sigma.append(x[i]*y[i]/sigma_y[i]**2)
    weight_squ.append(1/sigma_y[i]**2)
    x_2.append(x[i]**2)
    x_sigma2.append(x[i]*weight_squ[i])
    y_sigma2.append(y[i]*weight_squ[i])
    x2_sigma2.append(x_2[i]*weight_squ[i])
a1=(sum(weight_squ)*sum(xy_sigma) - sum(x_sigma2)*sum(y_sigma2))/(sum(weight_squ)*sum(x2_sigma2) - (sum(x_sigma2))**2)
a0= (sum(y_sigma2)-a1*(sum(x_sigma2)))/sum(weight_squ)
print(f"slope is {a1}")
print(f"intercept is {a0}")
y_pred=[]
for i in range(len(x)):
    y_pred.append(a0 + x[i]*a1)

ao_error = M.sqrt(sum(x2_sigma2) / (sum(weight_squ) * (sum(weight_squ) * sum(x2_sigma2) - sum(x_sigma2)**2)))
a1_error = M.sqrt(sum(weight_squ) / (sum(weight_squ) * sum(x2_sigma2) - sum(x_sigma2)**2))


print(f"error in a0 is {ao_error}")
print(f"error in a1 is {a1_error}")
plt.scatter(x,y)
plt.xlabel("x_label")
plt.ylabel("y_label")
plt.plot(x,y_pred)
plt.show()



#qus 2
# x=[203,58,210,202,198,158,165,201,157,131,166,160,186,125,218,146]
# y=[495,173,479,504,510,416,393,442,317,311,400,337,423,344,533,344]
# sigma_y=[21,15,27,14,30,16,14,25,52,16,34,31,42,26,16,22]
# xy_sigma=[]
# weight_squ=[]
# x_2=[]
# y_sigma2=[]
# x_sigma2=[]
# x2_sigma2=[]
# for i in range(len(x)):
#     xy_sigma.append(x[i]*y[i]/sigma_y[i]**2)
#     weight_squ.append(1/sigma_y[i]**2)
#     x_2.append(x[i]**2)
#     x_sigma2.append(x[i]*weight_squ[i])
#     y_sigma2.append(y[i]*weight_squ[i])
#     x2_sigma2.append(x_2[i]*weight_squ[i])
# a1=(sum(weight_squ)*sum(xy_sigma) - sum(x_sigma2)*sum(y_sigma2))/(sum(weight_squ)*sum(x2_sigma2) - (sum(x_sigma2))**2)
# a0= (sum(y_sigma2)-a1*(sum(x_sigma2)))/sum(weight_squ)
# print(f"slope is {a1}")
# print(f"intercept is {a0}")
# y_pred=[]
# for i in range(len(x)):
#     y_pred.append(a0 + x[i]*a1)
# ao_error = M.sqrt(sum(x2_sigma2) / (sum(weight_squ) * (sum(weight_squ) * sum(x2_sigma2) - sum(x_sigma2)**2)))
# a1_error = M.sqrt(sum(weight_squ) / (sum(weight_squ) * sum(x2_sigma2) - sum(x_sigma2)**2))

# print(f"error in a0 is {ao_error}")
# print(f"error in a1 is {a1_error}")
# plt.scatter(x,y)
# plt.xlabel("x_label")
# plt.ylabel("y_label")
# plt.plot(x,y_pred)
# plt.show()
