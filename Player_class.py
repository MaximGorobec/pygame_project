from Entity_class import Entity
class Player(Entity):
    pass


# if keys[pygame.K_w]:
#     collide_p = board.get_cell((screen.get_width() // 2, screen.get_height() // 2 - player_r))
#     collide_cell = board.board[collide_p[0]][collide_p[1]]
#     if collide_cell == 0:
#         board.top += 1
# if keys[pygame.K_a]:
#     collide_p = board.get_cell((screen.get_width() // 2 - player_r, screen.get_height() // 2))
#     collide_cell = board.board[collide_p[0]][collide_p[1]]
#     if collide_cell == 0:
#         board.left += 1
# if keys[pygame.K_s]:
#     collide_p = board.get_cell((screen.get_width() // 2, screen.get_height() // 2 + player_r))
#     collide_cell = board.board[collide_p[0]][collide_p[1]]
#     if collide_cell == 0:
#         board.top -= 1
# if keys[pygame.K_d]:
#     collide_p = board.get_cell((screen.get_width() // 2 + player_r, screen.get_height() // 2))
#     collide_cell = board.board[collide_p[0]][collide_p[1]]
#     if collide_cell == 0:
#         board.left -= 1