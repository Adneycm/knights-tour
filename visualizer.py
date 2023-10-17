import pygame
from solution import KnightsTour
import time
from constants import *


class Visualization:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.ROWS = 8
        self.COLS = 8
        self.SQUARE_SIZE = (self.WIDTH-200) // self.COLS
        self.B_WIDTH = self.COLS * self.SQUARE_SIZE
        self.B_HEIGHT = self.ROWS * self.SQUARE_SIZE
        self.B_X = (self.WIDTH - self.B_WIDTH) // 2
        self.B_Y = (self.HEIGHT - self.B_HEIGHT) // 2

        self.WIN = None
        self.image = None
        self.imageRect = None
        self.font = None
        self.selectedSquare = None
        self.moveSound = None
        self.run = True
        self.tour = False
        

    def initialize(self):
        pygame.init()
        pygame.mixer.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.WIN.fill(BLUE)
        # Move Sound
        self.moveSound = pygame.mixer.Sound(AUDIO_MOVE)
        # Font
        self.font = pygame.font.Font(None, 36)
        # Knight's Image
        self.image = pygame.image.load(IMG_KNIGHT)
        self.image = pygame.transform.scale(self.image, (self.SQUARE_SIZE, self.SQUARE_SIZE))
        self.imageRect = self.image.get_rect()  

    def boardSize(self):
        self.SQUARE_SIZE = (self.WIDTH-200) // self.COLS
        self.B_WIDTH = self.COLS * self.SQUARE_SIZE
        self.B_HEIGHT = self.ROWS * self.SQUARE_SIZE
        self.B_X = (self.WIDTH - self.B_WIDTH) // 2
        self.B_Y = (self.HEIGHT - self.B_HEIGHT) // 2

        self.image = pygame.image.load(IMG_KNIGHT)
        self.image = pygame.transform.scale(self.image, (self.SQUARE_SIZE, self.SQUARE_SIZE))
        self.imageRect = self.image.get_rect()

    def drawTitle(self):
        title = self.font.render(CAPTION, True, DARKBLUE)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2,HEIGHT//2 - 330)
        self.WIN.blit(title, titleRect)

    def drawC(self):
        c = pygame.image.load(IMG_C)
        c = pygame.transform.scale(c, (60, 60))
        cRect = c.get_rect()
        cRect.center = (WIDTH//2 - 220 ,HEIGHT//2 - 290)
        self.WIN.blit(c, cRect)
        cInst = self.font.render("Clear board", True, DARKBLUE)
        cInstRect = cInst.get_rect()
        cInstRect.center = (WIDTH//2 - 120, HEIGHT//2 - 290)
        self.WIN.blit(cInst, cInstRect)

    def drawSpace(self):
        space = pygame.image.load(IMG_SPACE)
        space = pygame.transform.scale(space, (120, 120))
        spaceRect = space.get_rect()
        spaceRect.center = (WIDTH//2 + 220 ,HEIGHT//2 - 290)
        self.WIN.blit(space, spaceRect)
        spaceInst = self.font.render("Start tour", True, DARKBLUE)
        spaceInstRect = spaceInst.get_rect()
        spaceInstRect.center = (WIDTH//2 + 120, HEIGHT//2 - 290)
        self.WIN.blit(spaceInst, spaceInstRect)

    def drawBoard(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(self.WIN, color, (self.B_X + col * self.SQUARE_SIZE, self.B_Y + row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

    def drawKnight(self, coordinates):
        row, col = coordinates
        self.imageRect.topleft = (self.B_X + col * self.SQUARE_SIZE, self.B_Y + row * self.SQUARE_SIZE)
        self.WIN.blit(self.image, self.imageRect)

    def drawPosition(self, coordinates, n):
        row, col = coordinates
        text = self.font.render(str(n), True, DARKBLUE)
        textRect = text.get_rect()
        textRect.center = (self.B_X + col * self.SQUARE_SIZE + 30, self.B_Y + row * self.SQUARE_SIZE + 30)
        self.WIN.blit(text, textRect)

    def drawTour(self, row, col):
        k = KnightsTour(self.ROWS, row, col)
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
            self.moveSound.play()
            pygame.display.update()

    def drawGame(self):
        self.WIN.fill(BLUE)
        self.boardSize()
        self.drawTitle()
        self.drawBoard()
        self.drawC()
        self.drawSpace()

    def visualize(self):
        self.drawGame()
        while self.run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.tour = True
                    elif event.key in (pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                        self.selectedSquare = None
                        n = int(pygame.key.name(event.key))
                        self.ROWS = n
                        self.COLS = n
                        self.drawGame()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the coordinates of the click
                    x, y = pygame.mouse.get_pos()
                    col = (x - self.B_X) // self.SQUARE_SIZE
                    row = (y - self.B_Y) // self.SQUARE_SIZE
                    if row >= 0 and row <= self.ROWS and col >= 0 and col <= self.COLS :
                        self.selectedSquare = (row, col)

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