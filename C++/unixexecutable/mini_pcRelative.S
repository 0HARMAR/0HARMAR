.globl _start
_start:
  movq $1, %rax   // write(
  movq $1,         %rdi   //   fd=1,
  lea (0x15)(%rip), %rsi   //   buf=st,
  movq $(ed - st), %rdx   //   count=ed-st
  syscall                 // );

   // 调用 exit 系统调用
  movq $60, %rax   // exit(
  xorq %rdi, %rdi  //   status=0
  syscall          // );

st:
  .ascii "\033[01;31mHello, OS World\033[0m\n"
ed:
