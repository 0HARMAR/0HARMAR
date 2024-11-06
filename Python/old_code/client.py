import socket

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务器的主机名和端口号
host = "127.0.0.1"
port = 7777

# 连接服务器
client_socket.connect((host, port))

# 接收欢迎消息
welcome_message = client_socket.recv(1024).decode('utf-8')
print("接收到的欢迎消息:", welcome_message)

# 关闭连接
client_socket.close()
