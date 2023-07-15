import random

import pygame

pygame.init()

width=600
height =500

game='run'
size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')

class Egg(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('0'+str(random.randint(1,3))+'.png')
        self.image=pygame.transform.scale(self.image , (35,45))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed= random.randint(2,6)
        #self.score=100
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y> height-50:
            self.kill()
            rabbit.score-=10
            print(rabbit.score)
        if self.rect.collidepoint(rabbit.rect.centerx + rabbit.dir, rabbit.rect.centery):
            self.kill()
            #print('yeee')
            rabbit.score+=10
            print(rabbit.score)

class Rabbit(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image_right = pygame.image.load('rabbit.png')
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image=self.image_right
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 7
        self.score = 100
        self.dir=20
    def update(self):
        global game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > -35:
            self.rect.centerx -= self.speed
            self.image=self.image_left
            self.dir=-20
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.centerx += self.speed
            self.image = self.image_right
            self.dir = 20
        if keys[pygame.K_UP] and self.rect.top > 250 :
            #self.image=self.image_left
            self.rect.centery -= self.speed
            #self.dir=-20
        if keys[pygame.K_DOWN] and self.rect.bottom <height:
            #self.image=self.image_left
            self.rect.centery += self.speed
            #self.dir=-20

        if self.score == 0 :
            game='lose'


bg = pygame.image.load('bg.jpg')

      #EGG
eggs_group = pygame.sprite.Group()

for i in range(2):
    ny_egg = Egg(random.randint(0,width),random.randint(-100,0))
    eggs_group.add(ny_egg)
   #RABBIT
rabbit_group= pygame.sprite.Group()
rabbit= Rabbit(width/2, height-100)
rabbit_group.add(rabbit)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill ('grey')
    window.blit(bg,(0,0))
    font = pygame.font.SysFont('mvboli', 30)
    text = 'Score:' + str(rabbit.score)
    image_score = font.render(text, True, pygame.Color('black'))
    window.blit(image_score, (50, 50))

    if len(eggs_group)< 5:
        ny_egg = Egg(random.randint(0, width), random.randint(-100, 0))
        eggs_group.add(ny_egg)

    eggs_group.update()
    eggs_group.draw(window)

    rabbit_group.update()
    rabbit_group.draw(window)
    if game!= 'run':
        font = pygame.font.SysFont('mvboli', 30)

        image_score = font.render(game, True, pygame.Color('black'))
        window.blit(image_score, (300, 250))
    pygame.display.update()
    pygame.time.delay(50)

pygame.quit()