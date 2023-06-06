import random

class Food:
    def __init__(self, window_width, window_height, apple_size):
        self.window_width = window_width
        self.window_height = window_height
        self.apple_size = apple_size
        self.position = self.generate_food()
    
    def generate_food(self):
        x = random.randrange(0, self.window_width, self.apple_size)
        y = random.randrange(0, self.window_height, self.apple_size)
        return (x, y)
