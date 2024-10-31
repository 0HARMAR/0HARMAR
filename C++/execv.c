#include <stdio.h>
#include <unistd.h>
#include <malloc.h>


char *PATHNAME;
int (*exec)(const char *pathname,char *const argv[]);
//int exec_win(const char *pathname,char *const argv[]);
int main()
{
#ifdef _WIN32
   //exec=exec_win;
    printf("IN WIN32");
#else
    exec=execv;
    printf("OTRES");
#endif
    setbuf(stdout,NULL);
    PATHNAME=(char *)malloc(sizeof(char)*50);
    scanf("%s",PATHNAME);
    char *argv[]={PATHNAME,"HELLO",NULL};
    exec(PATHNAME,argv);
}

/*
int exec_win(const char *pathname, char *const argv[]) {
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    
    // 初始化结构体
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));
    
    // 构造命令行
    char commandLine[1024];
    snprintf(commandLine, sizeof(commandLine), "%s", pathname);
    
    // 如果有参数，附加到命令行
    for (int i = 1; argv[i] != NULL; i++) {
        strcat(commandLine, " ");
        strcat(commandLine, argv[i]);
    }
    
    // 创建新进程
    if (!CreateProcess(
            NULL,           // 使用命令行
            commandLine,    // 命令行
            NULL,           // 进程属性
            NULL,           // 线程属性
            FALSE,          // 继承句柄
            0,              // 创建标志
            NULL,           // 环境
            NULL,           // 当前目录
            &si,            // 启动信息
            &pi             // 进程信息
    )) {
        // 创建进程失败
        return -1; // 可以返回 GetLastError() 以获取更多信息
    }
    
    // 等待进程结束
    WaitForSingleObject(pi.hProcess, INFINITE);
    
    // 关闭句柄
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    
    return 0; // 成功
}

*/
