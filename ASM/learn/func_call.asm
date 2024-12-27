.section .data
# 定义全局变量，用于存储结果
result: .long 0

.section .text
.globl _start

# 主程序入口
_start:
    # 准备参数
    movl $5, %edi         # 第一个参数，传递 5
    movl $10, %esi        # 第二个参数，传递 10

    # 调用 add_numbers 函数
    call add_numbers

    # 将返回值保存到全局变量 result
    movl %eax, result

    # 程序退出
    movl $60, %eax        # syscall: exit
    xor %edi, %edi        # exit code 0
    syscall

# 函数：add_numbers
# 功能：计算两个整数的和
# 输入：%edi = 第一个参数，%esi = 第二个参数
# 输出：%eax = 和
add_numbers:
    # 计算 %edi 和 %esi 的和，结果存储在 %eax
    movl %edi, %eax       # 将第一个参数复制到 %eax
    addl %esi, %eax       # 将第二个参数加到 %eax
    ret                   # 返回
