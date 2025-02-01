### 移动的数据大小
1. movb(byte)(1字节)
2. movw(word)(2字节)
3. movl(double word)(4字节)
4. movq(quad word)(8字节) 

### 扩展传送
1. movsbl
它的全称是 Move with Sign Extension Byte to Long，即“带符号扩展的字节到长字的移动”。该指令的作用是将一个字节（8 位）的值加载到一个 32 位寄存器中，并且进行符号扩展。  
如果源操作数的最高位是 1（负数），扩展后的高位会填充 1；如果最高位是 0（正数），扩展后的高位会填充 0。