import pygame
from pygame import Color
class Board:
    # создание поля
    def __init__(self, width, height):
        self.player_speed = 1
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]
        # значения по умолчанию
        self.left = 20
        self.top = 50
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 1:
                    r = 90
                else:
                    r = 1
                pygame.draw.rect(screen, Color('white'), (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), r)
        pygame.draw.circle(screen, Color('green'), (screen.get_width() // 2, screen.get_height() // 2), 30)
    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if pos[0] <= self.width - 1 and pos[1] <= self.height - 1:
            return pos
        return (-1, -1)
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if (cell != None) and (cell[0] >= 0) and (cell[1] >= 0):
            self.on_click(cell)

    def on_click(self, cell):
        self.board[cell[0]][cell[1]] = abs(self.board[cell[0]][cell[1]] - 1)



if __name__ == '__main__':
    player_r = 30
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 1024, 800
    screen = pygame.display.set_mode(size)
    board = Board(20, 20)
    running = True
    w_key = False
    keys = dict()
    for i in pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d:
        keys[i] = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)


            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                    keys[event.key] = True
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                    keys[event.key] = False
        collide_p = board.get_cell((screen.get_width() // 2, screen.get_height() // 2))
        collide_cell = board.board[collide_p[0]][collide_p[1]]
        # if collide_cell == 1:
        #     board.top = 0
        #     board.left = 0
        if keys[pygame.K_w]:
            collide_p = board.get_cell((screen.get_width() // 2, screen.get_height() // 2 - player_r))
            collide_cell = board.board[collide_p[0]][collide_p[1]]
            if collide_cell == 0:
                board.top += 1
        if keys[pygame.K_a]:
            collide_p = board.get_cell((screen.get_width() // 2 - player_r, screen.get_height() // 2))
            collide_cell = board.board[collide_p[0]][collide_p[1]]
            if collide_cell == 0:
                board.left += 1
        if keys[pygame.K_s]:
            collide_p = board.get_cell((screen.get_width() // 2, screen.get_height() // 2 + player_r))
            collide_cell = board.board[collide_p[0]][collide_p[1]]
            if collide_cell == 0:
                board.top -= 1
        if keys[pygame.K_d]:
            collide_p = board.get_cell((screen.get_width() // 2 + player_r, screen.get_height() // 2))
            collide_cell = board.board[collide_p[0]][collide_p[1]]
            if collide_cell == 0:
                board.left -= 1

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.display.flip()