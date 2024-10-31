#include <iostream>

int main() {
    // 输出欢迎信息
    std::cout << "Hello, World!" << std::endl;

    // 定义两个变量
    int num1, num2;

    // 提示用户输入第一个数字
    std::cout << "Enter the first number: ";
    std::cin >> num1;

    // 提示用户输入第二个数字
    std::cout << "Enter the second number: ";
    std::cin >> num2;

    // 计算和
    int sum = num1 + num2;

    // 输出结果
    std::cout << "The sum of " << num1 << " and " << num2 << " is " << sum << std::endl;

    // 控制结构示例
    if (sum % 2 == 0) {
        std::cout << "The sum is an even number." << std::endl;
    } else {
        std::cout << "The sum is an odd number." << std::endl;
    }

    return 0;
}

