#include "macrobox.h"
#include <sys/stat.h>
#include <time.h>

void print_file_info(const char *path) {
    struct stat file_stat;
    
    // 调用 stat 函数获取文件信息
    int ret = stat(path, &file_stat);
    
    if (ret == -1) {
        perror("stat");
        exit(EXIT_FAILURE);
    }

    // 打印获取到的文件信息
    printf("File: %s\n", path);
    printf("Device ID: %ld\n", (long)file_stat.st_dev);
    printf("Inode number: %ld\n", (long)file_stat.st_ino);
    printf("File mode: %o\n", (unsigned int)file_stat.st_mode);
    printf("Number of hard links: %ld\n", (long)file_stat.st_nlink);
    printf("Owner's user ID: %d\n", file_stat.st_uid);
    printf("Owner's group ID: %d\n", file_stat.st_gid);
    printf("Device ID (if special file): %ld\n", (long)file_stat.st_rdev);
    printf("Total size, in bytes: %ld\n", (long)file_stat.st_size);
    printf("Blocksize for filesystem I/O: %ld\n", (long)file_stat.st_blksize);
    printf("Number of 512B blocks allocated: %ld\n", (long)file_stat.st_blocks);
    
    // 打印时间信息
    printf("Time of last access: %s", ctime(&file_stat.st_atime));
    printf("Time of last modification: %s", ctime(&file_stat.st_mtime));
    printf("Time of last status change: %s", ctime(&file_stat.st_ctime));
}

MAIN{
    // 打印文件 /bin/gcc 的信息
    print_file_info("/bin/gcc");
    return 0;
}
