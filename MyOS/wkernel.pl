use strict;
use warnings;
use Fcntl;

# 汇编指令的二进制表示
my $instructions = "\x48\xc7\xc0\x01\x00\x00\x00" .
                   "\x48\xc7\xc3\x02\x00\x00\x00" .
                   "\x48\x01\xc3";

# 磁盘设备文件路径（请根据你的系统调整）
my $device = './xv6.img';  # 替换为你的实际设备文件路径

# 扇区大小
my $sector_size = 512;

# 打开磁盘设备文件进行读写
sysopen(my $fh, $device, O_RDWR) or die "无法打开设备文件: $!";

# 将文件指针移动到第二个扇区的开始
my $offset = $sector_size;
seek($fh, $offset, 0) or die "无法定位到第二个扇区: $!";

# 将指令写入第二个扇区
print $fh $instructions or die "写入失败: $!";

# 填充剩余扇区（如果指令长度不足一个扇区）
if (length($instructions) < $sector_size) {
    print $fh "\x00" x ($sector_size - length($instructions));
}

# 关闭文件
close($fh) or die "无法关闭文件: $!";

print "汇编指令已成功写入第二个扇区。\n";

