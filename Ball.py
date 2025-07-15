import pygame
from define import *

class Bong():
    x=0
    y=0
    colour=""
    
    def __init__(self,colour,x,y)->None:
        self.x=x
        self.y=y
        self.colour=colour
        self.dx = ball_dx
        self.dy = ball_dy
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.colour, (self.x,self.y), ball_radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def chamTuong(self):
        if self.y <= ball_radius or self.y >= WINDOW_HEIGHT - ball_radius:
            self.dy *= -1
            hit.play()
            
    def chamNguoi(self, player):
        ball_rect = pygame.Rect(self.x - ball_radius, self.y - ball_radius, ball_radius * 2, ball_radius * 2)
        player_rect = pygame.Rect(player.x, player.y, p_width, p_height)
        
        if ball_rect.colliderect(player_rect):
            self.dx *= -1
            hit.play()
            
    def reset(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.dx *= -1