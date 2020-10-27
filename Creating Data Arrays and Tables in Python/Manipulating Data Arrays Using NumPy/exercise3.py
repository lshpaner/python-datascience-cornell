import numpy as np

x = np.arange(10,20)
y = np.linspace(0.,1.,10)
z = np.arange(0,10).reshape((5,2))
print(x)
print(y)
print(z)

a = x+x
b = z/100
c = x*y

w1 = np.sum(z, axis=0)
w2 = np.sum(z, axis=1)
zmean = np.mean(z)