from time import sleep

import pygame
import random
import math
from tkinter import *

x = 600
y = 900
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class Troop:
    def __init__(self, imagee, move, position_y, hp=0):
        self.hp = hp
        self.imagee = pygame.image.load(imagee)
        self.imagee = pygame.transform.scale(self.imagee, (20, 20))
        self.move = move
        self.position_y = position_y
        self.position_x = random.randrange(20, 380)
        self.imagee_rect = self.imagee.get_rect(topleft=(self.position_x, self.position_y))

    def draw_troop(self, screen_m):
        screen_m.blit(self.imagee, self.imagee_rect)

    def move_troop(self, screen_m):
        self.position_y-=self.move
        self.imagee_rect = self.imagee.get_rect(topleft=(self.position_x, self.position_y))
        screen_m.blit(self.imagee, self.imagee_rect)


class Baze:
    def __init__(self, imagee, move, position_y, hp):
        self.hp = hp
        self.imagee = pygame.image.load(imagee)
        self.move = move
        self.position_y = position_y
        self.imagee = pygame.transform.scale(self.imagee, (400, 50))
        self.hp = hp
        self.imagee_rect = self.imagee.get_rect(bottomleft=(0, position_y))

    def draw_base(self, screen_m):
        screen_m.blit(self.imagee, self.imagee_rect)


class Game:
    def __init__(self):
        self.board = [[]]

    def draw_board(self):
        pygame.display.update()

    def create_board(self):
        self.board = [[0 for i in range(7)] for i in range(6)]
        return self.board

    def draw_line(self):
        pass

class Screen:
    def __init__(self, title, w, h):
        self.title = title
        self.w = w
        self.h = h
        self.current = False

    '''Makes specific screen main one'''
    def make_current(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode((self.w, self.h))

    '''Makes specific screen second one'''
    def not_current(self):
        self.current = False

    def get_screen(self):
        return self.screen

    '''Fills screen with black'''
    def update(self):
        if self.current:
            self.screen.fill(BLACK)


class Button:
    def __init__(self, xx, yy, w, h, font, window, i=0):
        self.x = xx
        self.y = yy
        self.w = w
        self.h = h
        self.font = font
        self.i = i
        self.window = window

    '''Draws columns numbers'''
    def draw(self):
        pygame.draw.rect(self.window, WHITE, (self.x, self.y, self.w, self.h))
        self.window.blit(self.font.render(str(self.i+1), False, BLACK), (self.x + 10, self.y - 10))

    '''Draws text buttons'''
    def draw_text(self, text):
        pygame.draw.rect(self.window, WHITE, (self.x, self.y, self.w, self.h))
        self.window.blit(self.font.render(text, False, BLACK), (self.x + 10, self.y - 5))

    def get_pos(self):
        return self.x, self.y



def main():
    pygame.init()
    pygame.font.init()
    screen_game = Screen("One line", 600, 900)
    screen_menu = Screen("Main Menu", 800, 800)
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    otherfont = pygame.font.SysFont('Comic Sans MS', 30)
    text_Menu = myfont.render("Game Menu", False, RED)
    screen_game.make_current()
    screen_m = screen_game.get_screen()
    clock = pygame.time.Clock()
    game = Game()
    Background = pygame.image.load('C:/Python_Git/one_line/Images/Background.png').convert()
    Background = pygame.transform.scale(Background, (400, 900))
    troops = []
    player_base = Baze('C:/Python_Git/one_line/Images/Base.png', 0, 900, 100)
    player_base.draw_base(screen_m)
    enemy_base = Baze('C:/Python_Git/one_line/Images/Base_enemy.png', 0, 50, 100)
    enemy_base.draw_base(screen_m)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for i in troops:
            if i.imagee_rect.colliderect(enemy_base.imagee_rect):
                enemy_base.hp-=1
                print(enemy_base.hp)
        screen_m.blit(Background, (0, 0))
        player_base.draw_base(screen_m)
        enemy_base.draw_base(screen_m)
        mouse_pos = pygame.mouse.get_pos()
        if  player_base.imagee_rect.collidepoint(mouse_pos):
            troop = Troop('C:/Python_Git/one_line/Images/Troop.png', 1, 800)
            troops.append(troop)
        for i in troops:
            i.draw_troop(screen_m)
            i.move_troop(screen_m)
        pygame.display.update()
        clock.tick(60)


def draw_text(screen_m, myfont, *args):
    x = 100
    y = 100
    for text in args:
        screen_m.blit(myfont.render(text, False, RED), (x, y))
        x += 150
        y += 150


main()
