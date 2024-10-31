import re

maps_file = open("/proc/self/maps", 'r')
mem_file = open("/proc/self/mem", 'rb', 0)
output_file = open("self1.dump", 'wb')

for line in maps_file.readlines():  # 遍歷每個映射區域
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    print(m)
    if m.group(3) == 'r':  # 如果這是可讀區域
        start = int(m.group(1), 16)
        end = int(m.group(2), 16)
        mem_file.seek(int(0x400000))  # 尋找區域起始位置
        chunk = mem_file.read(1)  # 讀取區域內容
        output_file.write(chunk)  # 將內容轉儲到輸出文件

maps_file.close()
mem_file.close()
output_file.close()
