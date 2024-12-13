#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <thread>
#include <chrono>
using namespace std;

const int SCREEN_WIDTH = 80;   // 屏幕宽度
const int SCREEN_HEIGHT = 20; // 屏幕高度
const char STAR = '*';        // 星星符号

void clearScreen() {
    // 清空终端屏幕
    cout << "\033[2J\033[H";
}

void display(const vector<string>& screen) {
    // 在终端上显示屏幕内容
    for (const auto& row : screen) {
        cout << row << endl;
    }
}

int main() {
    // 初始化随机数种子
    srand(static_cast<unsigned>(time(0)));

    // 初始化屏幕
    vector<string> screen(SCREEN_HEIGHT, string(SCREEN_WIDTH, ' '));

    // 存储每列的星星当前高度
    vector<int> starPositions(SCREEN_WIDTH, -1);

    while (true) {
        // 清空屏幕
        for (auto& row : screen) {
            fill(row.begin(), row.end(), ' ');
        }

        // 更新星星位置
        for (int col = 0; col < SCREEN_WIDTH; ++col) {
            if (starPositions[col] >= 0) {
                screen[starPositions[col]][col] = STAR;
            }

            // 随机生成新星星或让已有星星下落
            if (starPositions[col] >= SCREEN_HEIGHT - 1 || rand() % 10 < 2) {
                starPositions[col] = -1; // 星星消失
            } else if (starPositions[col] == -1 && rand() % 10 < 2) {
                starPositions[col] = 0; // 生成新星星
            } else if (starPositions[col] >= 0) {
                ++starPositions[col]; // 星星下落
            }
        }

        // 显示屏幕
        clearScreen();
        display(screen);

        // 延迟更新
        this_thread::sleep_for(chrono::milliseconds(100));
    }

    return 0;
}
