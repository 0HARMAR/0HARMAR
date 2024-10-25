import socket

def start_client():
    # 创建一个 TCP 套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到服务器
    client_socket.connect(('127.0.0.1', 65432))
    
    # 发送数据
    client_socket.sendall(b'Hello, server!')

    # 接收响应
    data = client_socket.recv(1024)
    print(f"收到响应: {data.decode()}")

    # 关闭套接字
    client_socket.close()

if __name__ == "__main__":
    start_client()
