from pygame import *
font.init()
font2 = font.SysFont('Arial', 36)
mixer.init()
game = True
clock = time.Clock()
FPS = 120
win = display.set_mode((1000, 700))
display.set_caption("game")
place = transform.scale(image.load('place.png'),(1000,700))
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
        if key_pressed[K_UP] and self.rect.y >= 108:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 592:
            self.rect.y += self.speed
        if key_pressed[K_SPACE]:
            shoot()

class Bullet(GameSprite):
    def update(self):
        
        self.rect.x = self.rect.x - 10
        if self.rect.x <= 0:
            self.kill()

    
def shoot():
    bullet = Bullet('bullet.png', turrel.rect.x, turrel.rect.y,10, 30, 15)
    bullets.add(bullet)
    global shoots
    shoots = 10
    shoots = shoots - 1

bullets = sprite.Group()

turrel = Player('turrel.png', 860, 400,1, 138, 108)
while game:
    clock.tick(FPS)
    win.blit(place,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    text = font2.render("Заряды" + str(shoots) , 1, (254, 195, 2))
    win.blit(text, (300, 250))

    turrel.reset()
    turrel.update()
    bullets.update()
    bullets.draw(win)
    display.update()
    
