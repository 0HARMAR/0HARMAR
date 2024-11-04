.section .data
a:      .quad 11
c:      .quad 10
b:      .quad 30
.section .text
.global _start
_start:
	movq a(%rip), %rax
	movq c(%rip), %rbx
	movq b(%rip), %rcx
	addq $21, %rcx
	movq $60, %rax
	xor %rdi, %rdi
	syscall

