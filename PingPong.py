from pygame import  *

#заготовка фона/сцены
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('background1.png'), (700, 500))

#переменные
clock = time.Clock()
FPS = 60
#создание игрового цикла
game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()