.section .data
    .word 0xfff0

.section .text
    .globl _start

_start:
    call init
    mov $0x100, %rax
    mov $0x1, %rdi
    mov $0x3, %rsi
    call sum
    add %rax, %rax
    jmp PUSH


PUSH:
    push %rax
    sub $0x1, %rax
    cmpq $0x0, %rax
    jne PUSH
    jmp ed
    
ed:
    mov $0x3c, %rax
    syscall

sum:
    lea (%rdi,%rsi), %rax
    ret

.section .init  #new code section
    .globl init
init:
    mov $100, %r15
    ret
