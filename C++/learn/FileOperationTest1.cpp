#include <iostream>
#include <fstream>
using namespace std;

void trunc_mode();
void app_mode();
void in_out_mode();

int main() {
    in_out_mode();
}

void trunc_mode(){
     // 使用 ios::in | ios::out | ios::trunc 模式，这样如果文件不存在会自动创建
    fstream inOutFile("example.txt", ios::in | ios::out | ios::trunc);
    if (inOutFile.is_open()) {
        cout << "文件已成功以读写模式打开或创建！" << endl;
        inOutFile.close();
    } else {
        cout << "文件无法打开或创建！" << endl;
    }
}

void app_mode(){
    // 使用 ios::in | ios::out | ios::app 模式，这样如果文件不存在会自动创建
    fstream inOutFile("example.txt", ios::in | ios::out | ios::app);
    if (inOutFile.is_open()) {
        cout << "文件已成功以读写模式打开或创建！" << endl;
        inOutFile.close();
    } else {
        cout << "文件无法打开或创建！" << endl;
    }
}

void in_out_mode(){
    // output : "文件无法打开或创建！"
    fstream inOutFile("example.txt", ios::in | ios::out);
    if (inOutFile.is_open()) {
        cout << "文件已成功以读写模式打开或创建！" << endl;
        inOutFile.close();
    } else {
        cout << "文件无法打开或创建！" << endl;
    }
}