#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

// 简单错误处理函数
void error(const char *msg) {
    perror(msg);
    exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <pid> <address> <length>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // 获取命令行参数
    pid_t pid = atoi(argv[1]);
    unsigned long address = strtoul(argv[2], NULL, 16);
    size_t length = strtoul(argv[3], NULL, 10);

    // 构建 /proc/[pid]/mem 的路径
    char mem_path[256];
    snprintf(mem_path, sizeof(mem_path), "/proc/%d/mem", pid);

    // 打开目标进程的内存文件
    int mem_fd = open(mem_path, O_RDONLY);
    if (mem_fd == -1) {
        error("Failed to open memory file");
    }

    // 将文件指针移动到目标地址
    if (lseek(mem_fd, address, SEEK_SET) == -1) {
        error("Failed to seek to address");
    }

    // 读取内存内容
    char *buffer = malloc(length);
    if (buffer == NULL) {
        error("Failed to allocate memory");
    }

    if (read(mem_fd, buffer, length) != length) {
        error("Failed to read memory");
    }

    // 打印读取到的内存内容
    printf("Memory content at address 0x%lx:\n", address);
    for (size_t i = 0; i < length; i++) {
        printf("%02x ", (unsigned char)buffer[i]);
        if ((i + 1) % 16 == 0) {
            printf("\n");
        }
    }
    printf("\n");

    // 关闭文件并释放内存
    close(mem_fd);
    free(buffer);

    return 0;
}
