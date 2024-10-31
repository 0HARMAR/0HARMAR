section .text
    global _start

_start:
    ; 清除屏幕
    mov ax, 0x07C0    ; 设置视频模式
    mov bx, 0         ; 光标位置 
    mov cx, 80        ; 列数
    mov dx, 25        ; 行数
    int 0x10          ; 调用 BIOS 中断

    ; 输出消息
    mov si, message
    call print_string

    ; 进入循环
.loop:
    jmp .loop         ; 无限循环

; 输出字符串的子程序
print_string:
    lodsb             ; 加载下一个字节到 AL
    test al, al       ; 检查是否为字符串结束符
    jz .done          ; 如果是结束符，返回
    mov ah, 0x0E      ; BIOS 输出字符功能
    int 0x10         ; 调用 BIOS 中断
    jmp print_string  ; 继续输出下一个字符
.done:
    ret

message db 'Hello, World!', 0

; 填充到 512 字节
times 510 - ($ - $$) db 0
dw 0xAA55            ; 引导扇区的签名

