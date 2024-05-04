# 打开文件
import json
import statistics

with open("result.txt", "r") as file:

    gflops_list = []

    # 逐行读取文件内容
    for line in file:
        # 去除行末尾的换行符
        line = line.strip()
        
        # 判断行是否为空
        if line:
            # 使用空格分隔字段
            fields = line.split()
            
            # 判断字段数量是否符合格式要求
            if len(fields) == 7 and fields[0].startswith("WR"):
                gflops = fields[-1]
                gflops_list.append(float(gflops))
                # print("提取到的 Gflops 数字为:", gflops)

    # 对 Gflops 数字列表进行排序
    # gflops_list.sort()
    
    # 打印排序后的 Gflops 数字列表
    # print("排序后的 Gflops 数字列表:", gflops_list)

    print("Result: ")

    # 计算最大值
    max_value = max(gflops_list)

    # 计算平均值
    average_value = statistics.mean(gflops_list)

    # 计算方差
    variance_value = statistics.variance(gflops_list)

    print("The Highest Gflops is {}".format(max_value))

    print("The Average Gflops is {}".format(average_value))

    # 创建包含统计数据的字典
    statistics_dict = {
        "gflops_list": gflops_list,
        "max_value": max_value,
        "average_value": average_value,
        "variance_value": variance_value
    }

    # 指定输出文件路径
    output_file = "statistics.json"

    # 将字典转换为 JSON 格式并写入文件
    with open(output_file, "w") as file:
        json.dump(statistics_dict, file, indent=4)

    print("统计数据已成功写入到文件:", output_file)

    # print(numbers)
 