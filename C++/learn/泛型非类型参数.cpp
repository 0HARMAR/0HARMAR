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

int main(){
    Array<int,5> array(10);
    array.infoA();
    std::cout << std::endl;
    array.infoSize();
}