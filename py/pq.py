import multiprocessing
import psutil
import math


def split_closest(number):
    # 计算给定数的平方根
    sqrt = math.sqrt(number)

    # 从平方根开始递减寻找最小因子
    for i in range(math.floor(sqrt), 1, -1):
        if number % i == 0:
            factor1 = i
            factor2 = number // i
            break
    else:
        # 如果没有找到合适的因子，则将给定数分解为 1 和其本身
        factor1 = 1
        factor2 = number

    return factor1, factor2


# 获取CPU的个数
cpu_num = multiprocessing.cpu_count()

# 返回CPU的个数作为整数值
cpu_num = int(cpu_num)

# 获取CPU的物理核心数
cpu_cores = psutil.cpu_count(logical=False)

answer1 = cpu_cores * cpu_num

answer2 = 2 * cpu_num

# print(cpu_cores)
# print(cpu_num)
# print(answer)

# test
# answer = 99

p, q = split_closest(answer2)

print("{} {}".format(p, q))

# print(p)
# print(q)
