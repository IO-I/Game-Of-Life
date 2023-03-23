import pygame
import random
pygame.init()
clock = pygame.time.Clock()
GRID_WIDTH = 1300
GRID_HEIGHT = 1000
CELL_SIZE = 2
DEAD = (0, 0, 0)
ALIVE = (0, 255, 0)
factor = 3
field = [[0 for i in range(int(GRID_WIDTH/factor))]for j in range(int(GRID_HEIGHT/factor))]
nextField = [[0 for i in range(int(GRID_WIDTH/factor))]for j in range(int(GRID_HEIGHT/factor))]
screen_size = (GRID_WIDTH, GRID_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game Of Life")
done = False

def drawBoard():
    global field
    global CELL_SIZE
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 0:
                pygame.draw.rect(screen, DEAD, (j * CELL_SIZE * factor, i * CELL_SIZE * factor, CELL_SIZE * factor, CELL_SIZE * factor))
            if field[i][j] == 1:
                pygame.draw.rect(screen, ALIVE, (j * CELL_SIZE * factor, i * CELL_SIZE * factor, CELL_SIZE * factor, CELL_SIZE * factor))
    return field

def checkLife():
    global field
    global nextField
    for i in range(1, len(field)-1):
        for j in range(1, len(field[i])-1):            
            cp = field[i][j] # current position
            # count the number of neighbors
            counter = field[i+1][j] + field[i-1][j] + field[i][j+1] + field[i][j-1] + field[i+1][j-1] + field[i+1][j+1] + field[i-1][j-1] + field[i-1][j+1]
            #print(type(counter))
            
            if cp == 1: # is cell currently alive?
                if counter < 2 or counter > 3:
                    nextField[i][j] = 0
                else:
                    nextField[i][j] = 1
            else:
                if counter == 3:
                    nextField[i][j] = 1
                else:
                    nextField[i][j] = 0

    field = [row[:] for row in nextField]
    return(field)

# making some cells alive, some not
for i in range(len(field)):
    for j in range(len(field[i])):
        ran = random.randint(0,1)
        if ran == 1:
            field[i][j] = 1
        else:
            field[i][j] = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    checkLife()
    drawBoard()
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
