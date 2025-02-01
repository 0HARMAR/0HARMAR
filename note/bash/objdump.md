### 反汇编elf
objdump -d program

### 反汇编16位纯二进制文件
objdump -D -b binary -mi386 -Maddr16,data16 boot.bin