import pygame, sys
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global score, score_font, score_surf, lives, lives_font, lives_surf
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = - self.speed[0]
            hit_wall.play()
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            hit_wall.play()
        if myBall.rect.top >= screen.get_rect().bottom:
            lives = lives - 1
            if lives > 0:
                pygame.time.delay(2000)
                myBall.rect.topleft = [50, 50]
            elif lives <= 0:
                screen.blit(lives_surf, lives_pos)
                pygame.time.delay(2000)
                pygame.quit()
                

                
            
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])

score = 0
score_font = pygame.font.Font(None,50)
score_surf = score_font.render(str(score),1,(0,0,0))
score_pos = [10,10]

lives = 3
lives_font = pygame.font.Font(None,50)
lives_surf = lives_font.render("Game Over",1,(0,0,0))
lives_pos = [screen.get_rect().width/2,screen.get_rect().height/2]

hit = pygame.mixer.Sound("get_point.wav")
hit.set_volume(0.2)

hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.4)

running = True
while running:
    clock.tick(30)
    screen.fill([255,255,255])
    screen.blit(score_surf, score_pos)
    for i in range (lives):
        width = screen.get_rect().width
        screen.blit(myBall.image, [width - 40* i, 20])
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        hit.play()
        myBall.speed[1] = -myBall.speed[1]
        score = score + 1
        score_surf = score_font.render(str(score),1,(0,0,0))

        
    myBall.move()
    screen.blit(myBall.image, myBall.rect)
    screen.blit(paddle.image, paddle.rect)
    pygame.display.flip()
pygame.quit()
