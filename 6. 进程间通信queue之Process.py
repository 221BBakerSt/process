from multiprocessing import Queue, Process
import time
import os


def write(q, msg):
    print(f"Writer starts. Process id {os.getpid()}, parent process id {os.getppid()}")
    for value in msg:
        q.put(value)
        print(f"{value} is put into the queue")
        time.sleep(1)


def read(q):
    print(f"Reader starts. Process id {os.getpid()}, parent process id {os.getppid()}")
    # print(q.qsize()) # qsize()结果不可靠，而且在Unix-like systems会报错，一般不用
    # 所以用循环再判断是否为空
    while 1:
        if not q.empty():
            value = q.get(True)
            print(f"Get {value} from the queue")
            time.sleep(1)
        else:
            print("No value now")
            break


if __name__ == "__main__":
    # parent process creates the queue, and pass the tasks to child processes
    q = Queue()
    pw = Process(target=write, args=(q, ("-11-", "-22-", "-33-")))
    pr = Process(target=read, args=(q,))
    # 启动子程序pw写入
    pw.start()
    pw.join()
    pr.start()
    pr.join()
