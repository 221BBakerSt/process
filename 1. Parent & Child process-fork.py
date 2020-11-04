import os
from time import sleep

# fork只适用于Unix-like systems
ret = os.fork()
# parent process的返回值，就是刚创建出的child process的id
print(ret)
if ret > 0:
    print(f'Parent process {os.getpid()}')

else:
    print(f"Child process {os.getpid()}; its father's process {os.getppid()}")
