.section .data
a:      .quad 1
b:      .quad 2
buffer: .ascii "0000000000"           # 字符串缓冲区，最后一个字节值为 0
        .byte 0

.section .text
.global _start

_start:
    # 将 a 和 b 相加，结果存储在 b 中
    movq a(%rip), %r8
    movq b(%rip), %r9
    addq %r8, %r9
    movq %r9, b(%rip)

    # 调用整数转换为字符串函数
    movq b(%rip), %rax        # 将 b 的值加载到 rax 中
    leaq buffer(%rip), %rdi   # 指向输出缓冲区
    call int_to_string        # 调用整数转字符串函数

    movq $1, %rdi             # 文件描述符 1 (stdout)
    leaq buffer(%rip), %rsi   # 输出缓冲区的地址
    movq $10, %rdx            # 输出缓冲区的大小
    movq $1, %rax             # 系统调用号 (write) 在 64 位系统中，1 代表 SYS_write
    syscall

    movq $60, %rax            # 系统调用号 (exit)
    xorq %rdi, %rdi           # status=0
    syscall

int_to_string:
    movq $10, %rcx            # 进制
    movq %rax, %rbx           # 保存原始值
    leaq buffer+9(%rip), %rdi # 指向缓冲区的末尾
    movb $0, (%rdi)           # 空字符结尾

.int_to_string_loop:
    xorq %rdx, %rdx           # 清除 %rdx
    divq %rcx                 # 除以 10，结果在 %rax，余数在 %rdx
    addb $'0', %dl            # 转换为 ASCII 字符
    decq %rdi                 # 移动到缓冲区的前一个位置
    movb %dl, (%rdi)          # 存储到缓冲区
    testq %rax, %rax          # 检查是否完成
    jnz .int_to_string_loop   # 如果还有数字继续

    ret
