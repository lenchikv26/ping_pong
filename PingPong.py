from pygame import  *
font.init()
#заготовка фона/сцены
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('background1.png'), (700, 500))

#создание классов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_weight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_height, player_weight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += 10
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += 10
#переменные
clock = time.Clock()
FPS = 60
speed_y = 5
speed_x = 5
win_height = 500
font1 = font.SysFont('Arial', 30)
lose1 = font1.render('Player 1 Defeat!', True, (100, 0, 0))
lose2 = font1.render('Player 2 Defeat!', True, (100, 0, 0))
#создание объектов

racket = Player('racket_right.png', 30, 90, 4, 30, 200)
racket2 = Player('racket_left.png', 640, 90, 4, 30, 200)
ball = GameSprite('Ball.png', 100, 100, 4, 65, 65)


#создание игрового цикла
finish = False
game = True
while game:
    
    if finish != True:
        window.blit(background, (0, 0))
        ball.reset()
        racket.reset()
        racket2.reset()
        racket.update_right()
        racket2.update_left()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 635:
            finish = True
            window.blit(lose2, (200, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
