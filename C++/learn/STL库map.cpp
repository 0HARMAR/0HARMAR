#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> age_map;
    age_map["Alice"] = 25;
    age_map["Bob"] = 30;
    age_map["Charlie"] = 20;

    // 查找元素
    std::string name = "Alice";
    if (age_map.find(name) != age_map.end()) {
        std::cout << name << " is " << age_map[name] << " years old." << std::endl;
    }

    // 遍历 map 中的键值对
    std::cout << "All elements in map:\n";
    for (const auto& pair : age_map) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
