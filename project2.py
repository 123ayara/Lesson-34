import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("gamescreen")
bg_color=(58,58,58)
image=pygame.image.load("download.png")
image=pygame.transform.scale(image,(300,300))
image_rect=image.get_rect(center=(250,250))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.fill(bg_color)
    screen.blit(image,image_rect)
    pygame.display.flip()
