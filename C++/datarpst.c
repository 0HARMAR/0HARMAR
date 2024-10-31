#include "macrobox.h"

// 打印一个字节的二进制表示
void print_byte_as_bits(byte b) {
    for (int i = 7; i >= 0; i--) {
        printf("%c", (b & (1 << i)) ? '1' : '0');
    }
}

int main() {
    char a=-10;
    unsigned char b=10;
    float c =1.1;

    printf("unsigned char 10 : ");
    print_byte_as_bits(b);  //unsigned char
    printf("\n");

    printf("char -10 : ");
    print_byte_as_bits((byte) a);  //char
    printf("\n");

    printf("float 1.1 : ");
    byte* c_ptr = (byte*)&c;
    FORI(sizeof(float))  //float
    {
        print_byte_as_bits((byte)(c_ptr[i]));printf(" ");
    }

    return 0;
}
