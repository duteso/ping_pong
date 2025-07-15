import pygame
from define import *
from players import Player
from Ball import Bong
import os
import sys

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

run = True
rect_visible = False
                
WINDOW_GAME = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(icon)

pygame.mixer.music.load(resource_path("sounds/music.mp3"))
pygame.mixer.music.play(-1)

pLeft = Player(COLOUR_BLUE,0,WINDOW_HEIGHT/2 - p_height/2)
pRight = Player(COLOUR_RED,WINDOW_WIDTH-p_width,WINDOW_HEIGHT/2 - p_height/2)
ball = Bong(COLOUR_ORANGE,400,300)



pygame.font.init()
font = pygame.font.Font(None, 74)

def key_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pLeft.moveUP()
            if event.key == pygame.K_s:
                pLeft.moveDown()
            if event.key == pygame.K_UP:
                pRight.moveUP()
            if event.key == pygame.K_DOWN:
                pRight.moveDown()

while run:
    WINDOW_GAME.blit(field, (0, 0))
    
    key_events()
    
    ball.move()
    
    ball.chamTuong()
    ball.chamNguoi(pLeft)
    ball.chamNguoi(pRight)
    
    if ball.x <= 0:
        random.choice(gay_ban).play()
        pRight.score += 1
        print(f"Player Red: {pRight.score}")
        ball.reset()
    elif ball.x >= WINDOW_WIDTH:
        random.choice(gay_ban).play()
        pLeft.score += 1
        print(f"Player Blue: {pLeft.score}")
        ball.reset()
    
    text_pLeft = font.render(str(pLeft.score), 1, COLOUR_WHITE)
    text_pRight = font.render(str(pRight.score), 1, COLOUR_WHITE)
    WINDOW_GAME.blit(text_pLeft, (WINDOW_WIDTH/4, 20))
    WINDOW_GAME.blit(text_pRight, (WINDOW_WIDTH*3/4, 20))
    
    pygame.draw.line(WINDOW_GAME, COLOUR_BLACK, (WINDOW_WIDTH/2,0), (WINDOW_WIDTH/2,WINDOW_HEIGHT), width=10)
    
    pLeft.show(WINDOW_GAME)
    pRight.show(WINDOW_GAME)
    ball.draw(WINDOW_GAME)
    
    pygame.display.update()
    
pygame.quit()