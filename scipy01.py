import numpy as np
import scipy as sp
from scipy.fftpack import fft2,ifft2
import matplotlib.pyplot as plt 
from scipy import matrix   #矩阵

a = matrix(np.random.randint(0,10,size=(4,5)))
b = matrix(np.random.randint(0,10,size=(5,4)))
c = a.dot(b)
print(a)
#print(b)
#print(c)
print('*'*10)
#稀松矩阵，大部分是0，小部分是非0数据 节省内存
from scipy import sparse
s1 = sparse.csc_matrix(a)
print(s1)
print('*'*10)
sparse.save_npz('./sparse.npz',s1)
s2 = sparse.csr_matrix(a)
print(s2)