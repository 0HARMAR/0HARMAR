import socket

def start_server():
    # 创建一个socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 获取本地主机名
    host = '127.0.0.1'
    port = 12345
    
    # 绑定端口
    server_socket.bind((host, port))
    
    # 设置最大连接数，超过后排队
    server_socket.listen(5)
    
    print(f"服务器启动，在 {host}:{port} 等待连接...")
    
    while True:
        # 建立客户端连接
        client_socket, addr = server_socket.accept()
        print(f"连接地址: {addr}")
        
        # 接收数据
        data = client_socket.recv(1024).decode('utf-8')
        print(f"接收到的数据: {data}")
        
        # 发送数据
        response = '服务器已收到消息'
        client_socket.send(response.encode('utf-8'))
        
        # 关闭连接
        client_socket.close()

if __name__ == "__main__":
    start_server()

