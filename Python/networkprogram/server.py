import socket

def start_server():
    # 创建一个 TCP 套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定到地址和端口
    server_socket.bind(('127.0.0.1', 65432))
    
    # 开始监听连接
    server_socket.listen()
    print("服务器正在监听...")

    while True:
        # 接受客户端连接
        client_socket, addr = server_socket.accept()
        print(f"连接来自: {addr}")

        # 接收数据
        data = client_socket.recv(1024)
        print(f"收到数据: {data.decode()}")

        # 发送响应
        client_socket.sendall(b'Hello, client!')

        # 关闭客户端连接
        client_socket.close()

if __name__ == "__main__":
    start_server()
