#include<stdio.h>

#ifdef _WIN32
    #include<io.h>
#elif __linux__
    #include<unistd.h>
#endif
int main()
{
    write(STDOUT_FILENO,"HELLO",5); // linux

    _write(1,"hello",5); //windows
}