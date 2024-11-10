#include <iostream>
#include "../compiler/json-develop/single_include/nlohmann/json.hpp"

using namespace std;
using json = nlohmann::json;

template <typename T>

void print_type(const T&) {
    std::cout << __PRETTY_FUNCTION__ << std::endl;  // GCC/Clang 特有
}

void traverseKeyValue_structBind(json jsonObject){
    // 遍历 JSON 对象中的键值对
    for (auto& [key, value] : jsonObject.items()) {
        std::cout << "Key: " << key << ", Value: " << value << std::endl;
    }
}

void traverseKeyValue_traditional(json jsonObject){
    for (auto& item : jsonObject.items()) {
        print_type(item);
    std::cout << "Key: " << item.key() << ", Value: " << item.value() << std::endl;
}
}

int main() {
    // 创建一个 JSON 对象
    nlohmann::json jsonObject = {
        {"name", "Alice"},
        {"age", 30},
        {"city", "Wonderland"}
    };

    print_type(jsonObject);
    cout << "结构化绑定遍历json对象" << endl;
    traverseKeyValue_structBind(jsonObject);

    cout << "传统方式遍历json对象" << endl;
    traverseKeyValue_traditional(jsonObject);
    return 0;
}
