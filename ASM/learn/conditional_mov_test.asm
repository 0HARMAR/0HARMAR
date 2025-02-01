.section .data
    char :      .word 1

.section .text
    .global _start

_start:
    movq $0 , %rdi
    movw $'a' , %ax
    movw $'b' , char
    testq %rdi , %rdi
    cmove %ax , %bx
    cmove char , %ax
    movw %bx , char

    movq $1, %rdi              # 文件描述符 1 (stdout)
    lea char(%rip), %rsi     # 加载缓冲区的地址到 %rsi
    movq $1 , %rdx            #写入的字符数
    movq $1, %rax              # 系统调用号 1 (sys_write) 
    syscall                    # 调用 write

    # 退出程序
    movq $60, %rax             # 系统调用号 60 (sys_exit)
    xor %rdi, %rdi             # 退出码 0
    syscall                    # 调用 syscall 退出
