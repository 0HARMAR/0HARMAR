import sys
import socket
import threading

HEX_FILTER = ''.join([chr(i) if len(repr(chr(i))) == 3 else '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()
    results = []
    for i in range(0, len(src), length):
        word = src[i:i+length]
        printable = word.translate(HEX_FILTER)
       
        hexa = ' '.join([f'{ord(c):02x}' for c in word])  # 02x 确保输出两位十六进制
        print(hexa)
        hexwidth = length * 3# 修改变量名为 hexwidth
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')  # 添加缺失的空格符号
    if show:
        for line in results:
            print(line)
    else:
        return results
    
def receive_from(connection):
    buffer=b""
    connection.settimeout(5)
    try:
        while True:
                data=connection.recv(4096)
                if not data:
                    break
                buffer +=data
    except Exception as e:
        pass
    return buffer