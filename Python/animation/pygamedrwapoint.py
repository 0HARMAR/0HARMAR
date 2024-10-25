import pygame
import sys
import time
pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Draw Point")

screen.fill((255,255,255))

x = 0
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if x < 300:
        pygame.draw.circle(screen,(255,0,0),(200,x),1)
        time.sleep(1)
    pygame.display.flip()
    x+=1
        
