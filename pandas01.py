import numpy as np 
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt 

s1 = Series({'A':144,'B':150,'C':100})
#print(s1)
#print(type(s1))
s2 = Series(data=np.random.randint(0,100,size=10),index=list('abcdefghij'))
#print(s2)
s3 = pd.DataFrame(data=np.random.randint(0,150,size=(10,3)),
                  index=list('ABCDEFGHIJ'),
                  columns=['PYTHON','MATH','ENGLISH'])
#print(s3)
#s3.to_csv('./data.txt')
#print(s3.values)
#print(s3.corr())   pearson系数
