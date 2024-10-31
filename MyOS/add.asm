.section .text
    .globl _start


_start:
    mov $0x100, %rax
    mov $0x1, %rdi
    add %rax, %rbx
    jmp PUSH


PUSH:
    push %rax
    sub $0x1, %rax
    cmpq $0x0, %rax
    jne PUSH
