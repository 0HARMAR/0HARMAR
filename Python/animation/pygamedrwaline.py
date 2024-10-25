import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸,并打开窗口
screen = pygame.display.set_mode((800, 600))

# 设置窗口标题
pygame.display.set_caption('Draw Line Example')

# 颜色
RED = (255, 0, 0)

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"windows quit with event type {event.type}")
            pygame.quit()
            sys.exit()
    
    # 填充背景色
    screen.fill((255, 255, 255))
    
    # 绘制红色线条
    pygame.draw.line(screen, RED, (100, 100), (700, 500), 1)
    
    # 更新显示
    pygame.display.flip()
