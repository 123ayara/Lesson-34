import pygame
pygame.init()
display=pygame.display.set_mode((500,500))
text=pygame.font.Font(None,36).render("Ayara",True,pygame.Color("yellow"))
text_rect=text.get_rect(center=(200,200))
done=False
while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        display.blit(text,text_rect)
        pygame.draw.rect(display,(255,128,192),(50,50,100,150))
        pygame.display.flip()
    