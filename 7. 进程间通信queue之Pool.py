from multiprocessing import Manager, Pool
import time, os

def writer(q, msg):
    print(f'Writer starts. Process id {os.getpid()}, parent process id {os.getppid()}')
    for value in msg:
        q.put_nowait(value)
        print(f'{value} is put into the pool')
        time.sleep(1)

def reader(q):
    print(f'Reader starts. Process id {os.getpid()}, parent process id {os.getppid()}')
    while 1:
        if not q.empty():
            value = q.get_nowait()
            print(f'Get {value} from the pool')
            time.sleep(1)
        else:
            print('No value now')
            break

if __name__ == '__main__':
    print('---start---')
    # 使用Manager创建个对象，对象中的队列
    q = Manager().Queue()
    p = Pool(3)
    for _ in range(5):
        # 把队列q扔到进程池中的一个任务
        p.apply_async(writer, (q, [str(x)*3 for x in range(5)]))
        p.apply_async(reader, (q,))
    p.close()
    p.join()
    print('---end---')