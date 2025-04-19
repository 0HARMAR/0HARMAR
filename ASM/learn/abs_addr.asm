.section .text
.globl _start

_start:
    movq $9, %rax               # syscall number for mmap (x86_64)
    movq $0x500000, %rdi             # address (NULL)
    movq $4096, %rsi            # size (1 page)
    movq $3, %rdx              # PROT_READ (1) | PROT_WRITE (2) = 3
    movq $0x22, %r10           # MAP_PRIVATE (0x02) | MAP_ANONYMOUS (0x20) = 0x22
    movq $-1, %r8              # fd (-1)
    xorq %r9, %r9              # offset (0)
    syscall

    movq $10,%rcx
    movq $20,0x500000(%rcx)


        # 退出程序
    movq $60, %rax             # 系统调用号 60 (sys_exit)
    xor %rdi, %rdi             # 退出码 0
    syscall                    # 调用 syscall 退出
