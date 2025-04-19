#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void child_signal_handler(int sig) {
    printf("子进程 %d: 接收到信号 %d (SIGUSR1)\n", getpid(), sig);
    printf("子进程状态：正在退出\n");
    exit(EXIT_SUCCESS);
}

int main() {
    pid_t child_pid;

    if ((child_pid = fork()) < 0) {
        perror("fork失败");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0) {  
        signal(SIGUSR1, child_signal_handler);
        
        printf("子进程 %d: 已启动，等待父进程信号...\n", getpid());
        
        while (1) pause(); 

    } else { 
        sleep(1);
        
        printf("父进程 %d: 正在向子进程 %d 发送SIGUSR1信号\n", getpid(), child_pid);
        if (kill(child_pid, SIGUSR1) < 0) {
            perror("信号发送失败");
            exit(EXIT_FAILURE);
        }
        int status;
        waitpid(child_pid, &status, 0);
        printf("父进程 %d: 子进程已退出，状态码：%d\n", getpid(), WEXITSTATUS(status));
    }

    return EXIT_SUCCESS;
}