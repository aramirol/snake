import pygame
import secrets
import os

# Dimensiones y colores
width, height = 800, 600
white, green, red, black, yellow = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0), (255, 255, 0)
gold = (255, 215, 0)  # --- NUEVO: Color para la manzana dorada ---

# Parámetros del juego
snake_block = 20
INITIAL_SNAKE_SPEED = 10
HIGHSCORE_FILE = 'highscore.txt'

# --- NUEVO: Parámetros de la Manzana Dorada ---
GOLDEN_APPLE_CHANCE = 10  # Probabilidad de 1 en 10
GOLDEN_APPLE_SCORE = 5    # Puntos que otorga

# Inicializar Pygame
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake con Manzana Dorada")
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("consolas", 35)

# Funciones de carga/guardado y dibujo (sin cambios)
def load_high_score():
    if not os.path.exists(HIGHSCORE_FILE): return 0
    try:
        with open(HIGHSCORE_FILE, 'r') as f: return int(f.read())
    except (ValueError, FileNotFoundError): return 0

def save_high_score(score):
    with open(HIGHSCORE_FILE, 'w') as f: f.write(str(score))

def draw_snake(snake_list):
    head = snake_list[-1]
    pygame.draw.rect(window, yellow, [head[0], head[1], snake_block, snake_block])
    for segment in snake_list[:-1]:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_block, snake_block])

def display_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center: text_rect.center = (x, y)
    else: text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)

# --- MODIFICADO: generate_food ahora devuelve el tipo de manzana ---
def generate_food(snake_list):
    """Genera una posición y tipo para la comida."""
    while True:
        foodx = round(secrets.randbelow((width - snake_block) // snake_block)) * snake_block
        foody = round(secrets.randbelow((height - snake_block) // snake_block)) * snake_block
        if [foodx, foody] not in snake_list:
            break
    
    # Decide si la manzana es dorada
    if secrets.randbelow(GOLDEN_APPLE_CHANCE) == 0:
        food_type = 'golden'
    else:
        food_type = 'normal'
        
    return foodx, foody, food_type

def main_game():
    high_score = load_high_score()
    
    def play_game():
        # --- Variables de una partida ---
        x1, y1 = width / 2, height / 2
        x1_change, y1_change = 0, 0
        snake_length = 3
        snake_list = [[x1 - 2 * snake_block, y1], [x1 - snake_block, y1], [x1, y1]]
        snake_speed = INITIAL_SNAKE_SPEED
        
        # --- NUEVO: Puntuación independiente ---
        score = 0
        
        # --- MODIFICADO: Ahora obtenemos el tipo de comida ---
        foodx, foody, food_type = generate_food(snake_list)

        while True: # Bucle de la partida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change == 0: x1_change, y1_change = -snake_block, 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0: x1_change, y1_change = snake_block, 0
                    elif event.key == pygame.K_UP and y1_change == 0: y1_change, x1_change = -snake_block, 0
                    elif event.key == pygame.K_DOWN and y1_change == 0: y1_change, x1_change = snake_block, 0

            if not (x1_change == 0 and y1_change == 0):
                x1 += x1_change
                y1 += y1_change

                if x1 >= width or x1 < 0 or y1 >= height or y1 < 0 or [x1, y1] in snake_list:
                    return score # Devuelve la puntuación final

                snake_head = [x1, y1]
                snake_list.append(snake_head)
                if len(snake_list) > snake_length:
                    del snake_list[0]
                
                # --- Lógica de comer comida MODIFICADA ---
                if x1 == foodx and y1 == foody:
                    # La serpiente siempre crece 1
                    snake_length += 1
                    
                    # Los puntos dependen del tipo de manzana
                    if food_type == 'golden':
                        score += GOLDEN_APPLE_SCORE
                    else: # 'normal'
                        score += 1
                    
                    # Generamos una nueva manzana
                    foodx, foody, food_type = generate_food(snake_list)
                    
                    # Comprobamos si sube la velocidad
                    if score > 0 and (score // 10) > ((score - (GOLDEN_APPLE_SCORE if food_type == 'golden' else 1)) // 10):
                        snake_speed += 1

            # --- Lógica de dibujado MODIFICADA ---
            window.fill(black)
            
            # Dibuja la manzana del color correcto
            if food_type == 'golden':
                pygame.draw.rect(window, gold, [foodx, foody, snake_block, snake_block])
            else:
                pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])

            draw_snake(snake_list)
            
            display_text(f"Puntuación: {score}", score_font, white, 10, 10)
            speed_text = score_font.render(f"Velocidad: {snake_speed}", True, white)
            window.blit(speed_text, (width - speed_text.get_width() - 10, 10))
            
            pygame.display.update()
            clock.tick(snake_speed)

    # Bucle principal que controla las pantallas (sin cambios)
    while True:
        window.fill(black)
        display_text("SNAKE GAME", font_style, green, width / 2, height / 3, center=True)
        display_text(f"Puntuación Máxima: {high_score}", font_style, yellow, width / 2, height / 2, center=True)
        display_text("Pulsa cualquier tecla para empezar", font_style, white, width / 2, height * 2 / 3, center=True)
        pygame.display.update()

        waiting_for_start = True
        while waiting_for_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting_for_start = False

        final_score = play_game()

        if final_score > high_score:
            high_score = final_score
            save_high_score(high_score)

        window.fill(black)
        display_text("¡Has perdido!", font_style, red, width / 2, height / 4, center=True)
        display_text(f"Tu Puntuación: {final_score}", font_style, white, width / 2, height / 2, center=True)
        display_text(f"Puntuación Máxima: {high_score}", font_style, yellow, width / 2, height / 2 + 50, center=True)
        display_text("Pulsa 'R' para reiniciar o 'Q' para salir", font_style, white, width / 2, height * 3 / 4, center=True)
        pygame.display.update()

        waiting_for_end = True
        while waiting_for_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    waiting_for_end = False

main_game()