from pygame import *
from random import randint

win_w = 600
win_h = 500
FPS = 60

def generate_color():
    return Color(randint(0, 255), randint(0, 255), randint(0, 255))

background = generate_color()

win = display.set_mode((win_w, win_h))
display.set_caption("Ping-Pong")
clock = time.Clock()

class Sprite():
    def __init__(self, picture, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def start(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def start_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (win_h - 80):
            self.rect.y += self.speed
    def start_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (win_h - 80):
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, (win_h / 2), 50, 150, 5)
racket2 = Player('racket.png', (win_w - 80), (win_h / 2), 50, 150, 5)

class Ball(Sprite):
    pass

tenis_ball = Sprite('tenis_ball.png', 200, 200, 50, 50, 5)

color_selection = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color_selection = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            color_selection = False

    if color_selection:
        background = generate_color()

    win.fill(background)

    racket1.start_left()
    racket2.start_right()

    racket1.start()
    racket2.start()
    tenis_ball.start()

    display.update()
    clock.tick(FPS)