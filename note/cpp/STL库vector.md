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
    std::cout << "Elements using iterator: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << " ";
    }
end()返回的是“超过最后一个元素的位置”，auto it创建了一个numbers的迭代器，通过*it解引用迭代器访问每个元素