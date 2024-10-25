import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Interactive Animation with Pygame")

# 定义颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 定义小球的属性
ball_pos = [400, 300]
ball_radius = 20
ball_speed = [0, 0]

# 设置帧率
clock = pygame.time.Clock()

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_speed[0] = -5
            elif event.key == pygame.K_RIGHT:
                ball_speed[0] = 5
            elif event.key == pygame.K_UP:
                ball_speed[1] = -5
            elif event.key == pygame.K_DOWN:
                ball_speed[1] = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ball_speed[0] = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ball_speed[1] = 0

    # 更新小球的位置
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 防止小球移出屏幕
    ball_pos[0] = max(ball_radius, min(size[0] - ball_radius, ball_pos[0]))
    ball_pos[1] = max(ball_radius, min(size[1] - ball_radius, ball_pos[1]))

    # 填充背景
    screen.fill(WHITE)

    # 绘制小球
    pygame.draw.circle(screen, BLUE, ball_pos, ball_radius)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)
