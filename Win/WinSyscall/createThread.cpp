#include <windows.h>
#include <stdio.h>

// 线程函数
DWORD WINAPI MyThreadFunction(LPVOID lpParam) {
    printf("Hello from new thread! Param: %d\n", *(int*)lpParam);
    return 0;
}

int main() {
    DWORD threadId;
    HANDLE hThread;
    int param = 42;

    // 创建新线程
    hThread = CreateThread(
        NULL,         // 默认安全性
        0,            // 默认栈大小
        MyThreadFunction, // 线程入口函数
        &param,       // 参数
        0,            // 默认标志（立即运行）
        &threadId     // 接收线程 ID
    );

    if (hThread == NULL) {
        printf("CreateThread failed, error: %lu\n", GetLastError());
        return 1;
    }

    printf("Thread created successfully with ID: %lu\n", threadId);

    // 等待线程完成
    WaitForSingleObject(hThread, INFINITE);

    // 关闭线程句柄
    CloseHandle(hThread);

    return 0;
}
