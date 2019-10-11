#可调用对象，即该对象可以像函数一样被调用


class SalaryAccount:
     #计算工资类
    def __call__(self,salary):
        print("算工资！")
        yearSalary=salary*12
        daySalary=salary//22.5 #国家规定每个月的平均工作天数

        return dict(yearSalary=yearSalary,daySalary=daySalary)

a=SalaryAccount()
print(a(30000))
    