import matplotlib.pyplot as plt
import subprocess
import sys

def main():
    # 启动C++程序
    cpp_process = subprocess.Popen(["./out/examplev1.exe"], stdout=subprocess.PIPE, text=True)

    # 初始化图形
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 20)
    ball1, = ax.plot([], [], 'bo', markersize=10)
    ball2, = ax.plot([], [], 'ro', markersize=10)

    while True:
        # 读取C++程序的输出
        line = cpp_process.stdout.readline()
        if not line:
            break

        # 解析坐标
        coords = line.strip().split()
        ball1_x, ball1_y = map(float, coords[0].split(','))
        ball2_x, ball2_y = map(float, coords[1].split(','))

        # 更新图形
        ball1.set_data([ball1_x], [ball1_y])  # Pass as lists
        ball2.set_data([ball2_x], [ball2_y])  # Pass as lists
        fig.canvas.flush_events()

    # 关闭C++程序
    cpp_process.terminate()

if __name__ == "__main__":
    main()
    