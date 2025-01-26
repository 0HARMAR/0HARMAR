.section .data
    num:    .quad 123  # 定义一个 64 位整数
    fmt:    .asciz "The number is: %ld\n"  # 格式化字符串（%ld 用于打印 64 位整数）

.section .bss
    buffer: .skip 64  # 创建一个缓冲区来存放整数的 ASCII 表示

.section .text
    .globl _start

_start:
    # 将整数转换为字符串（手动实现）
    movq num, %rax             # 将 num 的值加载到 %rax 中
    lea buffer(%rip), %rdi      # 加载缓冲区的地址到 %rdi

    # 手动将 64 位整数转换为字符串
    movq $0, %rcx              # %rcx 清零，用于保存字符串长度
convert_loop:
    movq %rax, %rdx            # 将 %rax 中的整数复制到 %rdx
    xor  %rdx, %rdx            # 清空 %rdx（准备除法）
    movq $10, %rdi             # 除以 10，获取最后一位数字
    divq %rdi                  # %rax /= 10, %rdx = %rax % 10
    addb $'0', %dl             # 将结果转换为字符
    movb %dl, buffer(%rcx)     # 存储字符到缓冲区
    inc %rcx                   # 增加缓冲区索引
    testq %rax, %rax           # 检查是否已经除尽
    jnz convert_loop           # 如果 %rax 不是零，继续循环

    # 打印转换后的整数字符串
    movq $1, %rdi              # 文件描述符 1 (stdout)
    lea buffer(%rip), %rsi     # 加载缓冲区的地址到 %rsi
    movq %rcx, %rdx            # 将字符串长度保存到 %rdx
    movq $1, %rax              # 系统调用号 1 (sys_write)
    syscall                    # 调用 write

    # 退出程序
    movq $60, %rax             # 系统调用号 60 (sys_exit)
    xor %rdi, %rdi             # 退出码 0
    syscall                    # 调用 syscall 退出
