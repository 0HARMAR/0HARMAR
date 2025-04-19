import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class PhysicsVisualizer:
    def __init__(self, data_file):
        self.data_file = data_file
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        # 设置坐标轴范围（显示4个象限）
        self.ax.set_xlim(-10, 10)  # X轴范围：-10到10
        self.ax.set_ylim(-10, 10)  # Y轴范围：-10到10
        
        # 设置网格和背景样式
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_facecolor('#f7f7f7')  # 浅灰色背景
        self.ax.axhline(0, color='black', linewidth=1)  # X轴
        self.ax.axvline(0, color='black', linewidth=1)  # Y轴
        
        # 初始化图形元素
        self.trajectories = {}
        self.current_positions = {}
        self.collision_markers = self.ax.scatter([], [], c='red', s=100, marker='x', zorder=3)
        
        # 存储地面信息
        self.ground = None

    def parse_data(self):
        self.data = {}
        collisions = []

        with open(self.data_file, 'r') as f:
            headers = f.readline().strip().split(',')
            for line in f:
                parts = line.strip().split(',')
                if len(parts) != 5:
                    continue
                
                time, obj_id, x, y, collision = parts
                obj_id = int(obj_id)
                time = float(time)
                x = float(x)
                y = float(y)
                collision = int(collision)

                if obj_id not in self.data:
                    self.data[obj_id] = {'time': [], 'x': [], 'y': [], 'collisions': []}
                
                self.data[obj_id]['time'].append(time)
                self.data[obj_id]['x'].append(x)
                self.data[obj_id]['y'].append(y)
                
                if collision == 1:
                    collisions.append((x, y))

        self.collisions = np.array(collisions) if collisions else np.empty((0, 2))
        
        # 识别地面（假设地面是第一个静止物体）
        for obj_id in self.data:
            if np.allclose(np.diff(self.data[obj_id]['x']), 0) and \
               np.allclose(np.diff(self.data[obj_id]['y']), 0):
                self.ground = obj_id
                break

    def init_animation(self):
        for obj_id in self.data:
            color = 'blue' if obj_id == self.ground else 'green'
            if obj_id != self.ground:
                self.trajectories[obj_id], = self.ax.plot([], [], color=color, alpha=0.5, linewidth=2)
                self.current_positions[obj_id] = self.ax.scatter(
                    [], [], c=color, s=100, zorder=2, edgecolor='black')
        
        # 绘制地面
        if self.ground is not None:
            ground_data = self.data[self.ground]
            x = ground_data['x'][0]
            y = ground_data['y'][0]
            size = (10, 1)  # 根据物理引擎中的地面尺寸
            self.ax.add_patch(plt.Rectangle(
                (x - size[0]/2, y - size[1]/2), size[0], size[1],
                color='gray', alpha=0.5, zorder=1
            ))
        
        return (*self.trajectories.values(), *self.current_positions.values(), self.collision_markers)

    def update_animation(self, frame):
        for obj_id in self.data:
            if obj_id == self.ground:
                continue
            
            x_data = self.data[obj_id]['x'][:frame]
            y_data = self.data[obj_id]['y'][:frame]
            
            self.trajectories[obj_id].set_data(x_data, y_data)
            
            if frame < len(self.data[obj_id]['x']):
                self.current_positions[obj_id].set_offsets(
                    [[self.data[obj_id]['x'][frame], self.data[obj_id]['y'][frame]]])
        
        self.collision_markers.set_offsets(self.collisions)
        
        return (*self.trajectories.values(), *self.current_positions.values(), self.collision_markers)

    def visualize(self):
        self.parse_data()
        
        ani = animation.FuncAnimation(
            self.fig,
            self.update_animation,
            frames=min(len(d['x']) for d in self.data.values()) + 20,
            init_func=self.init_animation,
            interval=50,
            blit=True
        )
        
        # 保存GIF
        ani.save('physics_simulation.gif', writer='pillow', fps=20, dpi=100)
        plt.show()

if __name__ == "__main__":
    visualizer = PhysicsVisualizer("physics_data.csv")
    visualizer.visualize()