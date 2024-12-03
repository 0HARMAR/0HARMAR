package main

import (
	"bufio"
	"fmt"
	"net"
	"strings"
	"sync"
)

var (
	clients   = make(map[net.Conn]string) // 维护连接的客户端和用户名
	broadcast = make(chan string)         // 广播消息的通道
	mutex     = sync.Mutex{}              // 保护 clients 的互斥锁
)

func main() {
	// 启动TCP服务器，监听本地8000端口
	listener, err := net.Listen("tcp", ":8000")
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer listener.Close()

	// 启动广播消息的协程
	go broadcastMessages()

	fmt.Println("Chat server started on port 8000...")

	for {
		// 接受客户端连接
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}

		// 处理客户端连接
		go handleClient(conn)
	}
}

// 处理客户端连接
func handleClient(conn net.Conn) {
	defer conn.Close()

	// 提示用户输入用户名
	conn.Write([]byte("Enter your username: "))
	username, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		fmt.Println("Error reading username:", err)
		return
	}
	username = strings.TrimSpace(username)

	// 保存客户端信息
	mutex.Lock()
	clients[conn] = username
	mutex.Unlock()

	// 广播新用户加入
	broadcast <- fmt.Sprintf("%s joined the chat", username)

	// 监听客户端发送的消息
	for {
		message, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			// 用户断开连接，删除客户端
			mutex.Lock()
			delete(clients, conn)
			mutex.Unlock()
			broadcast <- fmt.Sprintf("%s left the chat", username)
			return
		}

		// 广播用户的消息
		broadcast <- fmt.Sprintf("%s: %s", username, strings.TrimSpace(message))
	}
}

// 广播消息给所有客户端
func broadcastMessages() {
	for {
		// 等待广播的消息
		message := <-broadcast

		// 将消息发送给所有客户端
		mutex.Lock()
		for conn := range clients {
			_, err := conn.Write([]byte(message + "\n"))
			if err != nil {
				fmt.Println("Error writing to client:", err)
				conn.Close()
				delete(clients, conn)
			}
		}
		mutex.Unlock()
	}
}
