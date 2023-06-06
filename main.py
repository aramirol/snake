import pygame
from snake import Snake
from food import Food

# Initialize Pygame
pygame.init()

# Game window dimensions
window_width = 800
window_height = 600

# Size of the snake and apples
snake_size = 20
apple_size = 20

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Initialize the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

snake = Snake(window_width, window_height, snake_size)
food = Food(window_width, window_height, apple_size)

clock = pygame.time.Clock()

# Initial score
score = 0

# Font for the score display
font = pygame.font.Font(None, 36)

# Function to restart the game
def restart_game():
    global snake, food, score
    snake = Snake(window_width, window_height, snake_size)
    food = Food(window_width, window_height, apple_size)
    score = 0

# Main game loop
running = True
restart = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
    
    if not restart:
        snake.move()
        if snake.position[0] == food.position:
            food.position = food.generate_food()
            score += 10
        else:
            snake.position.pop()
        
        if snake.check_collision():
            restart = True
    
    window.fill(black)
    
    # Draw the snake
    for x, y in snake.position:
        pygame.draw.rect(window, green, (x, y, snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(window, red, (food.position[0], food.position[1], apple_size, apple_size))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

    pygame.display.update()

    # Check if the game has ended
    if restart:
        restart_text = font.render("Game Over. Press R to restart or Q to quit.", True, white)
        restart_rect = restart_text.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(restart_text, restart_rect)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            restart_game()
            restart = False
        elif keys[pygame.K_q]:
            running = False

    # Limit the FPS
    clock.tick(15)

# Quit Pygame
pygame.quit()
