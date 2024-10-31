#include <iostream>
#include <optional>

class RangeGenerator {
public:
    RangeGenerator(int start, int end) : current(start), end(end) {}

    std::optional<int> next() {
        if (current < end) {
            return current++;
        }
        return std::nullopt;  // 表示生成结束
    }

private:
    int current;
    int end;
};

int main() {
    RangeGenerator range(0, 5);
    // 模拟生成器的使用
    while (auto value = range.next()) {
        std::cout << *value << std::endl;
    }

    return 0;
}
