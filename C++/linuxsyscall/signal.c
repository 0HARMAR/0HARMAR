#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

// 信号处理函数
void handle_signal(int signal) {
    if (signal == SIGINT) {
        printf("Received SIGINT (Ctrl+C). Cleaning up and exiting...\n");
        //exit(0);
    } else if (signal == SIGTERM) {
        printf("Received SIGTERM. Cleaning up and exiting...\n");
        //exit(0);
    }
}

int main() {
    // 注册信号处理器
    signal(SIGINT, handle_signal);
    signal(SIGTERM, handle_signal);

    printf("Press Ctrl+C to send SIGINT, or send SIGTERM to process.\n");

    // 主循环
    while (1) {
        printf("Running...\n");
        sleep(1);
    }

    return 0;
}
