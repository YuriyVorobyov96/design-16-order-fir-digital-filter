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

with open ('C:\\Users\\darth\\Desktop\\Python_codes\\ish.txt', 'w') as out:
	for z in Xn:
		print(z, file=out)

plt.plot(T, Xn,linewidth=0.5, color='r')
plt.show() 
