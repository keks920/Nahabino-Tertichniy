# -*- coding: utf-8 -*-
import pygame
from random import *
import os

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        for i in range(40):
            k = randint(0, 399)
            self.board[k // 20][k % 20] = 1
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (10 + i * 30, 10 + j * 30, 30, 30), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (10 + i * 30, 10 + j * 30, 30, 30), 1)
    
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        g = self.on_click(cell)
        return g
    
    def get_cell(self, mouse_pos):
        i, j = mouse_pos
        if i >= 10 and i <= self.width * 30 + 10 and j >= 10 and j <= self.height * 30 + 10:
            i = (i - 10) // 30
            j = (j - 10) // 30
            return (i, j)
        else:
            return None
    
    def on_click(self, k):
        if k != None:
            i, j = k
            if self.board[j][i] == 1:
                return (1, k)
            elif self.board[j][i] == 0:
                image = loadImage(self.neighbours(k))
                screen.blit(image, (i * 30 + 10, j * 30 + 10))
                return (2, k, image)
    
    def on_click2(self, k):
        if k != None:
            i, j = k
            return (1, k)
    
    def neighbours(self, k):
        i, j = k
        if i == 0 and j == 0:
            s = self.board[1][1] + self.board[0][1] + self.board[1][0]
        elif i == 19 and j == 0:
            s = self.board[1][19] + self.board[0][18] + self.board[1][18]
        elif i == 0 and j == 19:
            s = self.board[19][1] + self.board[18][0] + self.board[18][1]
        elif i == 19 and j == 19:
            s = self.board[18][19] + self.board[19][18] + self.board[18][18]
        elif i == 0:
            s = self.board[j + 1][0] + self.board[j - 1][0] + self.board[j + 1][1] + self.board[j][1] + self.board[j - 1][1]
        elif i == 19:
            s = self.board[j + 1][19] + self.board[j - 1][19] + self.board[j + 1][18] + self.board[j][18] + self.board[j - 1][18]
        elif j == 0:
            s = self.board[1][i] + self.board[0][i - 1] + self.board[1][i + 1] + self.board[0][i + 1] + self.board[1][i - 1]
        elif j == 19:
            s = self.board[18][i] + self.board[19][i + 1] + self.board[18][i + 1] + self.board[19][i - 1] + self.board[18][i - 1]
        else:
            s = self.board[j + 1][i - 1] + self.board[j - 1][i + 1] + self.board[j - 1][i - 1] + self.board[j + 1][i + 1] + self.board[j - 1][i] + self.board[j + 1][i] + self.board[j][i - 1] + self.board[j][i + 1]
        if s == 0:
            return '0.png'
        if s == 1:
            return '1.png'
        if s == 2:
            return '2.png'
        if s == 3:
            return '3.png'
        if s == 4:
            return '4.png'
        if s == 5:
            return '5.png'
        if s == 6:
            return '6.png'
        if s == 7:
            return '7.png'
        if s == 8:
            return '8.png'

def loadImage(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

pygame.init()
size = width, height = 710, 710
screen = pygame.display.set_mode(size)
board = Board(20, 20)
running = True
board.render()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                h = board.get_click(event.pos)
                i = h[1][0]
                j = h[1][1]
                if h[0] == 1:
                    image = loadImage('bomb.png')
                    screen.blit(image, (i * 30 + 10, j * 30 + 10))
                else:
                    screen.blit(h[2], (i * 30 + 10, j * 30 + 10))
            if event.button == 3:
                cell = board.get_cell(event.pos)
                g = board.on_click2(cell)
                i = g[1][0]
                j = g[1][1]
                if g[0] == 1:
                    image = loadImage('orange.png')
                    screen.blit(image, ((i * 30 + 11, j * 30 + 11)))
                else:
                    image = loadImage('black.png')
                    screen.blit(image, ((i * 30 + 11, j * 30 + 11)))
    pygame.display.flip()
pygame.quit()
