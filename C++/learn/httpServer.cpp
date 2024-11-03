// compiler command 
// g++ -IC:\boost\boost_1_86_0 httpServer.cpp -o ./out/httpServer.exe -lWs2_32

#include <iostream>
#include <string>
#include <thread>
#include <fstream>
#include <boost/asio.hpp>

using namespace std;
using boost::asio::ip::tcp;

void session(tcp::socket sock){
    try {
        char data[1024]
        
        // 读取 HTML 文件内容到字符串中
        std::ifstream file(R"(C:\Just-For-Fun\Web\main.html)");
        if (!file.is_open()) {
            cerr << "Failed to open HTML file." << endl; 
            return;
        }

        // 读取整个文件内容
        std::string html_content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        file.close();

        // 准备 HTTP 响应头
        std::string response =
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Content-Length: " + std::to_string(html_content.size()) + "\r\n"
            "\r\n" + html_content;

        // 循环读取数据并处理请求
        while (true) {
            boost::system::error_code error;
            size_t length = sock.read_some(boost::asio::buffer(data), error);
            
            // 如果连接关闭，退出循环
            if (error == boost::asio::error::eof)
                break;
            else if (error)
                throw boost::system::system_error(error);

            // 发送响应
            boost::asio::write(sock, boost::asio::buffer(response));
        }
    } catch (exception& e) {
        cerr << "Exception in thread: " << e.what() << endl;
    }
}

int main() {
    try {
        boost::asio::io_context io_context;
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 8080));

        while (true) {
            tcp::socket sock(io_context);
            acceptor.accept(sock); // accept方法会阻塞主线程，直到有连接请求到达
            thread(session, move(sock)).detach();
        }
    } catch (exception& e) {
        cerr << "Exception: " << e.what() << endl;
    }
    return 0;
}
