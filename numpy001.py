#将最大值替换为10
import numpy as np 
nd1 = np.random.randint(1,100,size=10)
print(nd1)
v_value = nd1.max()
print(v_value)
cond = nd1 == nd1.max()
print(cond)
nd1[cond] = 10
print(nd1)
