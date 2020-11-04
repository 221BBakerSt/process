from multiprocessing import Process
import os
import time

class NewProcess(Process):

    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        # Override run method in Process class
        t_start = time.perf_counter()
        print(f'This process id is {os.getpid()}, the parent process id is {os.getppid()}')
        for i in range (5):
            print('---child process---')
            time.sleep(self.interval)
        t_stop = time.perf_counter()
        print(f'The child process is over, taking up {round(t_stop - t_start, 3)}s')

if __name__ == '__main__':
    t_start = time.perf_counter()
    print(f'This process id is {os.getpid()}')
    p = NewProcess(1)
    p.start()
    # p.join() # 主进程是否等待子进程结束
    t_stop = time.perf_counter()
    print(f'the process {os.getpid()} is over, taking up {round(t_stop - t_start, 3)}s')
