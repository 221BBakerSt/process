from multiprocessing import Pool
import time
import os

def sum_square(number):
    s = 0
    for i in range(number):
        s += i*i
    return s

def sum_square_with_sp(numbers):
    start_time = time.perf_counter()

    result = []
    for i in numbers:
        result.append(sum_square(i))

    end_time = time.perf_counter()
    print(f"Serial process id {os.getpid()} taking {round(end_time - start_time, 3)}s. Parent process id {os.getppid()}")


def sum_square_with_mp(numbers):
    start_time = time.perf_counter()

    p = Pool()
    result = p.map(sum_square, numbers)

    # 关闭进程池之后不再接收新任务
    p.close()
    # 等待pool里所有子进程执行完成，必须放在close()之后
    p.join()

    end_time = time.perf_counter()
    print(f"Multiprocess id {os.getpid()} taking {round(end_time - start_time, 3)}s. Parent process id {os.getppid()}")


if __name__ == "__main__":
    # 不能大于10000了!
    numbers = range(10000)
    sum_square_with_mp(numbers)
    sum_square_with_sp(numbers)
