#析构方法，释放对象占用的资源，例如：打开的文件资源、网络连接
#实现自动的垃圾回收，当对象没有被引用时，由垃圾回收器调用__del__

class Person:
    def __del__(self):
        print("销毁对象{0}".format(self))

p1=Person()
p2=Person()

del p2
print("程序结束")