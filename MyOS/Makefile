# 编译器和链接器
CC = gcc
LD = ld
OBJCOPY = objcopy
OBJDUMP = objdump

# 编译和链接选项
CFLAGS = -fno-builtin -fno-pic -m32 -nostdinc -Iinclude -Os -fno-stack-protector
LDFLAGS = -m elf_i386 -z nodefaultlib --omagic -e start -Ttext 0x7C00

# 输出目录
OUT = out

# 目标文件
TARGET = xv6.img
BOOTBLOCK = $(OUT)/bootblock

# 默认目标
.PHONY: all
all: $(TARGET)

# 创建输出目录
$(OUT):
	@mkdir -p $(OUT)

 # 编译和链接 bootblock
$(BOOTBLOCK): $(OUT)/bootasm.o $(OUT)/bootmain.o | $(OUT)
	$(LD) $(LDFLAGS) -o $(OUT)/bootblock.o $^
	$(OBJDUMP) -S $(OUT)/bootblock.o > $(OUT)/bootblock.asm
	$(OBJCOPY) -S -O binary -j .text $(OUT)/bootblock.o $(BOOTBLOCK)
	./sign.pl $(OUT)/bootblock
	# 添加引导签名
# 编译 bootasm.S
$(OUT)/bootasm.o: bootasm.S | $(OUT)
	$(CC) $(CFLAGS) -o $@ -c $<

# 编译 bootmain.c
$(OUT)/bootmain.o: bootmain.c | $(OUT)
	$(CC) $(CFLAGS) -o $@ -c $<

# 生成 xv6.img
$(TARGET): $(BOOTBLOCK)
	dd if=/dev/zero of=$(TARGET) bs=512 count=10000
	dd if=$(BOOTBLOCK) of=$(TARGET) conv=notrunc

#写入内核代码

	./wkernel.py
# 清理
.PHONY: clean
clean:
	rm -rf $(OUT) $(TARGET)
# 运行 QEMU
.PHONY: run
run: $(TARGET)
	qemu-system-x86_64 -drive file=$(TARGET),format=raw 

