需添加头文件
#include <vector>

定义语法:
std::vector<type> varName = {value1,value2...}
例子:
 std::vector<int> numbers = {1, 2, 3, 4, 5};

 添加元素:
// 添加元素
    numbers.push_back(6);

遍历元素
// 使用 range-based for 循环遍历
    std::cout << "Elements in vector: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
// 使用迭代器遍历
```cpp
    std::cout << "Elements using iterator: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        size_t index = std::distance(numbers.begin(), it);// 获取迭代的Index
        std::cout << *it << " ";
    }
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
结果是这样做没有问题
```
end()返回的是“超过最后一个元素的位置”，auto it创建了一个numbers的迭代器，通过*it解引用迭代器访问每个元素