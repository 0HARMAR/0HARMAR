#include <iostream>
#include <stdexcept>

void divide(double a, double b) {
    if (b == 0) {
        throw std::invalid_argument("Division by zero"); // 抛出异常
    }
    std::cout << "Result: " << a / b << std::endl;
}

int main() {
    try {
        divide(10, 0); // 可能引发异常
    } catch (const std::invalid_argument& e) { // 捕获并处理异常
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
