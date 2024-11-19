#include <iostream>
#include <vector>
using namespace std;

// 测试是否可以进行双层遍历
void iterator_test(vector<int> numbers){
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        size_t index = std::distance(numbers.begin(), it); //获取遍历的Index
        if (index == 2){
            cout << *it << endl;
            for(auto it_ = next(it);it_ != numbers.end(); ++it_){
                cout << *it_ << endl;
            }

        }
    }
}
int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // 添加元素
    numbers.push_back(6);

    // 使用 range-based for 循环遍历
    std::cout << "Elements in vector: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 使用迭代器遍历
    std::cout << "Elements using iterator: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        size_t index = std::distance(numbers.begin(), it); //获取遍历的Index
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // test
    iterator_test(numbers);

    return 0;
}
