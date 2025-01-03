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
```

2. arith shift
**fill with the signed bit**
```bash
11111010 (-6 in decimal, two's complement representation)
>> 2 (shift right by 2 positions, preserve sign bit)
11111110 (-2 in decimal)
```