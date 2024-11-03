#include <iostream>
#include <string>
#include <windows.h>

using namespace std;

int main() {
    string command;
    while (true) {
        cout << "my_shell> ";
        getline(cin, command);
        if (command == "exit") break;

        // 设置进程信息
        STARTUPINFO si;
        PROCESS_INFORMATION pi;
        ZeroMemory(&si, sizeof(si));
        si.cb = sizeof(si);
        ZeroMemory(&pi, sizeof(pi));

        // 创建新的进程
        if (!CreateProcess(
                NULL,                   // 应用程序名称（在这里我们传入命令行）
                &command[0],            // 命令行
                NULL,                   // 进程安全属性
                NULL,                   // 线程安全属性
                FALSE,                  // 是否继承句柄
                0,                      // 创建标志
                NULL,                   // 使用父进程环境
                NULL,                   // 使用父进程目录
                &si,                    // STARTUPINFO 指针
                &pi)                    // PROCESS_INFORMATION 指针
        ) {
            cerr << "Failed to execute command: " << command << endl;
        } else {
            // 等待子进程结束
            WaitForSingleObject(pi.hProcess, INFINITE);
            // 关闭进程和线程句柄
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
        }
    }
    return 0;
}
