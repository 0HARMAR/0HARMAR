```asm
# 无条件跳转指令
jmp label              # 跳转到 label
jmp *%rax              # 跳转到 %rax 寄存器的地址
jmp *label(,%rbx,4)    # 跳转到 (label + %rbx * 4)

# 有条件跳转指令
je label               # 跳转到 label，如果 ZF = 1
jz label               # 跳转到 label，如果 ZF = 1
jne label              # 跳转到 label，如果 ZF = 0
jnz label              # 跳转到 label，如果 ZF = 0
jg label               # 跳转到 label，如果 SF = OF 且 ZF = 0
jnle label             # 跳转到 label，如果 SF = OF 且 ZF = 0
jge label              # 跳转到 label，如果 SF = OF
jnl label              # 跳转到 label，如果 SF = OF
jl label               # 跳转到 label，如果 SF ≠ OF
jnge label             # 跳转到 label，如果 SF ≠ OF
jle label              # 跳转到 label，如果 SF ≠ OF 或 ZF = 1
jng label              # 跳转到 label，如果 SF ≠ OF 或 ZF = 1
jb label               # 跳转到 label，如果 CF = 1
jc label               # 跳转到 label，如果 CF = 1
jnae label             # 跳转到 label，如果 CF = 1
jnb label              # 跳转到 label，如果 CF = 0
jae label             # 跳转到 label，如果 CF = 0
jo label               # 跳转到 label，如果 OF = 1
jno label              # 跳转到 label，如果 OF = 0
js label               # 跳转到 label，如果 SF = 1
jns label              # 跳转到 label，如果 SF = 0
```

### jmp的机器码解析方式
```asm
e9 77 ff ff ff          jmpq   10c0 <register_tm_clones>10c0
```
e9表示jmp,77ffffff依照小端序规则，代表的数字是ffffff77
0xFFFFFF77 是一个有符号的 32 位整数。
在补码表示法中，0xFFFFFF77 对应的十进制值是 -137。
所以会跳转到偏移量为-137的位置

