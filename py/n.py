#!/usr/bin/env python3

import re
import subprocess
import math

# 运行free命令并获取输出结果
output = subprocess.check_output(["free", "-h"]).decode("utf-8")

# 在输出结果中查找包含"Mem:"的行
mem_line = next(line for line in output.split("\n") if "Mem:" in line)

# 使用正则表达式提取总内存大小的数字部分
total_mem_str = re.search(r"\d+\.*\d*", mem_line).group()

# 将字符串形式的内存大小转换为浮点数
total_mem_num = float(total_mem_str)

answer = math.sqrt(total_mem_num * 1024 * 1024 * 1024 * 0.6 / 8)

answer = int(answer)

# 输出总内存大小的数字
print(answer)
# print("{} ".format(answer))
