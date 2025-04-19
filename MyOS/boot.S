# boot.S - 打印字符串的引导扇区程序（GAS 语法）
.code16                 # 16 位实模式
.section .text
.global _start

_start:
    jmp main            # 跳转到主程序

# 打印字符串函数（使用 BIOS 中断 0x10）
print_string:
    lodsb               # 从 SI 加载字符到 AL
    orb  %al, %al       # 检查是否到字符串结尾（AL=0）
    jz   loop_end       # 若结束则跳转
    movb $0x0E, %ah     # BIOS 功能号 0x0E（打印字符）
    movb $0x00, %bh     # 显示页号 0
    int  $0x10          # 调用 BIOS 中断
    jmp  print_string   # 继续处理下一个字符
loop_end:
    ret

main:
    # 设置段寄存器
    xorw %ax, %ax
    movw %ax, %ds       # DS = 0
    movw %ax, %es       # ES = 0
    movw %ax, %ss       # SS = 0
    movw $0x7C00, %sp   # 栈指针指向引导扇区起始地址
    # 打印字符串
    movw $msg, %si      # SI 指向字符串
    call print_string

    # 死循环
    cli                 # 禁用中断
    hlt
    jmp .               # 无限循环

msg:
    .asciz "Hello, Boot Sector!"  # 以 0 结尾的字符串

# 填充引导扇区标志
.fill 510 - (. - _start), 1, 0   # 填充至 510 字节,510 - (. - _start)计算需要填充的单元数
.word 0xAA55                     # 引导扇区魔数