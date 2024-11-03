#include <windows.h>
#include <iostream>

int main() {
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    
    // 初始化 STARTUPINFO 结构
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    // 命令行参数
    char commandLine[] = "notepad.exe";

    // 创建新进程
    if (!CreateProcess(
            NULL,          // 应用程序名称
            commandLine,   // 命令行
            NULL,          // 进程安全属性
            NULL,          // 线程安全属性
            FALSE,         // 不继承句柄
            0,             // 默认创建标志
            NULL,          // 使用父进程的环境
            NULL,          // 使用父进程的工作目录
            &si,           // 指向 STARTUPINFO 结构的指针
            &pi)           // 指向 PROCESS_INFORMATION 结构的指针
    ) {
        std::cerr << "Failed to create process: " << GetLastError() << std::endl;
        return 1;
    }

    // 等待新进程结束
    WaitForSingleObject(pi.hProcess, INFINITE);

    // 关闭进程和线程句柄
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    std::cout << "Process finished." << std::endl;
    return 0;
}
