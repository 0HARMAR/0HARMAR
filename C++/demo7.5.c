#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {
    int fd = open("process_info.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid > 0) {  
        char parent_msg[100];
        int len = snprintf(parent_msg, sizeof(parent_msg),
                         "[Parent] PID=%d, PPID=%d\n", getpid(), getppid());
        write(fd, parent_msg, len);
        printf("Parent process wrote to file\n");
    } else {               
        char child_msg[100];
        int len = snprintf(child_msg, sizeof(child_msg),
                          "[Child]  PID=%d, PPID=%d\n", getpid(), getppid());
        write(fd, child_msg, len);
        printf("Child process wrote to file\n");
        exit(EXIT_SUCCESS);  
    }

    close(fd);
    return 0;
}