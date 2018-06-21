import os
import time

pid = os.fork()

num = 0

# 每个进程中的所有数据都各自拥有一份，互不影响（包括全局变量）
if pid == 0:
    num += 1
    print("----子线程%d---"%num)
    time.sleep(1)
else:
    num += 1
    print("---父线程%d---"%num)
    time.sleep(1)

print("----over----")