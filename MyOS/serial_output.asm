section .data
; 定义一个字符串缓冲区，用于存放要输出的字符
msg db 'Hello, QEMU from Serial Port!', 0

section .text
    global _start

_start:
    ; 初始化串口
    call init_serial

    ; 输出字符串
    mov si, msg          ; SI寄存器指向字符串缓冲区
print_loop:
    lodsb                ; 从 [SI] 取一个字节到 AL
    test al, al          ; 检查是否是结束符（0）
    jz done              ; 如果是结束符，跳转到 done
    call write_serial    ; 否则调用 write_serial 输出字符
    jmp print_loop       ; 继续循环

done:
    ; 进入无限循环
    jmp $

; 初始化串口函数
init_serial:
    ; 设置波特率除数，波特率为 115200
    mov dx, 0x3F8        ; 串口基地址 COM1
    mov al, 0x80         ; 启用DLAB（波特率除数访问）
    out dx, al
    mov dx, 0x3F9
    mov al, 0x01         ; 设置波特率除数为 1 (115200)
    out dx, al
    mov dx, 0x3F8
    mov al, 0x03         ; 8位数据，无校验，1停止位
    out dx, al
    mov dx, 0x3FA
    mov al, 0xC7         ; 启用FIFO，清除队列
    out dx, al
    mov dx, 0x3FC
    mov al, 0x0B         ; IRQ使能，RTS/DSR设置为1
    out dx, al
    ret

; 向串口输出字符
write_serial:
    mov dx, 0x3F8        ; 串口基地址 COM1
.wait:
    in al, dx            ; 读取串口状态
    test al, 0x20        ; 检查发送缓冲区是否为空
    jz .wait             ; 如果没准备好，继续等待
    mov al, [si-1]       ; 取刚才从 lodsb 读取的字符
    out dx, al           ; 发送字符
    ret
