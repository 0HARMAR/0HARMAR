# 定义字节序列
byte_sequence = [
    0x48, 0xc7, 0xc0, 0x00, 0x00, 0x00, 0x00,  # mov $0x0, %rax
    0x48, 0xc7, 0xc7, 0x01, 0x00, 0x00, 0x00,  # mov $0x1, %rdi
    0x48, 0xc7, 0xc6, 0x00, 0x00, 0x00, 0x00,  # mov $0x0, %rsi
    0x48, 0xc7, 0xc2, 0x1c, 0x00, 0x00, 0x00,  # mov $0x1c, %rdx
    0x0f, 0x05,                                # syscall
    0x48, 0xc7, 0xc0, 0x00, 0x00, 0x00, 0x00,  # mov $0x0, %rax
    0x48, 0x31, 0xff,                          # xor %rdi, %rdi
    0x0f, 0x05                                 # syscall
]

# 将字节序列写入二进制文件
with open('output.bin', 'wb') as f:
    f.write(bytearray(byte_sequence))

print("字节序列已写入 output.bin 文件。")

