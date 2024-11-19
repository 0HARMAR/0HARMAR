#include <iostream>

template <typename T, int size>
class Array {
public:
    Array(T A) : a(A){}
    T a;
    int size_ = size;
    void infoSize(){
        std::cout << size_;
    }
    void infoA(){
        std::cout << a;
    }
};

template <typename Type>
struct stct
{
    int a;
    int b;
};

int main(){
    struct stct s = {1,2};
    std::cout << s.a << std::endl;
    Array<int,5> array(10);
    array.infoA();
    std::cout << std::endl;
    array.infoSize();
}