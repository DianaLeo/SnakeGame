import pygame
import random
from pygame.locals import *

pygame.init()


#class
class Point:
    col = 0
    row = 0
    def __init__(self,c,r) -> None:
        self.col = c
        self.row = r

#some constants
SCREEN_SIZE = (800,600)
screenColor = (180,230,240)
unitSquareLen = 20
unitSquareEdgeColor = (255,255,255)
ROW = SCREEN_SIZE[1] / unitSquareLen #30
COL = SCREEN_SIZE[0] / unitSquareLen #40
direct = ''

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

snake1 = Point(COL / 2, ROW / 2) 
food = Point(random.randint(0, COL-1), random.randint(0,ROW-1))
snakeColor_r = 100
snakeColor_g = 200
snakeColor_b= 200
snakeColor = (snakeColor_r,snakeColor_g,snakeColor_b)
foodColor = (220,220,50)

#setmode return a Surface object, it is a window
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(screenColor)
pygame.display.set_caption('Snake')

# draw unit checked lines and row col numbers
def drawUnitLines():
    x = 1
    while x <= COL:
        pygame.draw.line(screen, unitSquareEdgeColor, (x * unitSquareLen,0), (x * unitSquareLen,SCREEN_SIZE[1]), 1)
        screen.blit(font.render(str(x),False, unitSquareEdgeColor), ((x-1) * unitSquareLen + 1,0))
        pygame.draw.line(screen, unitSquareEdgeColor, (0, x * unitSquareLen), (SCREEN_SIZE[0], x * unitSquareLen), 1)
        screen.blit(font.render(str(x),False, unitSquareEdgeColor), (1, (x-1) * unitSquareLen))
        x = x + 1

drawUnitLines()

snakes = [Point(snake1.col, snake1.row)]

clock = pygame.time.Clock()
n=2

while True:
    #have to use get instead of wait
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key == K_LEFT:
                direct = 'left'
            elif event.key == K_RIGHT:
                    direct = "right"
            elif event.key == K_UP:
                    direct = "up"
            elif event.key == K_DOWN:
                    direct = "down"

    if direct == "left":
        snake1.col -= 1
    if direct == "down":
        snake1.row += 1
    if direct == "up":
        snake1.row -= 1
    if direct == "right":
        snake1.col += 1

    

    snakes.insert(0, Point(snake1.col, snake1.row))
    snakes.pop()

    if snake1.col < 0 or snake1.col > 39 or snake1.row < 0 or snake1.row > 29 :
        exit()

    # on eating food
    if snakes[0].col == food.col and snakes[0].row == food.row :
        food = Point(random.randint(0, COL-1), random.randint(0,ROW-1))
        n = n * 1.2
        if direct == "left":
            snakes.insert(1,Point(snake1.col+1, snake1.row))
        if direct == "down":
            snakes.insert(1,Point(snake1.col, snake1.row-1))
        if direct == "up":
            snakes.insert(1,Point(snake1.col, snake1.row+1))
        if direct == "right":
            snakes.insert(1,Point(snake1.col-1, snake1.row))


    #clear image
    screen.fill(screenColor)
    drawUnitLines()

    snakeColor_r = 100
    snakeColor_g = 200
    snakeColor_b= 200
    snakeColor = (snakeColor_r,snakeColor_g,snakeColor_b)

    for snake in snakes:
        pygame.draw.rect(screen,snakeColor,(snake.col * unitSquareLen, snake.row * unitSquareLen, unitSquareLen, unitSquareLen))
        if snakeColor_r < 255:
            snakeColor_r += 5
            snakeColor_g += 5
            snakeColor_b += 5
            snakeColor = (snakeColor_r,snakeColor_g,snakeColor_b)
    pygame.draw.rect(screen,foodColor,(food.col * unitSquareLen, food.row * unitSquareLen, unitSquareLen, unitSquareLen))
    pygame.display.update()
    
    clock.tick(n)

