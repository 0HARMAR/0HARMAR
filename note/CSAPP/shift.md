### left shift
```bash
00001010 (10 in decimal)
<< 2 (shift left by 2 positions)
00101000 (40 in decimal)
```

### right shift
1. logic shift
```bash
00001010 (10 in decimal)
>> 2 (shift right by 2 positions)
00000010 (2 in decimal)

# if dividend is not divisible by 2,the result
# like divisible by 2 to the n
# such as 7 >> 2 = 7 // 2 to the 2,result is 1
```

2. arith shift
**fill with the signed bit**
```bash
11111010 (-6 in decimal, two's complement representation)
>> 2 (shift right by 2 positions, preserve sign bit)
11111110 (-2 in decimal)
```

**如果无法被整除，则结果向负无穷取整，例如 -7 >> 1 = -4，等价于 -7/2 = -3.5 → 取整为-4**