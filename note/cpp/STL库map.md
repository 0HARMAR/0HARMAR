# 定义
**使用需定义#include <map>**
```cpp
std::map<std::string, int> age_map;
    age_map["Alice"] = 25;
    age_map["Bob"] = 30;
    age_map["Charlie"] = 20;
```
**定义一个键为string类型，值为int类型的map,并向里面动态添加数据**

# 遍历
**遍历map中的元素**
```cpp
    std::cout << "All elements in map:\n";
    for (const auto& pair : age_map) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
```
**&代表引用,表示使用的是原先map里的元素，并没有产生一个副本,auto 代表自动类型推断,const 代表pair无法修改**
常用方法
1.find()
// 查找元素
    std::string name = "Alice";
    if (age_map.find(name) != age_map.end()) {
        std::cout << name << " is " << age_map[name] << " years old." << std::endl;
    }
find方法返回一个迭代器，如果找到，则迭代器指向目标元素的位置，如果没找到
则指向end()