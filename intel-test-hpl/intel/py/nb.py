import cpuinfo

def get_cache_alignment():
    info = cpuinfo.get_cpu_info()
    cache_alignment = info['l2_cache_line_size']
    return cache_alignment

# 获取缓存对齐值
cache_alignment = get_cache_alignment()
cache_alignment = cache_alignment / 2
cache_alignment = int(cache_alignment)
print(cache_alignment)
# print("{} ".format(cache_alignment))