#include <iostream>

int main() {
    auto lambda = []() {
        std::cout << "Hello, Lambda!" << std::endl;
    };

    lambda(); // 调用 Lambda 函数
    return 0;
}
