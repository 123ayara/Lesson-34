import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("sprites")
bg_color=(173,216,230)
rectangle=(255,255,255)
clock=pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill(rectangle)
        self.rect=self.image.get_rect(topleft=(x,y))
    def update(self,keys):
        if keys[pygame.K_LEFT]:
            self.rect.x-=5
        if keys[pygame.K_RIGHT]:
            self.rect.x+=5
        if keys[pygame.K_UP]:
            self.rect.y-=5
        if keys[pygame.K_DOWN]:
            self.rect.y+=5
player1=Player(100,100)
player2=Player(300,100)
all_sprites=pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    player1.update(keys)
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
