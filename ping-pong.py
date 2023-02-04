from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

dx = 3
dy = 3
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Mazy')
background = transform.scale(image.load('images/baground.png'), (win_width, win_height))
player1 = Player1('images/Player 1.png', 5, win_height - 350, 4)
player2 = Player2('images/Player 2.png', win_width - 70, win_height - 350, 4)
ball = GameSprite('images/ball.png', 200, win_height - 350, 3)
clock = time.Clock()
FPS = 60
game = True
finish = False
font.init()
font = font.Font(None, 70)
lose1 = font.render('PLAYER 1 LOSE!!!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!!!', True, (180, 0, 0))
mixer.init()

while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish != True:
        ball.rect.x += dx
        ball.rect.y += dy
        player1.update()
        ball.update()
        player2.update()
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            dx *= -1
            dy * 1
        if ball.rect.y > win_height - 100 or ball.rect.y < -40:
            dy *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        

        window.blit(background, (0, 0))
        player1.reset()
        ball.reset()
        player2.reset()
    clock.tick(FPS)
    display.update()