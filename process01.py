from multiprocessing import Process
#process = Process(target=function,name=name of process,args=(给函数传递的参数))
#process 对象
#对象调用的方法：
#process.start() 启动进程并执行任务
#process.run() 只执行任务没有启动进程
#terminate()终止

#自定义进程

class MyProcess(Process):
    def run(self):
        n=1
        while True:
            print('{0}------>自定义进程，次数：{1}'.format(self.name,n))
            n+=1

if __name__ == '__main__':
    p=MyProcess('XiaoHu')
    p.start()
    p1=MyProcess('UZI')