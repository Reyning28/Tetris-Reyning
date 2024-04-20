import pygame
import random
# Inicialización de Pygame y configuración inicial
pygame.font.init()
pygame.init()


# Variables globales
s_width = 800
s_height = 700
play_width = 300  # Ancho del área de juego
play_height = 600   # Alto del área de juego
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# Cargar imágenes de fondo
background = pygame.image.load('front.jpg')
back = pygame.image.load('back2.jpg')
try_again = pygame.image.load('try.jpg')

# Definición de colores en formato RGB
gray = (119, 118, 110)
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 255, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
sea_green = (0, 255, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
light_red = (255, 0, 0)

# Definición de las formas de las piezas del Tetris
shapes = [
    [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']],

    [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']],

    [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']],

    [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']],

    [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']],

    [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']],

    [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
]
# Colores asociados a cada forma de pieza del Tetris
shape_colors = [
    (0, 255, 0),  # S
    (255, 0, 0),  # Z
    (0, 255, 255),  # I
    (255, 255, 0),  # O
    (255, 165, 0),  # J
    (0, 0, 255),  # L
    (128, 0, 128)  # T
]

# Definición de la clase Piece que representa una pieza del Tetris
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# Función para mostrar la pantalla de inicio del juego
def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        s_width = 900
        s_height = 700

        message('TETRIS', red, 100, (s_width / 2 - 200), 100)
        message("Esto No Para Hasta que Mueras", white, 50, (s_width / 2 - 300), 200)
        button(100, 400, 118, 30, 'COMENZAR!', white, bright_red, red, 25, 106, 406, gameloop)
        button(600, 400, 80, 30, 'SALIR', white, bright_green, green, 25, 606, 406, quit1)

        pygame.display.update()

# Función para mostrar la pantalla de fin del juego y opciones
def next_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        s_width = 900
        s_height = 700

        message("QUIRES JUGAR DE NUEVO", yellow, 50, (s_width / 2 - 300), 200)
        button(100, 400, 160, 30, 'JUGAR DE NUEVO', white, bright_red, red, 25, 106, 406, gameloop)
        button(600, 400, 80, 30, 'SALIR', white, bright_green, green, 25, 606, 406, quit1)

        pygame.display.update()


# Función para mostrar texto en la pantalla
def message(mess, colour, size, x, y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(mess, True, colour)
    win.blit(screen_text, (x, y))
    pygame.display.update()

# Función para crear botones en la pantalla
def button(x, y, w, h, mess, mess_color, actc, noc, size, tx, ty, func):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(win, actc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
        if click == (1, 0, 0):
            func()

    else:
        pygame.draw.rect(win, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()

# Función para cerrar el juego
def quit1():
    pygame.quit()
    quit()

# Función principal del juego
def gameloop():
    x = 300
    y = 400
    x_change = 0
    y_change = 0
    global game_over
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        main(win)

        pygame.display.update()

# Función para crear la cuadrícula del juego
def create_grid(locked_pos={}):
    grid = [[(black) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

# Función para convertir el formato de la forma de la pieza
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

# Función para validar si hay espacio para la pieza en la cuadrícula
def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (black)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

# Función para verificar si se perdió el juego
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False

# Función para obtener una nueva pieza aleatoria
def get_shape():
    return Piece(5, 0, random.choice(shapes))

# Función para dibujar la ventana del juego
def draw_window(surface, grid, score=0, last_score=0):
    win.blit(back, (0, 0))

    pygame.font.init()

    font = pygame.font.SysFont("comicsans", 60, bold=True)
    label = font.render('***TETRIS***', 1, (white))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    font = pygame.font.SysFont("comicsansms", 30, bold=True)
    label = font.render('Score: ' + str(score), 1, (black))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100

    surface.blit(label, (sx + 20, sy + 160))

    font = pygame.font.SysFont("comicsansms", 23, bold=True)
    label = font.render('High Score: ' + last_score, 1, (black))

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx + 1, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size,
                                                    block_size, block_size), 0)

    pygame.draw.rect(surface, (red), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)
    pygame.display.update()

# Función principal del juego
def main(win):
    last_score = max_score()
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            pygame.mixer.music.load('gameover.wav')
            pygame.mixer.music.play()
            draw_text_middle(win, "Try Again", 80, (red))
            pygame.display.update()

            pygame.time.delay(1500)
            run = False
            update_score(score)

            win.blit(try_again, (0, 0))
            next_game()
            pygame.quit()
            quit()

# Función para mostrar el menú principal del juego
def main_menu(win):
    run = True
    while run:
        win.fill((255, 255, 255))
        win.blit(background, (0, 0))
        game_intro()
        pygame.quit()
        quit()
        main(win)

    pygame.display.quit()

# Función para obtener la puntuación máxima
def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()

        score = lines[0].strip()

    return score

# Función para actualizar la puntuación máxima
def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

# Función para limpiar filas completas en la cuadrícula
def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
                pygame.mixer.music.load('linecleared.wav')
                pygame.mixer.music.play()

    return inc

# Función para dibujar la próxima forma de pieza que aparecerá en la ventana
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsansms", 30, bold=True)
    label = font.render('Next Shape', 1, (0, 0, 0))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * block_size, sy + i * block_size,
                                                         block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))


# Función para dibujar la cuadrícula del juego en la ventana
def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (gray), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (gray), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))

# Función para mostrar texto en el centro de la pantalla
def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsansms", size, bold=True)
    label = font.render(text, 3, color)

    surface.blit(label, (top_left_x + play_width / - (label.get_width() / 2), top_left_y + play_height / 2 - label.get_height() / 2))

# Función para mostrar texto en el centro de la pantalla
def draw_text_center(surface, text, size, color):
    font = pygame.font.SysFont("comicsansms", size, bold=True)
    label = font.render(text, 3, color)

    surface.blit(label, (top_left_x + play_width / 5 - (label.get_width() / 5), top_left_y + play_height / 5 - label.get_height() / 5))

# Función para mostrar texto en una esquina de la pantalla
def draw_text_corner(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 5, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), top_left_y + play_height / 2 - label.get_height() / 2))

# Iniciar la ventana del juego y el bucle principal
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)
