#include "macrobox.h"
#include <fcntl.h>

MAIN{
    int fd = open("/dev/tty5",O_RDONLY);

    OASSERT(fd);

    char buffer[1024];

    buffer[63] = '\0';

    int ret = read(fd,buffer,sizeof(buffer)-1);

    RASSERT(ret);

    printint(ret);

    printstr(buffer);
}
