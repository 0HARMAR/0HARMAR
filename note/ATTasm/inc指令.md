### 指令行为
```asm
inc destination
```
inc 指令将 destination 操作数的值加 1，并更新标志寄存器中的相关标志。其主要的功能是递增操作。
**inc 指令会修改以下标志：**

- 零标志（ZF, Zero Flag）：如果结果为零，则设置为 1，否则设置为 0。
- 符号标志（SF, Sign Flag）：如果结果为负（即最高位为 1），则设置为 1，否则设置为 0。
- 溢出标志（OF, Overflow Flag）：如果有符号溢出，则设置为 1，否则设置为 0。
- 进位标志（CF, Carry Flag）：inc 指令 不影响进位标志，与 add 指令不同，add 会根据加法结果修改进位标志。