import numpy as np
import matplotlib.pyplot as plt

def function(T, A, F):
    result = 0
    for i in range(7):
        result += A[i] * np.sin(2 * np.pi * F[i] * T)
    return result

F = np.array([2000, 4000, 5000, 7000, 9000, 12000, 15000])
A = np.array([11, 15, 12, 13, 21, 10, 9])

Fmax = np.ndarray.max(F)
Fd = 2*Fmax
Td = 1 / Fd
T = np.arange(0, Td*1024, Td)

Xn = np.empty_like(T)
for i in range(1024):
    Xn[i] = function(T[i], A, F)

h = np.array([
3.42591553E-0003,
1.98488129E-0002,
-5.43602554E-0002,
2.56355684E-0002,
6.93667396E-0002,
-6.39440064E-0002,
-1.63419803E-0001,
4.29283935E-0001,
4.29283935E-0001,
-1.63419803E-0001,
-6.39440064E-0002,
6.93667396E-0002,
2.56355684E-0002,
-5.43602554E-0002,
1.98488129E-0002,
3.42591553E-0003
])

Xfiln = np.zeros_like(T)
for i in range(1024):
    for j in range(16):
        Xfiln[i] += h[j]*function(T[i] - Td, A, F)

plt.plot(T, Xfiln,linewidth=0.5, color='r')
plt.plot(T, Xn,linewidth=0.5, color='r')
plt.show()
