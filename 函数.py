def print_max(a,b):
    '''用于比较两个数之间的大小'''    #说明定义的函数的具体含义
    if a>b :
        print("最大值为：",a)
    elif b>a :
        print("最大值为：",b)
    elif a==b:
        print("两束相同")

print_max(7,7)
print_max(74,77777)  #函数直接调用

help(print_max.__doc__)