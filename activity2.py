import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
window.fill((55,100,100))
GREEN=(255,210,233)
pygame.draw.circle(window,GREEN,(200,200),50)
pygame.draw.circle(window,GREEN,(100,100),50,5)
pygame.display.flip()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True