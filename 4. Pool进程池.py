from multiprocessing import Pool
import time
import os

def worker(msg):
    t_start = time.time()
    print(msg)
    time.sleep(1)
    t_end = time.time()
    print(f'Process id {os.getpid()} takes {t_end - t_start}s. Parent id {os.getppid()}\n')

if __name__ == "__main__":
    print("---start---")

    # 定义一个进程池，和最大进程数
    p = Pool(4)
    for i in range(12):
        # p.apply_async(要调用的目标, (传递给目标的参数元组,))
        p.apply_async(func = worker, args = (f'---{i}---',))
        # p.apply(worker, (f'---{i}---',)) #堵塞式执行任务
    # 关闭进程池之后不再接收新任务
    p.close()
    # 等待pool里所有子进程执行完成，必须放在close()之后
    # 主进程默认不会等待进程池中的任务结束，所以如果没有join()进程池的任务就不会执行了
    p.join()

    print("---end---")
