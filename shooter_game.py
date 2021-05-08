from pygame import *
from random import randint

font.init()
font2 = font.SysFont('Arial', 36)
mixer.init()

clock = time.Clock()
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__(self, gamer_image,gamer_x, gamer_y, gamer_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(gamer_image),(size_x,size_y))
        self.speed = gamer_speed
        self.rect = self.image.get_rect()
        self.rect.x = gamer_x
        self.rect.y = gamer_y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.rect.x <= 600:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
    def shoot(self):
        fire_sound = mixer.Sound('fire.ogg')
        fire_sound.play()
        bullet = BulletCode('bullet.png', rocket.rect.centerx, 340, 5, 10, 15)
        bullets.add(bullet)
        
        
       
shoots = 5
reloadt = False


class Enemy(GameSprite):
    
    def update(self):
        self.rect.y += 1
        if self.rect.y >= 499:
            self.rect.y = -150
            self.rect.x= randint(0, 640)
            global lost
            lost += 1
        
        




class BulletCode(GameSprite):
    def update(self):
        self.rect.y -= 1
        if self.rect.y <=-20:
            self.kill()



mixer.init()
win = display.set_mode((700, 500))
display.set_caption("space")
game = True
finish = False
place = transform.scale(image.load('galaxy.jpg'),(700,500))
rocket = Player('rocket.png',190,340,5,95,150)
bullets = sprite.Group()
mixer.music.load('the_final_boss.ogg')
mixer.music.play()

enemies = sprite.Group()
rocks = sprite.Group()
rockets = sprite.Group()
rockets.add(rocket)
for i in range (20):
    enemy = Enemy('ufo.png', randint(0, 640), randint(-600, -250),1, 80, 55)
    enemies.add(enemy)

for i in range (3):
    rock = Enemy('asteroid.png', randint(0, 640), randint(-600, -250),1,80,55)
    rocks.add(rock)



score = 0
lost = 0
health = 3



while game:
    clock.tick(FPS)
    win.blit(place,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                    rocket.shoot()

                
                
    
    if not finish:
             
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        win.blit(text, (10, 20))
        healths = font2.render("Жизни " + str(health), 1, (255, 255, 255))
        win.blit(healths, (10, 80))
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        win.blit(text_lose, (10, 50))
        sprite_list1 = sprite.groupcollide(enemies, bullets, True, True)
        sprite_list2 = sprite.groupcollide(rocks, bullets, False ,True)
        sprite_list3 = sprite.groupcollide(rockets, rocks, False, False)

        for s in sprite_list1:
            enemy = Enemy('ufo.png', randint(0, 640), randint(-700, -250),1, 80, 55)
            
            enemies.add(enemy)
           
            score += 1
        
        if sprite.spritecollide(rocket, rocks, True):
            health -= 1
            if health == 0:
                text = font2.render(" YOU LOST ", 1, (255, 0, 0))
                win.blit(text, (300, 250))
                mixer.music.stop()
                
                finish = True
        

        if score == 20:
            text = font2.render(" YOU WON ", 1, (254, 195, 2))
            win.blit(text, (300, 250))
            
            finish = True  
        if lost == 5:
            text = font2.render(" YOU LOST ", 1, (255, 0, 0))
            win.blit(text, (280, 250))
           
            finish = True 
        enemies.draw(win)
        enemies.update()
        rocks.draw(win)
        rocks.update()
        bullets.update()
        bullets.draw(win)
        rocket.reset()
        rocket.update()
        display.update()
