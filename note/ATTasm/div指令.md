### 指令行为
```asm
divq %rdi
```
divq 指令是用于执行无符号整数除法操作的指令，针对 64 位寄存器（q 表示 64 位操作） 
除数是第一个操作数
被除数存储在寄存器对 %rdx:%rax 中，其中：
- %rdx 是被除数的高 64 位。
- %rax 是被除数的低 64 位。
- 除数是寄存器 %rdi 的值。
执行完毕后：
- 商存储在 %rax 中。
- 余数存储在 %rdx 中。