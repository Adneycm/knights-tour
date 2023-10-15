import pygame
from solution import KnightsTour
import time
from constants import *


class Visualization:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))

        self.image = pygame.image.load("img/knight.png")
        self.imageRect = self.image.get_rect()

        self.font = pygame.font.Font(None, 36)

        self.selectedSquare = None

        self.run = False
        self.tour = False


    def initialize(self):
        pygame.init()
        pygame.display.set_caption("Knights Tour")
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))

    def drawBoard(self):
        # Draw the chessboard
        for row in range(ROWS):
            for col in range(COLS):
                color = WHITE if (row + col) % 2 == 0 else GREEN
                pygame.draw.rect(self.WIN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawKnight(self, coordinates):
        row, col = coordinates
        self.imageRect.topleft = (col * SQUARE_SIZE, row * SQUARE_SIZE)
        screen.blit(self.image, self.imageRect)

    def drawPosition(self, coordinates, n):
        row, col = coordinates
        text = font.render(str(n), True, RED)
        textRect = text.get_rect()
        textRect.center = (col * SQUARE_SIZE + 40, row * SQUARE_SIZE + 40)
        screen.blit(text, textRect)

    def drawTour(self, row, col):
        k = KnightsTour(ROWS, row, col)
        if k.tour():
            path = k.getSolution()
            print("solucionado!")

        i = 1
        for move in path[1:]:
            self.drawBoard()
            self.drawKnight(move)

            # Número do movimento
            aux = 1
            for move in path[:i]:
                self.drawPosition(move, aux)
                aux+=1

            i+=1
            time.sleep(.5)
            pygame.display.update()

    def visualize(self):
        self.run = True
        self.tour = False
        while self.run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the coordinates of the click
                    x, y = pygame.mouse.get_pos()
                    col = x // SQUARE_SIZE
                    row = y // SQUARE_SIZE
                    self.selectedSquare = (row, col)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.tour = True
                
            if self.tour:
                self.drawTour(row, col)

            while self.tour:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        self.tour = False

                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_c:
                                self.tour = False
                
            # Draw the chessboard
            self.drawBoard()

            # Draw the selected image on the clicked square
            if self.selectedSquare is not None:
                self.drawKnight(self.selectedSquare)

            # Update the display
            pygame.display.update()

        # Quit Pygame
        pygame.quit()

v = Visualization(WIDTH, HEIGHT)
v.initialize()
v.visualize()