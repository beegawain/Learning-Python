#可变参数
# *a：将多个参数收集到一个“元组”对象中
# **a：将多个参数收集到一个“字典”对象中


def fun(a,b,*c,**d):
    print(a,b,c,d)

fun(10,20,30,40,name='BJW',age=18)


#若将可变参数放在前面，则后面的数要强制命名

'''
def fun(*a,b):
    print(a,b)
fun(1,2)

会报错！！
'''
def fun(*a,b=2):
    print(a,b)
fun(1,2)

#所以，尽量不要这样写
