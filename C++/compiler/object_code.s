.section .data
a:      .quad 1
b:      .quad 2
c:      .quad 0
.section .text
.global _start

_start:
    # 将 a 的值放入寄存器 rax
    movq a(%rip), %rax

    # 将 b 的值放入寄存器 rbx
    movq b(%rip), %rbx

    # 将 rax 和 rbx 的值相加，并存放在 rax 中
    addq %rbx, %rax

    # 将 rax 中的结果存入 c
    movq %rax, c(%rip)

    # 退出程序
    movq $60, %rax    # 系统调用号 60: exit
    xor %rdi, %rdi    # 返回状态码 0
    syscall
    