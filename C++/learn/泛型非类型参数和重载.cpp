#include <iostream>

template <typename T, int size>
class Array {
public:
    T data[size];
     // 重载 [] 运算符
    T& operator[](int index) {
        return data[index]; // 返回数组元素的引用
    }
};

int main(){
    Array<int,5> intArray;
    for (int i = 0; i < 5; ++i) {
        intArray[i] = i + 1; // 设置数组元素
    }

    for (int i = 0; i < 5; ++i) {
        std::cout << intArray[i] << " "; // 输出数组元素
    }
    std::cout << std::endl;

    return 0;
}