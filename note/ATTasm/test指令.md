### 指令行为
```asm
test operand1, operand2
```
operand1 和 operand2 可以是寄存器、内存地址或立即数（立即数通常是第二个操作数）。
test 指令执行 operand1 AND operand2 操作，但不会将结果存储在目标寄存器或内存位置中。它只会更新标志寄存器。

它 仅影响标志寄存器，并根据运算的结果更新以下标志：
- 零标志（ZF, Zero Flag）：如果结果为 0，则设置为 1，否则设置为 0。
- 符号标志（SF, Sign Flag）：如果结果的最高位为 1（即负数），则设置为 1，否则设置为 0。
- 溢出标志（OF, Overflow Flag）：test 指令 不会改变 溢出标志（OF）。
- 进位标志（CF, Carry Flag）：test 指令 不会改变 进位标志（CF）。