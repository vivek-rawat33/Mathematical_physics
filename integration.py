
# y = x**2 + 3*x -5
import matplotlib.pyplot as plt
import numpy as np
x= int(input("Number of points between a and b :"))
if(x ==1 or x==0):
    print("please put some large values")
x_val=np.linspace(0,5,x)
sum2=0
h=5/(x-1)
for i in range(1,len(x_val)-1):
    sum2+=(h*((x_val[i]**2) +3*x_val[i] -5))
sum1 = (h/2)*(x_val[0]**2 + 3*x_val[0] - 5 + x_val[x-1]**2 + 3*x_val[x-1] - 5)

result = sum1 + sum2

print("The approximate value of the definite integral is : ",result)
