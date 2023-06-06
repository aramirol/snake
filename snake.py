import random

class Snake:
    def __init__(self, window_width, window_height, snake_size):
        self.window_width = window_width
        self.window_height = window_height
        self.snake_size = snake_size
        self.position = [(window_width // 2, window_height // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
    
    def move(self):
        x, y = self.position[0]
        if self.direction == "UP":
            y -= self.snake_size
        elif self.direction == "DOWN":
            y += self.snake_size
        elif self.direction == "LEFT":
            x -= self.snake_size
        elif self.direction == "RIGHT":
            x += self.snake_size
        self.position.insert(0, (x, y))
    
    def change_direction(self, direction):
        if (direction == "UP" and self.direction != "DOWN" or
            direction == "DOWN" and self.direction != "UP" or
            direction == "LEFT" and self.direction != "RIGHT" or
            direction == "RIGHT" and self.direction != "LEFT"):
            self.direction = direction
    
    def check_collision(self):
        x, y = self.position[0]
        if (x < 0 or x >= self.window_width or
            y < 0 or y >= self.window_height or
            (x, y) in self.position[1:]):
            return True
        return False
