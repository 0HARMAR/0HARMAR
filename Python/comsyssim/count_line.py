import os
import argparse
import json
from datetime import datetime

# 指定你想统计的文件扩展名
FILE_EXTENSIONS = ['.py', '.cpp', '.java', '.go', '.c']  # 根据需要修改
LOG_FILE = 'line_count_log.json'  # 存储统计记录的日志文件

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
    file_line_counts = {}  # 保存每个文件的行数

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
                file_line_counts[file_path] = lines_in_file

    return total_lines, file_line_counts

def load_previous_counts(log_file):
    """加载之前的统计数据"""
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_counts(log_file, counts):
    """保存当前的统计数据到日志文件"""
    with open(log_file, 'w', encoding='utf-8') as file:
        json.dump(counts, file, ensure_ascii=False, indent=4)

def compare_counts(new_counts, old_counts):
    """比较当前统计数据和之前的统计数据，返回新增的行数"""
    diff_counts = {}
    total_new_lines = 0
    for file, new_count in new_counts.items():
        old_count = old_counts.get(file, 0)
        diff = new_count - old_count
        if diff != 0:
            diff_counts[file] = diff
            total_new_lines += diff
    return total_new_lines, diff_counts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='统计项目中的代码行数')
    parser.add_argument('project_directory', type=str, help='项目根目录路径')
    parser.add_argument('-ef', type=str, nargs='*', default=[], help='要忽略的文件名')
    parser.add_argument('-ed', type=str, nargs='*', default=[], help='要忽略的文件夹名')

    args = parser.parse_args()

    # 加载之前的统计数据
    previous_counts = load_previous_counts(LOG_FILE)

    # 计算当前的代码行数
    total_lines, current_counts = count_lines_in_directory(
        args.project_directory,
        FILE_EXTENSIONS,
        args.ef,
        args.ed
    )

    # 计算增量
    new_lines, diff_counts = compare_counts(current_counts, previous_counts)

    # 输出统计结果
    print(f"项目的总代码行数: {total_lines}")
    print(f"新增的代码行数: {new_lines}")
    if diff_counts:
        print("每个文件的增量行数:")
        for file, diff in diff_counts.items():
            print(f"{file}: {diff} 行")

    # 保存当前的统计数据到日志文件
    current_counts['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_counts(LOG_FILE, current_counts)
