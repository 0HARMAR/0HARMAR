import socket

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = "127.0.0.1"
print(host)
# 设置端口号
port = 7777

# 绑定端口号
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

print(f"等待客户端连接...")

while True:
    # 建立客户端连接
    client_socket, addr = server_socket.accept()
    print(f"连接地址: {str(addr)}")

    # 发送欢迎消息给客户端
    message = "hhhhh"
    client_socket.send(message.encode('utf-8'))

    # 关闭连接
    client_socket.close()
