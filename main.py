import pygame
from Board_class import Board
from pygame import Color
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

        # перенести в класс игрока и исправить колизию с обьектами находящимися не в направлении движения
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


        collide_p = board.get_cell((screen.get_width() // 2, screen.get_height() // 2))
        collide_cell = board.board[collide_p[0]][collide_p[1]]
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.display.flip()