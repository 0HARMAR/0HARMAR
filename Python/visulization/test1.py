import matplotlib.pyplot as plt

# 示例数据
processes = ['Process 1', 'Process 2', 'Process 3']
start_times = [0, 10, 20]
durations = [10, 15, 10]

fig, ax = plt.subplots()

# 绘制条带
for i, process in enumerate(processes):
    ax.barh(process, durations[i], left=start_times[i], height=0.5, color='skyblue', edgecolor='black')

# 设置轴标签和标题
ax.set_xlabel('Time')
ax.set_title('Process Execution Flow')


# 保存图像到指定路径
plt.savefig("Python/visulization/test1.png")
