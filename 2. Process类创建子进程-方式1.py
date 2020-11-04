from multiprocessing import Process, current_process
# Process是multiprocessing模块中的类，可以跨平台使用，而fork只能在Unix-like系统里调用
# Process会等待所有child processes都结束才会停止进程，而fork中的parent process不管那些
from time import sleep
import os

def func(name):
    
    print('process id:', os.getpid(), 'parent process:', os.getppid())

    for i in range(8):
        print('hello', name)
        sleep(1)

if __name__ == '__main__':
    #info('main line')
    p0 = current_process()
    print('current process id:', p0.pid, 'current process name', p0.name)
    p = Process(target=func, args=('bob',)) #Process类创建了p对象，该对象可以被当作进程
    p.start()
    print('this process id is %d, and its name is %s'%(p.pid, p.name))
    #p.join([timeout]) #等待child process执行多少秒再运行parent process，或不写的话干脆等到子进程完成
    p.join(4)
    print(p.is_alive()) #判断进程实例是否还在进行
    #p.terminate() #不管child process是否完成，立即终止
    print('---main process over---')
