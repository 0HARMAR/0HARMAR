.section .text
    .global _start

_start:
    popq %rax


    # 退出程序
    movq $60, %rax             # 系统调用号 60 (sys_exit)
    xor %rdi, %rdi             # 退出码 0
    syscall                    # 调用 syscall 退出
