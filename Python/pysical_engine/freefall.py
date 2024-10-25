import pygame
import time

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# 初始条件
y = 100.0  # 高度
v = 0.0  # 速度
g = 9.81  # 重力加速度
delta_t = 0.01  # 时间步长
restitution = 0.8  # 反弹系数

ball_radius = 20
ball_color = (255, 0, 0)

running = True
while running:
    screen.fill((255, 255, 255))  # 清屏

    # 更新物理状态
    v += g * delta_t
    y += v * delta_t * 100  # 乘以 100 是为了将物理距离转化为像素距离

    # 碰撞检测
    if y > 400 - ball_radius:
        y = 400 - ball_radius
        v = -v * restitution

    # 绘制小球
    pygame.draw.circle(screen, ball_color, (200, int(y)), ball_radius)
    
    pygame.display.flip()  # 更新显示

    clock.tick(60)  # 控制帧率

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
