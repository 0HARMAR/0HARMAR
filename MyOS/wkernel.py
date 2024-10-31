#!/usr/bin/env python3

import struct

# 汇编指令
instructions = [
    0x48, 0xc7, 0xc0, 0x01, 0x00, 0x00, 0x00,
    0x48, 0xc7, 0xc3, 0x02, 0x00, 0x00, 0x00,
    0x48, 0x01, 0xc3
]

# 磁盘镜像文件名
xv6 = "./xv6.img"

# 扇区大小
sector_size = 512

# 第二个扇区的起始位置
start_position = sector_size

# 打开磁盘镜像文件
with open(xv6, "r+b") as f:
    # 移动到第二个扇区的起始位置
    f.seek(start_position)
    
    # 写入汇编指令
    f.write(bytearray(instructions))

print("汇编指令已成功写入磁盘镜像文件的第二个扇区。")

