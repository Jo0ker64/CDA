import tkinter
import random

class Tile:
    """
    Classe représentant une case du jeu.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SnakeGame:
    """
    Classe principale pour gérer le jeu de Snake.
    """
    TILE_SIZE = 20
    ROWS = 20
    COLS = 20

    def __init__(self):
        # Initialisation de la fenêtre de jeu
        self.window = tkinter.Tk()
        self.window.title("Snake")
        self.window.resizable(False, False)

        # Taille de la fenêtre
        self.WINDOW_WIDTH = self.TILE_SIZE * self.COLS
        self.WINDOW_HEIGHT = self.TILE_SIZE * self.ROWS

        # Création du canvas
        self.canvas = tkinter.Canvas(self.window, bg="black", width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.canvas.pack()

        # Centrer la fenêtre
        self.center_window()

        # Variables de jeu
        self.snake = Tile(self.TILE_SIZE * 5, self.TILE_SIZE * 5)  # Tête du serpent
        self.food = Tile(self.TILE_SIZE * 10, self.TILE_SIZE * 10)  # Nourriture
        self.snake_body = []  # Corps du serpent
        self.velocityX = 0  # Direction X
        self.velocityY = 0  # Direction Y
        self.game_over = False
        self.score = 0

        # Liaisons des événements
        self.window.bind("<KeyRelease>", self.change_direction)

    def center_window(self):
        """
        Centre la fenêtre sur l'écran.
        """
        self.window.update()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_x = int((screen_width / 2) - (window_width / 2))
        window_y = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    def change_direction(self, event):
        """
        Change la direction du serpent en fonction de la touche pressée.
        """
        if self.game_over:
            return

        if event.keysym == "Up" and self.velocityY != 1:
            self.velocityX = 0
            self.velocityY = -1
        elif event.keysym == "Down" and self.velocityY != -1:
            self.velocityX = 0
            self.velocityY = 1
        elif event.keysym == "Left" and self.velocityX != 1:
            self.velocityX = -1
            self.velocityY = 0
        elif event.keysym == "Right" and self.velocityX != -1:
            self.velocityX = 1
            self.velocityY = 0

    def move(self):
        """
        Gère le déplacement du serpent et les collisions.
        """
        if self.game_over:
            return

        # Vérification des collisions avec les bords
        if self.snake.x < 0 or self.snake.x >= self.WINDOW_WIDTH or self.snake.y < 0 or self.snake.y >= self.WINDOW_HEIGHT:
            self.game_over = True
            return

        # Vérification des collisions avec le corps du serpent
        for tile in self.snake_body:
            if self.snake.x == tile.x and self.snake.y == tile.y:
                self.game_over = True
                return

        # Collision avec la nourriture
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake_body.append(Tile(self.food.x, self.food.y))
            self.food.x = random.randint(0, self.COLS - 1) * self.TILE_SIZE
            self.food.y = random.randint(0, self.ROWS - 1) * self.TILE_SIZE
            self.score += 1

        # Mise à jour du corps du serpent
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].x = self.snake_body[i - 1].x
            self.snake_body[i].y = self.snake_body[i - 1].y
        if self.snake_body:
            self.snake_body[0].x = self.snake.x
            self.snake_body[0].y = self.snake.y

        # Déplacement de la tête
        self.snake.x += self.velocityX * self.TILE_SIZE
        self.snake.y += self.velocityY * self.TILE_SIZE

    def draw(self):
        """
        Dessine les éléments du jeu.
        """
        self.move()

        self.canvas.delete("all")

        # Dessin de la nourriture
        self.canvas.create_rectangle(
            self.food.x, self.food.y, self.food.x + self.TILE_SIZE, self.food.y + self.TILE_SIZE, fill="red"
        )

        # Dessin du serpent
        self.canvas.create_rectangle(
            self.snake.x, self.snake.y, self.snake.x + self.TILE_SIZE, self.snake.y + self.TILE_SIZE, fill="lime green"
        )
        for tile in self.snake_body:
            self.canvas.create_rectangle(
                tile.x, tile.y, tile.x + self.TILE_SIZE, tile.y + self.TILE_SIZE, fill="lime green"
            )

        # Affichage du score ou du message de fin
        if self.game_over:
            self.canvas.create_text(
                self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2, font="Arial 20", text=f"Game Over: {self.score}", fill="white"
            )
        else:
            self.canvas.create_text(30, 20, font="Arial 10", text=f"Score: {self.score}", fill="white")

        # Appel récursif pour redessiner
        self.window.after(100, self.draw)

    def run(self):
        """
        Démarre le jeu.
        """
        self.draw()
        self.window.mainloop()


# Exemple d'utilisation autonome
if __name__ == "__main__":
    game = SnakeGame()
    game.run()
