import socket

def start_client():
    # 创建一个socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到服务器的公网IP和端口
    server_ip = '47.121.210.221'  # 替换为你的服务器公网IP
    server_port = 12345
    
    client_socket.connect((server_ip, server_port))
    print("connected!")
    # 发送数据
    message = 'Hello, Server!'
    client_socket.send(message.encode('utf-8'))
    
    # 接收数据
    response = client_socket.recv(1024).decode('utf-8')
    print(f"来自服务器的响应: {response}")
    
    # 关闭连接
    client_socket.close()

if __name__ == "__main__":
    start_client()
