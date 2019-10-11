def recuration(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("请输入一个整数："))
result=recuration(num)

print("%d的阶乘是%d"%(num,result))
