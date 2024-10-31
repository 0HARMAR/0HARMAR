#include <stdio.h>
#include <unistd.h>
int main()
{
    setbuf(stdout,NULL);
    char seq[4] = {'-', '\\', '|', '/'};
    int i = 0;
    while(1){
        i %= 4;
        printf("\r%c",seq[i]);
        usleep(100000);
        i++;
    }
}
