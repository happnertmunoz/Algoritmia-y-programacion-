from tkinter import *

# CONSTANTES DE DISEÑO
GAME_WIDTH = 700
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#10B981"      # Verde esmeralda moderno
FOOD_COLOR = "#EF4444"       # Rojo coral vibrante
BACKGROUND_COLOR = "#1F2937" # Gris oscuro premium

class GameInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Retro Snake Pro - Enterprise Edition")
        self.window.resizable(False, False)

        # Marcador con tipografía limpia
        self.label = Label(
            self.window, text="SCORE: 0", 
            font=('Helvetica', 28, 'bold'), fg="#374151"
        )
        self.label.pack(pady=10)

        self.canvas = Canvas(
            self.window, bg=BACKGROUND_COLOR, 
            height=GAME_HEIGHT, width=GAME_WIDTH, 
            highlightthickness=0
        )
        self.canvas.pack()

        self.center_window()

    def center_window(self):
        self.window.update()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def update_score(self, score):
        self.label.config(text=f"SCORE: {score}")

    def show_start_screen(self):
        self.canvas.delete(ALL)
        
        # Forzamos a la ventana a actualizarse antes de dibujar
        self.window.update() 
        
        self.canvas.create_text(
            GAME_WIDTH / 2, GAME_HEIGHT / 3, 
            font=('Helvetica', 45, 'bold'), text="SNAKE GAME", fill="#10B981"
        )
        self.canvas.create_text(
            GAME_WIDTH / 2, GAME_HEIGHT / 2, 
            font=('Helvetica', 14), text="Usa las flechas del teclado para conducir la serpiente.", fill="#9CA3AF"
        )
        self.canvas.create_text(
            GAME_WIDTH / 2, GAME_HEIGHT * 2 / 3, 
            font=('Helvetica', 18, 'bold'), text="Presiona cualquier flecha para iniciar", fill="#F59E0B"
        )

    def show_game_over(self):
        self.canvas.delete(ALL)
        self.window.update()
        
        # Sombra del texto
        self.canvas.create_text(GAME_WIDTH / 2 + 3, GAME_HEIGHT / 2 - 47, font=('Helvetica', 55, 'bold'), text="GAME OVER", fill="#111827")
        self.canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 50, font=('Helvetica', 55, 'bold'), text="GAME OVER", fill="#EF4444")
        
        self.canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 40, font=('Helvetica', 16), text="Presiona 'R' para reiniciar el sistema", fill="#9CA3AF")