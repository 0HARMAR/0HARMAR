import sys

if __name__ == "__main__":
    print(f"总共有 {len(sys.argv)} 个命令行参数:")
    
    for i, arg in enumerate(sys.argv):
        print(f"参数 {i}: {arg}")