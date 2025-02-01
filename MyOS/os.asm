/* 实模式内核，需加载到0x10000处 */
.code16
.section .text
.global _start

_start:
    /* 初始化段寄存器（由加载器设置CS=0x1000, IP=0x0000） */
    movw %cs, %ax       # 假设加载器已将CS设为0x1000
    movw %ax, %ds       # DS = CS = 0x1000
    movw %ax, %es       # ES = 0x1000

    /* 打印字符串 */
    movw $msg, %si      # SI = 符号msg的段内偏移
    call print_string
    cli
1:  hlt
    jmp 1b

print_string:
    movb $0x0E, %ah     # BIOS tele-type输出
    movw $0x0007, %bx   # BH=0, BL=07h（灰色）
.print_loop:
    lodsb               # 加载DS:SI -> AL
    testb %al, %al
    jz .done
    int $0x10
    jmp .print_loop
.done:
    ret

msg: .asciz "Hello,HOS Kernel!\r\n"

/* 不需要填充到512字节（内核大小自由） */
