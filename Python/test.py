import sys
import datetime
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas# 注意：PySide6 通常使用 backend_qt6agg，但这里为了兼容性仍使用 backend_qt5agg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 假设数据
data_queue = [0,1,2,3]

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.subplots() 
        super().__init__(self.fig)
        self.setParent(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.updateGeometry()

        self.line, = self.ax.plot([], [], 'ro-', lw=2)  # 初始化空线条
        self.ax.set_xlim(0, len(data_queue))  # 设置x轴范围
        self.ax.set_ylim(0, max(data_queue) * 1.1)  # 设置y轴范围，稍微留出一些空间
        self.ax.grid(True)

        self.data_index = 0  # 数据索引
        self.data_points = []  # 当前展示的数据点

        # 启动定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1000)  # 每秒更新一次

    def update_figure(self,new_data=None):
        # if new_data is not None:
        #     data_queue.append(new_data) 
        #     print(data_queue,"data_queue")
        #     print(new_data,"new_data")
            
            if len(data_queue) > 0:
                if len(self.data_points) == 4:
                    self.data_index = len(self.data_points) - 1
                    # 如果数据点超过4个，移除第一个
                    self.data_points.pop(0)
                    data_queue.pop(0)
                    new_data = 2 #我这里让新数据永远等于2
                    data_queue.append(new_data)
                    # 添加新数据点
                    new_point = data_queue[self.data_index]
                    self.data_points.append(new_point)
                else:
                    # 添加新数据点
                    new_point = data_queue[self.data_index]
                    self.data_points.append(new_point)
                    self.data_index += 1  # 更新数据索引

                # 更新线条数据
                self.line.set_data(range(len(self.data_points)), self.data_points)
                self.ax.relim()  # 重新设置轴范围
                self.ax.autoscale_view()  # 自动调整视图
                self.draw()  # 重新绘制

            else:
                # 数据展示完成，停止定时器
                self.timer.stop()

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(self.mpl)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.show()
    sys.exit(app.exec_())