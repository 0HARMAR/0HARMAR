.section .data
a:      .quad 1
b:      .quad 2
c:      .quad 10
d:      .quad 20
.section .text
.global _start
_start:
	movq a(%rip), %rax
	movq b(%rip), %rbx
	movq c(%rip), %rcx
	movq d(%rip), %rdx
	addq $6, %rbx
	addq $7, %rcx
	addq $27, %rcx
	addq $8, %
