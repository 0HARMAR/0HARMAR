基本定义语法
auto lambda = []() {
        std::cout << "Hello, Lambda!" << std::endl;
    };

auto自动推断lambda函数的类型是std::function
[]表示lambda函数的变量捕获列表，它允许 Lambda 函数捕获外部变量，这里是空
1.按值捕获
int x = 10;
auto lambda = [x]() {
    std::cout << "Value of x: " << x << std::endl; // 使用 x 的副本
};
按值捕获使用的只是外部变量的值，不会修改它
2.按引用捕获
int x = 10;
auto lambda = [&x]() {
    x++; // 修改外部 x
};
lambda();
std::cout << "Updated value of x: " << x << std::endl; // 输出：Updated value of x: 11
3.捕获全部变量
int a = 1, b = 2;
auto lambdaByValue = [=]() {
    std::cout << "a: " << a << ", b: " << b << std::endl; // 捕获副本
};

auto lambdaByReference = [&]() {
    a++; // 修改原始变量
    b++;
};

lambdaByValue(); // 输出：a: 1, b: 2
lambdaByReference();
std::cout << "a: " << a << ", b: " << b << std::endl; // 输出：a: 2, b: 3
lambda只会捕获定义在它前面的变量
()表示函数参数列表

函数的返回值类型可以不指定，可以通过自动类型推导
但也可以显式指定，例如
 // 显式指定返回类型为 double
    auto addWithDouble = [](int x, int y) -> double {
        return x + y + 0.5;
    };