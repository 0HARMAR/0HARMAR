#include "macrobox.h"
#include <signal.h>

MAIN{
    char *argv[] = {"/bin/yes",NULL};
    char *envp[] = {NULL};

    int cpid = fork();
    if(cpid == 0){
        execve("/bin/yes",argv,envp);
    }

    if(cpid != 0){
        int ret = kill(cpid,SIGTERM);
    }
}

