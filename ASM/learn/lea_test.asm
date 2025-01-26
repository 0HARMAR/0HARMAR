.section .data
num:  .quad 12

.section .text
    .global _start

_start:
    movq $10 , %rsi
    movabs $num , %r8
    lea num(%rsi) , %rdi
    lea num(%rip) , %rdi
