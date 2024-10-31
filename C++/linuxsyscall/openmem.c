#include "macrobox.h"
#include <fcntl.h>

MAIN
{
    setbuf(stdout, NULL);

    int *start = MALLOC(int, 100);

    assert(start != NULL);

    printptr(start);

    char buffer[100];

    FORI(100)
    {
        *((char *)start + i) = (65 + i) % 91;
    }

    int fd = open("/proc/self/mem", O_RDWR);

    assert(fd != -1);

    lseek(fd, (long int)start, SEEK_SET);

    printint(fd);

    int ret = read(fd, buffer, 99);

    printint(ret);

    if (ret == -1)
    {
        perror("read");
        close(fd);
    }

    buffer[ret] = '\0';

    printf("%s", buffer);
    printstr(buffer);
}
