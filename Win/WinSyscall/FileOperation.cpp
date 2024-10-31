#include <windows.h>
#include <iostream>

int main() {
    // 打开文件
    HANDLE hFile = CreateFile(
        "example.txt",             // 文件名
        GENERIC_READ | GENERIC_WRITE, // 访问模式
        0,                         // 不共享
        NULL,                      // 默认安全属性
        CREATE_ALWAYS,            // 创建新文件
        FILE_ATTRIBUTE_NORMAL,     // 文件属性
        NULL                       // 不使用模板文件
    );

    if (hFile == INVALID_HANDLE_VALUE) {
        std::cerr << "无法打开文件，错误代码: " << GetLastError() << std::endl;
        return 1;
    }

    // 写入数据
    const char* data = "Hello, Windows API!";
    DWORD bytesWritten;
    WriteFile(hFile, data, strlen(data), &bytesWritten, NULL);

    std::cout << "成功写入 " << bytesWritten << " 字节." << std::endl;

    // 关闭文件
    CloseHandle(hFile);

    return 0;
}
