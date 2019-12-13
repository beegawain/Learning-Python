import numpy as np 
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt 

s1 = pd.DataFrame(data=np.random.randint(0,150,size=(10,3)),
                  index=pd.MultiIndex.from_product([list('ABCDE'),['期末','期中']]),
                  columns=['PYTHON','MATH','ENGLISH'])
print(s1)