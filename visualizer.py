import pygame
from solution import KnightsTour
import time
from constants import *


class Visualization:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.image = pygame.image.load("knight.png")
        self.font = pygame.font.Font(None, 36)


    def initialize(self):
        pygame.display.set_caption("Knights Tour")
        pygame.init()

        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))




WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knights Tour")

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knights Tour")

# Load the image
image = pygame.image.load("knight.png")

# Resize the image to fit the chessboard squares
image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

# Initialize a font
font = pygame.font.Font(None, 36)

# Initialize variables
selected_square = None  # Stores the selected square
image_rect = image.get_rect()

def drawBoard():
    # Draw the chessboard
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawKnight(coordinates):
    row, col = coordinates
    image_rect.topleft = (col * SQUARE_SIZE, row * SQUARE_SIZE)
    screen.blit(image, image_rect)

def drawPosition(coordinates, n):
    row, col = coordinates
    text = font.render(str(n), True, RED)
    text_rect = text.get_rect()
    text_rect.center = (col * SQUARE_SIZE + 40, row * SQUARE_SIZE + 40)
    screen.blit(text, text_rect)

def drawTour(row, col):
    k = KnightsTour(ROWS, row, col)
    if k.tour():
        path = k.getSolution()
        print("solucionado!")

    i = 1
    for move in path[1:]:
        drawBoard()
        drawKnight(move)

        # Número do movimento
        aux = 1
        for move in path[:i]:
            drawPosition(move, aux)
            aux+=1

        i+=1
        time.sleep(.5)
        pygame.display.update()


# Main loop
running = True
tour = False
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the coordinates of the click
            x, y = pygame.mouse.get_pos()
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            selected_square = (row, col)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tour = True
        
    if tour:
        drawTour(row, col)

    while tour:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        tour = False
        
    # Draw the chessboard
    drawBoard()

    # Draw the selected image on the clicked square
    if selected_square is not None:
        drawKnight(selected_square)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
