import numpy as np
import scipy as sp
import matplotlib.pyplot as plt 
from scipy.interpolate import lagrange
from scipy import interp   #线性插值

x = np.linspace(0.2*np.pi,10)
y = np.sin(x)
plt.plot(x,y)

X = np.linspace(0.2*np.pi,40)
Y = interp(X,x,y)

plt.plot(x,y,marker = 'o')
plt.show()