#include <stdio.h>

int main(){
    void * pmain = main;
    char *pmain_ = (char*)pmain;
    printf("%02X",pmain_[0]);
}