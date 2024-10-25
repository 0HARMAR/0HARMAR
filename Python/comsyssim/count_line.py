import os
import argparse

# 指定你想统计的文件扩展名
FILE_EXTENSIONS = ['.py', '.cpp', '.java','.go','.c']  # 根据需要修改

def count_lines_in_file(file_path):
    """计算单个文件的代码行数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except Exception as e:
        print(f"无法读取文件 {file_path}，错误: {e}")
        return 0

def count_lines_in_directory(directory, file_extensions, exclude_files, exclude_dirs):
    """递归统计指定目录中的所有代码行数"""
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        # 排除指定的目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file in exclude_files:
                continue
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                lines_in_file = count_lines_in_file(file_path)
                print(f"{file_path}: {lines_in_file} 行")
                total_lines += lines_in_file
    return total_lines

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='统计项目中的代码行数')
    parser.add_argument('project_directory', type=str, help='项目根目录路径')
    parser.add_argument('-ef', type=str, nargs='*', default=[], help='要忽略的文件名')
    parser.add_argument('-ed', type=str, nargs='*', default=[], help='要忽略的文件夹名')
    parser.add_argument('-if', type=str, nargs='*', default=[], help='只统计的文件名')

    args = parser.parse_args()

    # 开始计算代码行数
    total_lines = count_lines_in_directory(
        args.project_directory,
        FILE_EXTENSIONS,
        args.ef,
        args.ed
    )
    print(f"项目的总代码行数: {total_lines}")
