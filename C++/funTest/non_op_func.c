#include <stdio.h>


void non_op(){
    int a = 3;
    float b = 3.3;
}
int main(){
    printf("ready to call non op func");
    non_op();
}