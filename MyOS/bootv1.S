.code16                 # 16位实模式
.globl _start           # 入口点声明

_start:
    jmp start           # 跳过数据段

# 数据段定义
.section .data
cursor: .word 0         # 当前光标位置（偏移量）

# 代码段
.section .text
start:
    # 设置显存段地址
    movw $0xB800, %ax   # 显存段地址0xB800
    movw %ax, %es       # ES = 显存段
    
    # 初始化光标
    xorw %di, %di       # DI=0 屏幕左上角
    movw %di, cursor    # 存储初始光标位置

main_loop:
    call check_key      # 检查按键
    testb %al, %al
    jz main_loop        # 无按键则继续循环
    
    # 处理特殊按键
    cmpb $0x0D, %al     # 回车键
    je handle_enter
    cmpb $0x08, %al     # 退格键
    je handle_backspace
    
    # 显示普通字符
    movb $0x0F, %ah     # 属性：白底黑字
    stosw               # 将AX写入ES:DI并DI+2
    movw %di, cursor    # 更新光标位置
    jmp check_screen    # 检查屏幕边界

handle_enter:
    # 计算下一行起始位置: DI = ((DI / 160) + 1) * 160
    movw %di, %ax
    movb $160, %bl
    divb %bl            # AL = 行号, AH = 余数
    incb %al            # 下一行
    mulb %bl            # AX = 新偏移量
    movw %ax, %di
    jmp update_cursor

handle_backspace:
    cmpw $0, %di
    je main_loop        # 已在屏幕最左端
    subw $2, %di        # 回退一个字符位置
    movw $0x0F00, %es:(%di)  # 用空格擦除字符
    jmp update_cursor

check_screen:
    # 检查是否超过25行（25*160=4000）
    cmpw $4000, %di
    jb update_cursor
    # 简单滚屏：重置到顶部
    xorw %di, %di

update_cursor:
    movw %di, cursor
    jmp main_loop

# 键盘检查子程序
check_key:
    # 检查键盘状态
    inb $0x64, %al      # 读取状态寄存器
    testb $1, %al
    jz .no_key
    
    inb $0x60, %al      # 读取扫描码
    call scancode_to_ascii
    ret
.no_key:
    xorb %al, %al
    ret

# 扫描码转换（示例部分按键）
scancode_to_ascii:
    cmpb $0x1E, %al     # 'A'键按下
    je .key_a
    cmpb $0x1E + 0x80, %al  # 'A'键释放
    je .ignore
    cmpb $0x0E, %al     # Backspace
    je .backspace
    cmpb $0x1C, %al     # Enter
    je .enter
    # 添加其他按键...
    jmp .no_match

.key_a:
    movb $'a', %al
    ret
.backspace:
    movb $0x08, %al
    ret
.enter:
    movb $0x0D, %al
    ret
.ignore:
.no_match:
    xorb %al, %al
    ret

# 填充引导扇区
.fill 510 - (. - _start), 1, 0
.word 0xAA55            # 引导扇区签名
