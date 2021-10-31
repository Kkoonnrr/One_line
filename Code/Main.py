from time import sleep
from pygame.math import Vector2
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


class Troop(pygame.sprite.Sprite):
    def __init__(self, imagee, move, position_y, hp=0):
        super().__init__()
        self.hp = hp
        self.destroyed = 0
        self.imagee = pygame.image.load(imagee)
        self.imagee = pygame.transform.scale(self.imagee, (20, 20))
        self.move = move
        self.move_cont = move
        self.position_y = position_y
        self.position_x = random.randrange(20, 30)
        self.imagee_rect = self.imagee.get_rect(topleft=(self.position_x, self.position_y))
        #self.imagee_rect.update(200,200,400,200)

    def draw_troop(self, screen_m):
        screen_m.blit(self.imagee, self.imagee_rect)

    def move_troop(self, screen_m):
        self.position_y-=self.move
        self.imagee_rect = self.imagee.get_rect(topleft=(self.position_x, self.position_y))
        screen_m.blit(self.imagee, self.imagee_rect)

    def destroy(self):
        pass
        #print("destroyed")
        #self.destroyed = 1
        #self.imagee_rect = 0

    def stop(self):
        self.move = 0

    def move_again(self):
        self.move = self.move_cont

    def taking_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp == 0:
            self.destroy()
        #print(self.hp)

class Baze:
    def __init__(self, imagee, move, position_y, hp, name):
        self.name = name
        self.hp = hp
        self.imagee = pygame.image.load(imagee)
        self.move = move
        self.position_y = position_y
        self.imagee = pygame.transform.scale(self.imagee, (400, 50))
        self.hp = hp

        self.imagee_rect = self.imagee.get_rect(bottomleft=(0, position_y))

    def draw_base(self, screen_m):
        screen_m.blit(self.imagee, self.imagee_rect)

    def taking_damage(self, dmg):
        self.hp = self.hp - dmg
        print("%s hit points %d" % (self.name,  self.hp))


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

    def button_pressed(self, w, h):
        pos_m = pygame.mouse.get_pos()
        pos = self.get_pos()
        if pos[0] < pos_m[0] < pos[0] + w and pos[1] < pos_m[1] < pos[1] + h:
            #print("pressed")
            return True
        else:
            return False


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
    unit_count = 0
    Background = pygame.image.load('C:/Python_Git/one_line/Images/Background.png').convert()
    Background = pygame.transform.scale(Background, (400, 900))
    friendly_troops = []
    enemy_troops = []
    player_base = Baze('C:/Python_Git/one_line/Images/Base.png', 0, 900, 100, "Player Base")
    player_base.draw_base(screen_m)
    enemy_base = Baze('C:/Python_Git/one_line/Images/Base_enemy.png', 0, 50, 100, "Enemy Base")
    enemy_base.draw_base(screen_m)
    marine_button = Button(420, 800, 50, 50, otherfont, screen_m)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if marine_button.button_pressed(50, 50):
                    troop = Troop('C:/Python_Git/one_line/Images/Troop.png', 2, 800, 50)
                    friendly_troops.append(troop)
        for j in enemy_troops:
            for i in friendly_troops:
                if j.imagee_rect.colliderect(i.imagee_rect):
                    i.stop()
                    j.stop()
                    i.taking_damage(1)
                    if i.hp <= 0:
                        friendly_troops.remove(i)
                else:
                    j.move_again()
            #if j.move==0 and len(friendly_troops)==0 and not j.imagee_rect.colliderect(i.imagee_rect):
                #j.move_again()
            if j.imagee_rect.colliderect(player_base.imagee_rect) and j.destroyed == 0:
                player_base.taking_damage(1)
                enemy_troops.remove(j)
        for i in friendly_troops:
            for j in enemy_troops:
                if i.imagee_rect.colliderect(j.imagee_rect):
                    j.stop()
                    i.stop()
                    j.taking_damage(1)
                    if j.hp <= 0:
                        enemy_troops.remove(j)
                #else:
                    #i.move_again()
            #if i.move == 0 and len(enemy_troops)==0 and not i.imagee_rect.colliderect(j.imagee_rect):
                #i.move_again()
            if i.imagee_rect.colliderect(enemy_base.imagee_rect) and i.destroyed == 0:
                enemy_base.taking_damage(1)
                friendly_troops.remove(i)
        screen_m.blit(Background, (0, 0))
        player_base.draw_base(screen_m)
        enemy_base.draw_base(screen_m)
        marine_button.draw()
        mouse_pos = pygame.mouse.get_pos()
        unit_count += 1
        if unit_count == 45:
            unit_count = 0
            troop = Troop('C:/Python_Git/one_line/Images/Troop.png', -2, 100, 50)
            player_base.imagee_rect.collidepoint(mouse_pos)
            enemy_troops.append(troop)
        for i in friendly_troops:
            i.draw_troop(screen_m)
            i.move_troop(screen_m)
        for i in enemy_troops:
            i.draw_troop(screen_m)
            i.move_troop(screen_m)
        pygame.display.update()
        clock.tick(60)


'''def draw_text(screen_m, myfont, *args):
    x = 100
    y = 100
    for text in args:
        screen_m.blit(myfont.render(text, False, RED), (x, y))
        x += 150
        y += 150'''


main()
