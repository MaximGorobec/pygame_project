import pygame
from pygame import Color
class Board:
    # создание поля
    def __init__(self, width, height):
        self.player_speed = 1
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]
        self.board[0][0] = 1
        # значения по умолчанию
        self.left = 20
        self.top = 50
        self.cell_size = 200

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 1:
                    r = self.cell_size
                else:
                    r = 1
                pygame.draw.rect(screen, Color('white'), (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), r)
        pygame.draw.circle(screen, Color('green'), (screen.get_width() // 2, screen.get_height() // 2), 30)

    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if (0 <= pos[0] <= self.width - 1) and (0 <= pos[1] <= self.height - 1):
            return pos
        return (0, 0)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell != None) and (cell[0] >= 0) and (cell[1] >= 0):
            self.on_click(cell)

    def on_click(self, cell):
        self.board[cell[0]][cell[1]] = abs(self.board[cell[0]][cell[1]] - 1)

