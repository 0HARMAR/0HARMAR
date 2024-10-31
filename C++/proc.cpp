#include <windows.h>
#include <iostream>

int main() {
    STARTUPINFOW si = { sizeof(si) };
    PROCESS_INFORMATION pi;

    if (!CreateProcessW(
        NULL,            // 应用程序名称
        (wchar_t*)"C:\\Windows\\System32\\notepad.exe", // 命令行
        NULL,            // 进程安全属性
        NULL,            // 线程安全属性
        FALSE,           // 继承句柄
        0,               // 创建标志
        NULL,            // 环境变量
        NULL,            // 当前目录
        &si,             // STARTUPINFO 指针
        &pi              // PROCESS_INFORMATION 指针
    )) {
        std::cerr << "创建进程失败: " << GetLastError() << std::endl;
        return 1;
    }

    WaitForSingleObject(pi.hProcess, INFINITE);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return 0;
}
