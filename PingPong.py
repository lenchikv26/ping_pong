from pygame import  *

#заготовка фона/сцены
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('background1.png'), (700, 500))

#создание классов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (30, 200))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += 10
 
#переменные
clock = time.Clock()
FPS = 60

#создание объектов

racket = Player('racket_right.png', 30, 90, 4)
racket2 = Player('racket_left.png', 640, 90, 4)

#создание игрового цикла
game = True
while game:
    window.blit(background, (0, 0))
    racket.reset()
    racket2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
