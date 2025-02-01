# boot.S - 使用 GAS 语法的引导程序
.code16                 # 16 位实模式
.section .text
.global _start

_start:
    jmp main            # 跳转到主程序

# 打印字符串函数（使用 BIOS 中断 0x10）
print_string:
    lodsb               # 从 %si 加载字符到 %al
    orb  %al, %al       # 检查是否到字符串结尾（%al=0）
    jz   loop_end       # 若结束则跳转
    movb $0x0E, %ah     # BIOS 功能号 0x0E（打印字符）
    movb $0x00, %bh     # 显示页号 0
    int  $0x10          # 调用 BIOS 中断
    jmp  print_string   # 继续处理下一个字符
loop_end:
    ret

# 错误处理函数
disk_error:
    movw $msg_error, %si
    call print_string
    jmp .

main:
    # 初始化段寄存器
    xorw %ax, %ax
    movw %ax, %ds       # DS = 0
    movw %ax, %es       # ES = 0
    movw %ax, %ss       # SS = 0
    movw $0x7C00, %sp   # 栈指针指向引导扇区起始地址

    # 打印加载提示
    movw $msg_loading, %si
    call print_string

    # 加载内核到内存 0x1000 (ES:BX = 0x1000:0x0000)
    movw $0x1000, %ax
    movw %ax, %es
    xorw %bx, %bx

    # 调用 BIOS 中断读取磁盘扇区
    movb $0x02, %ah     # 功能号：读取扇区
    movb $1, %al        # 读取 1 个扇区
    movb $0, %ch        # 柱面号 0
    movb $2, %cl        # 扇区号 2（从第2扇区开始）
    movb $0, %dh        # 磁头号 0
    movb $0x00, %dl     # 驱动器号（0x80 表示第一块硬盘）
    int  $0x13          # 调用中断
    jc   disk_error     # 检查错误（CF=1 表示失败）

    # 跳转到内核入口点（0x1000:0x0000）
    ljmp $0x1000, $0x0000

# 数据段
msg_loading:
    .asciz "Loading kernel..."
msg_error:
    .asciz "Disk error!"

# 填充引导扇区标志
.fill 510 - (. - _start), 1, 0   # 填充至 510 字节
.word 0xAA55                     # 引导扇区魔数
