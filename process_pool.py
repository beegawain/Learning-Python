from multiprocessing import Pool
from random import random
import time

def task(task_name):
    print('Start doing task! -- ',task_name)
    start=time.time()
    time.sleep(random()*2)
    end=time.time()
    print('End Task,time is:',(end-start))

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['Listening music','Watching TV','Washing Clothes','Playing game','run','make love']
    for task in tasks:
        pool.apply_async(task,args=(task,))
    pool.close()
    pool.join()

    print('OVER!')