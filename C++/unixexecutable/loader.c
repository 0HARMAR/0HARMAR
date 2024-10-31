#include "macrobox.h"
#include <unistd.h>
#include "ue.h"
#include <fcntl.h>
#include <sys/mman.h>

void push_to_stack();

int main(int agrc,char *agrv[]){
    if(agrc == 1){
        printstr("too few agrument!");
    }
    else{
        int fd = open(agrv[1],O_RDONLY);

        unsigned char buf[70]; //text 42 bytes and data 28 bytes

        if(fd == -1){
            perror("open");
        }

        lseek(fd,UEHEADER,SEEK_SET);

        read(fd,buf,sizeof(buf));

        FORI(42){
            if(i % 16 == 0 && i != 0)
            printf("\n");
            printf("%02x",buf[i]);
        }

        void *addr = (void *)0x400000;  // 指定起始地址
        size_t size = 4096;  // 4KB
    
        // 分配4KB内存，从0x400000开始
        void *allocated_mem = mmap(addr, size, PROT_READ | PROT_WRITE | PROT_EXEC,MAP_ANONYMOUS | MAP_PRIVATE,-1,0);
    
        if (allocated_mem == MAP_FAILED) {
            perror("mmap failed");
            return 1;
        }

        printf("Memory allocated at: %p\n", allocated_mem);

        // write text
        unsigned char *allocated_mem_uchar = (unsigned char *)allocated_mem;

        FORI(70){
            *(allocated_mem_uchar + i) = buf[i];
        }

        FORI(42){
            printf("%02x",*(allocated_mem_uchar+i));
        }

        printf("start execute process\n");

        push_to_stack();

       asm volatile (
            "mov $0x400000,%%rax\n"
            "jmp *%%rax"
            :
            :
            :"rax"
        );

    }
}
void push_to_stack() {
    asm volatile (
        "push %%rax\n"  // 保存通用寄存器 RAX
        "push %%rbx\n"  // 保存通用寄存器 RBX
        "push %%rcx\n"  // 保存通用寄存器 RCX
        "push %%rdx\n"  // 保存通用寄存器 RDX
        "push %%rsi\n"  // 保存通用寄存器 RSI
        "push %%rdi\n"  // 保存通用寄存器 RDI
        "push %%rbp\n"  // 保存基址寄存器 RBP
        "push %%rsp\n"  // 保存栈指针寄存器 RSP
        "push %%r8\n"   // 保存通用寄存器 R8
        "push %%r9\n"   // 保存通用寄存器 R9
        "push %%r10\n"  // 保存通用寄存器 R10
        "push %%r11\n"  // 保存通用寄存器 R11
        "push %%r12\n"  // 保存通用寄存器 R12
        "push %%r13\n"  // 保存通用寄存器 R13
        "push %%r14\n"  // 保存通用寄存器 R14
        "push %%r15\n"  // 保存通用寄存器 R15
        // 计算返回地址位置
        "mov %%rsp, %%rax\n"      // 将当前 RSP 保存到 RAX
        "add $9*15, %%rax\n"      // 计算返回地址在栈中的位置（保存了15个寄存器，每个8字节）
        "add $1,%%rax\n"
        
        // 将返回地址压入栈
        "push (%%rax)\n"          // 将返回地址从内存位置 RAX 压入栈
        "push %%rbp\n"

        :
        : // 无输入寄存器
        : "memory"  // 通知编译器，内存已被修改
    );
}
