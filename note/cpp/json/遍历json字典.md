```cpp
// 创建一个 JSON 对象
    nlohmann::json jsonObject = {
        {"name", "Alice"},
        {"age", 30},
        {"city", "Wonderland"}
    };

    // 遍历 JSON 对象中的键值对
    // 1. 使用结构化绑定的方法遍历[key, value]，c++17 start
    for (auto& [key, value] : jsonObject.items()) {
        std::cout << "Key: " << key << ", Value: " << value << std::endl;
    }

    // 2. 传统遍历方法
    for (auto& item : jsonObject.items()) {
    std::cout << "Key: " << item.key() << ", Value: " << item.value() << std::endl;
}

    // item 的类型并不是
    std::pair<const std::string, nlohmann::json>
    
```
