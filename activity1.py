import pygame
pygame.init()
display=pygame.display.set_mode((400,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(display,(255,128,192),(50,50,100,50))
    pygame.display.flip()