.section .data
.


.section .text
.global _start
_start: , %rsi        #第二个参数
    call add
    movq $60, %rax        # syscall: exit
    xor %rdi, %rdi        # exit code 0
    syscall

add:
    addq %rdi , %rsi
    movq %rsi , %rax
    ret
    movq $5 , %rdi         #第一个参数
    movq $10

print_int64:
