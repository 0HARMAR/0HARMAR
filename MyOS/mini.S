.globl _start
_start:
  movl $1, %eax   // write(
  movl $1,         %edi   //   fd=1,
  movl $st,        %esi   //   buf=st,
  movl $(ed - st), %edx   //   count=ed-st
  syscall                 // );

   // 调用 exit 系统调用
  movl $60, %eax   // exit(
  xorl %edi, %edi  //   status=0
  syscall          // );

st:
  .ascii "\033[01;31mHello, OS World\033[0m\n"
ed:
