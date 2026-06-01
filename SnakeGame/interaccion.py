from tkinter import ALL
from interfaz import GameInterface, GAME_WIDTH, GAME_HEIGHT, SPEED, SPACE_SIZE, BODY_PARTS, SNAKE_COLOR, FOOD_COLOR
from personaje import Snake, Food

class GameController:
    def __init__(self):
        self.interface = GameInterface()
        self.score = 0
        self.direction = 'down'
        self.game_started = False
        self.game_over_state = False
        self.snake = None
        self.food = None

        # Vinculación de eventos de usuario
        self.interface.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.interface.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.interface.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.interface.window.bind('<Down>', lambda event: self.change_direction('down'))
        self.interface.window.bind('<r>', self.restart_game)
        self.interface.window.bind('<R>', self.restart_game)

        # Mostrar menú inicial de forma segura
        self.interface.show_start_screen()

    def start_game(self):
        if not self.game_started and not self.game_over_state:
            self.game_started = True
            self.interface.canvas.delete(ALL)
            
            # Instanciación limpia secuencial
            self.snake = Snake(self.interface.canvas, SPACE_SIZE, BODY_PARTS, SNAKE_COLOR)
            self.food = Food(self.interface.canvas, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, FOOD_COLOR, self.snake.coordinates)
            self.next_turn()

    def change_direction(self, new_direction):
        if self.game_over_state:
            return

        if not self.game_started:
            self.start_game()
            return

        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def next_turn(self):
        if not self.game_started:
            return

        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, [x, y])

        square = self.interface.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
        )
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.interface.update_score(self.score)
            self.interface.canvas.delete("food")
            self.food = Food(self.interface.canvas, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, FOOD_COLOR, self.snake.coordinates)
        else:
            del self.snake.coordinates[-1]
            self.interface.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            velocidad_actual = max(50, SPEED - (self.score * 1))
            self.interface.window.after(velocidad_actual, self.next_turn)

    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.game_started = False
        self.game_over_state = True
        self.interface.show_game_over()

    def restart_game(self, event=None):
        self.interface.canvas.delete(ALL)
        self.score = 0
        self.direction = 'down'
        self.interface.update_score(self.score)
        self.game_over_state = False
        self.game_started = True
        self.snake = Snake(self.interface.canvas, SPACE_SIZE, BODY_PARTS, SNAKE_COLOR)
        self.food = Food(self.interface.canvas, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, FOOD_COLOR, self.snake.coordinates)
        self.next_turn()

    def run(self):
        self.interface.window.mainloop()

if __name__ == "__main__":
    game = GameController()
    game.run()