#include <stdio.h>

void get_cpuid(unsigned int info[4], unsigned int function_id) {
    #if defined(__i386__) || defined(__x86_64__)
    __asm__ __volatile__ (
        "cpuid"
        : "=a" (info[0]), "=b" (info[1]),
          "=c" (info[2]), "=d" (info[3])
        : "a" (function_id)
    );
    #else
    #error "cpuid is not supported on this architecture"
    #endif
}

int main() {
    unsigned int info[4];
    get_cpuid(info, 0);  // 获取 CPUID 信息-
    // 打印厂商 ID 字符串
    char vendor[13];
    *((unsigned int*)&vendor[0]) = info[1]; // EBX
    *((unsigned int*)&vendor[4]) = info[3]; // EDX
    *((unsigned int*)&vendor[8]) = info[2]; // ECX
    vendor[12] = '\0'; // 添加字符串结尾符

    printf("Vendor ID: %s\n", vendor);

    return 0;
}
