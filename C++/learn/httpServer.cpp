#include <iostream>
#include <string>
#include <thread>
#include <boost/asio.hpp>

using namespace std;
using boost::asio::ip::tcp;

void session(tcp::socket sock) {
    try {
        char data[1024]
        while (true){
            boost::system::error_code error; //创建一个boost::system::error_code类型的变量
            size_t length = sock.read_some(boost::asio::buffer(data), error);
            if (error == boost::asio::error::eof) break; // Connection closed cleanly by peer
            else if (error) throw boost::system::system_error(error); // Some other error

            string response = "HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!";
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
            acceptor.accept(sock);
            thread(session, move(sock)).detach();
        }
    } catch (exception& e) {
        cerr << "Exception: " << e.what() << endl;
    }
    return 0;
}
