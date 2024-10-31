#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>

using namespace std;

mutex cout_mutex; // 定义一个互斥锁

void task1() {
    for (int i = 0; i < 5; ++i) {
        {
            lock_guard<mutex> lock(cout_mutex); // 上锁
            cout << "任务 1 - 计数: " << i << endl;
        } // lock_guard 离开作用域时自动解锁
        this_thread::sleep_for(chrono::milliseconds(500));
    }
}

void task2() {
    for (int i = 0; i < 5; ++i) {
        {
            lock_guard<mutex> lock(cout_mutex); // 上锁
            cout << "任务 2 - 计数: " << i << endl;
        } // lock_guard 离开作用域时自动解锁
        this_thread::sleep_for(chrono::milliseconds(500));
    }
}

int main() {
    thread t1(task1);
    thread t2(task2);

    t1.join(); // 等待 t1 结束
    t2.join(); // 等待 t2 结束

    return 0;
}
