### lea
```asm
lea src, dst
```
1. src 是要计算地址的操作数，可以是内存地址（通常为某个寄存器加上偏移量的形式）。
2. dst 是目标寄存器，计算出的地址会存储到这个寄存器中。
**lea指令不会访问内存，只会计算地址**

### 举例
1. lea 8(%eax), %ebx
将%eax的值加8存进%ebx寄存器

2. lea (%eax, %ebx, 4), %ecx
这条指令会计算 %eax + (%ebx * 4) 的地址，并将该地址存入 %ecx

3. lea 10(%rip) , %rdi
这条指令会将rip+10的值存到rdi

4. lea num(%rip) , %rdi
num为汇编中的全局变量名，此时num的值为相对rip的偏移量，适用于动态加载程序的相对寻址,指令的行为是&num = %rdi
编码结果是
48 8d 3d e1 0f 00 00    lea    0xfe1(%rip),%rdi        # 402000 <num>

5. lea num(%r8) , %rdi
此时num的值是静态加载时的绝对地址，指令的行为是&num + %r8 = %rdi
编码结果是
48 8d be 00 20 40 00    lea    0x402000(%rsi),%rdi