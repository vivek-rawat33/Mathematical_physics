
import matplotlib.pyplot as plt
import numpy as np
# def recurrence_relation(n,x):
#     p_0=0
#     p_1 =x
#     for i in range(1,n+1):
#         if n==0:
#             return p_0
#         elif n==1:
#             return p_1
#         p_prev2= p_0
#         p_prev1= p_1
        
#         for i in range(2,n+1):
#             p_current= ((2*i-1)*x*p_prev1-(i-1)*p_prev2)/i
#             p_prev2= p_prev1
#             p_prev1= p_current
#         return p_current
        
    
# x_values= np.linspace(-1,1,400)
# for n in range(6):
#     y_val=[recurrence_relation(n,x) for x in x_values]
#     plt.plot(x_values,y_val,label=f"n={n}")
# plt.title("Legendre")
# plt.legend()
# plt.grid(True)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def legendre_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre_poly(n - 1, x) - (n - 1) * legendre_poly(n - 2, x)) / n

x = np.linspace(-1, 1, 100)
plt.figure()
for n in range(6):
    y = [legendre_poly(n, xi) for xi in x]
    plt.plot(x, y, label=f'P_{n}(x)')

plt.legend()
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.title('Legendre Polynomials')
plt.grid()
plt.show()