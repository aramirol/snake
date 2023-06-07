import pygame
import time
import random

# Dimensiones de la pantalla
width = 800
height = 600

# Colores RGB
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

pygame.init()

# Crear ventana de juego
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_block = 20  # Tamaño de la serpiente
snake_speed = 15

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])


def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    window.blit(value, [10, 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Cambio en la posición de la serpiente
    x1_change = 0
    y1_change = 0

    # Cuerpo de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Posición aleatoria de la manzana
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0  # Tamaño de la manzana
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0  # Tamaño de la manzana

    while not game_over:

        while game_close:
            window.fill(black)
            message("Game Over. Press R to restart or Q to quit.", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0  # Tamaño de la manzana
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0  # Tamaño de la manzana
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()


game_loop()
