'''
查找名称时，按照 local，enclosed，global，built in的顺序
'''

#测试LEGB

#str="global str"
def outer():
    #str="outer"
    def inner():
        #str="inner"
        print(str)
        pass
    inner()
outer()