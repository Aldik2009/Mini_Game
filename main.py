from pygame import *

init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 5:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, max_right, max_left, max_up, max_down):
        GameSprite.__init__(self, player_image, player_x, player_y, player_speed)
        self.direction = 'left'
        self.direction2 = 'up'
        self.max_right = max_right
        self.max_left = max_left
        self.max_up = max_up
        self.max_down = max_down

    def update(self):
        if self.rect.x <= self.max_left:
            self.direction = 'right'
        if self.rect.x >= self.max_right:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update2(self):
        if self.rect.y <= self.max_up:
            self.direction2 = 'down'
        if self.rect.y >= self.max_down:
            self.direction2 = 'up'

        if self.direction2 == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.w = wall_w
        self.h = wall_h
        self.image = Surface((self.w, self.h))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

mixer.init()
mixer.music.load('game_music.mp3')
mixer.music.play()
sound_of_lose = mixer.Sound('shelchok.ogg')

font.init()
font_finish = font.SysFont('Arial', 80)
win = font_finish.render('Победа!', True, (20, 50, 255))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Mini-game')
background = transform.scale(image.load('forest.jpg'), (win_width, win_height))

player = Player('ghost.png', 50, 50, 5)
enemy1 = Enemy('lamp.png', 70, 300, 3, 200, 10, 0, 0)
enemy2 = Enemy('lamp.png', 600, 200, 3, 0, 0, 15, 420)
enemy3 = Enemy('lamp.png', 270, 250, 3, 320, 150, 0, 0)
finish = Player('door.png', 520, 325, 3)
w1 = Wall(30, 255, 40, 5, 5, 2, 490)
w2 = Wall(30, 255, 40, 5, 495, 690, 2)
w3 = Wall(30, 255, 40, 690, 5, 2, 490)
w4 = Wall(30, 255, 40, 5, 5, 690, 2)
w5 = Wall(30, 255, 40, 144, 5, 2, 380)
w6 = Wall(30, 255, 40, 260, 150, 2, 345)
w7 = Wall(30, 255, 40, 380, 5, 2, 400)
w8 = Wall(30, 255, 40, 380, 405, 200, 2)
w9 = Wall(30, 255, 40, 578, 300, 2, 105)
w10 = Wall(30, 255, 40, 470, 300, 110, 2)
w11 = Wall(30, 255, 40, 470, 110, 2, 190)
w12 = Wall(30, 255, 40, 470, 110, 110, 2)

game = True
finish_game = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish_game != True:
        window.blit(background, (0, 0))
        player.update()
        enemy1.update()
        enemy2.update2()
        enemy3.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()

        player.reset()
        enemy1.reset()
        enemy2.reset()
        enemy3.reset()
        finish.reset()

    if sprite.collide_rect(player, enemy1):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, enemy2):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, enemy3):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w1):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w2):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w3):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w4):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w5):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w6):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w7):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w8):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w9):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w10):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w11):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, w12):
        player.rect.x = 50
        player.rect.y = 50
        sound_of_lose.play()

    if sprite.collide_rect(player, finish):
        window.blit(win, (300, 200))
        finish_game = True

    display.update()
    clock.tick(FPS)