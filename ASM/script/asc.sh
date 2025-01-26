#!/bin/bash

# 检查参数数量
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <assembly file> [output file]"
    exit 1
fi

# 获取汇编文件名和输出文件名
asm_file=$1
output_file=${2:-program}  # 如果没有提供输出文件名，默认为 'program'

# 检查汇编文件是否存在
if [ ! -f "$asm_file" ]; then
    echo "Error: Assembly file '$asm_file' not found."
    exit 1
fi

# 编译汇编文件并链接
as -o "${output_file}.o" "$asm_file" && ld -o "$output_file" "${output_file}.o"

# 检查是否成功
if [ $? -eq 0 ]; then
    echo "Compilation successful: ${output_file}"
else
    echo "Compilation failed."
    exit 1
fi

