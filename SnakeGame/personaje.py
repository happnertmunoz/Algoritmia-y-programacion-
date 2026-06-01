import random

class Snake:
    def __init__(self, canvas, space_size, body_parts, color):
        self.space_size = space_size
        self.color = color
        self.body_size = body_parts
        self.coordinates = [[0, 0] for _ in range(body_parts)]
        self.squares = []
        self.draw(canvas)

    def draw(self, canvas):
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + self.space_size, y + self.space_size, 
                fill=self.color, tag="snake"
            )
            self.squares.append(square)

class Food:
    def __init__(self, canvas, game_width, game_height, space_size, color, snake_coordinates=None):
        self.space_size = space_size
        
        # Si no se pasan coordenadas (como en el inicio), usamos una lista vacía
        if snake_coordinates is None:
            snake_coordinates = []
            
        while True:
            x = random.randint(0, (game_width // space_size) - 1) * space_size
            y = random.randint(0, (game_height // space_size) - 1) * space_size
            
            # Validamos si la posición tentativa se cruza con el cuerpo
            if [x, y] not in snake_coordinates:
                self.coordinates = [x, y]
                break

        canvas.create_oval(
            x, y, x + space_size, y + space_size, 
            fill=color, tag="food"
        )
        