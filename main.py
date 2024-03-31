import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,)

pygame.init()
screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode([screenWidth,screenHeight])
pygame.display.set_caption("2048")
background_image = pygame.image.load("images/background.xcf")

i2 = pygame.image.load("images/2.xcf")
i4 = pygame.image.load("images/4.xcf")
i8 = pygame.image.load("images/8.xcf")
i16 = pygame.image.load("images/16.xcf")
i32 = pygame.image.load("images/32.xcf")
i64 = pygame.image.load("images/64.xcf")
i128 = pygame.image.load("images/128.xcf")
i256 = pygame.image.load("images/256.xcf")
i512 = pygame.image.load("images/512.xcf")
i1024 = pygame.image.load("images/1024.xcf")
i2048 = pygame.image.load("images/2048.xcf")
TryAgain = pygame.image.load("images/TryAgain.xcf")

black = (0,0,0)
font = pygame.font.Font("freesansbold.ttf",70)
font_small = pygame.font.Font("freesansbold.ttf",40)
text_sc = font_small.render("Score:", True, black)
text_hs = font_small.render("High Score:", True, black)
text_go = font.render("Game Over!", True, black)

#declare funtions and variables
clock = pygame.time.Clock()
game_over = False
score = 0
p = open("high_scores.txt", "r")
high_score = int(p.readline())
p.close()

def move_up():
    for x in range(0,4):
        for y in range(0,4):
            #check what is the max distance that is safe to move
            if grid[x][y] != 0:
                if y-3 >= 0 and grid[x][y-3] == 0:
                    move_dist = 3
                elif y-2 >= 0 and grid[x][y-2] == 0:
                    move_dist = 2
                elif y-1 >= 0 and grid[x][y-1] == 0:
                    move_dist = 1
                else:
                    move_dist = 0
                #check if we need to add numbers and add them
                if grid[x][y] == grid[x][y-move_dist-1] and y-move_dist-1 >= 0:
                    grid[x][y-move_dist-1] = grid[x][y] *2
                    grid[x][y] = 0
                #othwise just move them
                elif move_dist != 0:
                    grid[x][y-move_dist] = grid[x][y]
                    grid[x][y] = 0
    place_new_tile()
def move_down():
    for x in range(0,4):
        for y in range(0,4):
            #check what is the max distance that is safe to move
            yn = 3-y
            if grid[x][yn] != 0:
                if yn+3 <= 3 and grid[x][yn+3] == 0:
                    move_dist = 3
                elif yn+2 <= 3 and grid[x][yn+2] == 0:
                    move_dist = 2
                elif yn+1 <= 3 and grid[x][yn+1] == 0:
                    move_dist = 1
                else:
                    move_dist = 0
                #check if we need to add numbers and add them
                if yn+move_dist+1 <= 3 and grid[x][yn] == grid[x][yn+move_dist+1]:
                    grid[x][yn+move_dist+1] = grid[x][yn] *2
                    grid[x][yn] = 0
                elif move_dist != 0:
                    grid[x][yn+move_dist] = grid[x][yn]
                    grid[x][yn] = 0
    place_new_tile()
def move_left():
    for x in range(0,4):
        for y in range(0,4):
            #check what is the max distance that is safe to move
            if grid[x][y] != 0:
                if x-3 >= 0 and grid[x-3][y] == 0:
                    move_dist = 3
                elif x-2 >= 0 and grid[x-2][y] == 0:
                    move_dist = 2
                elif x-1 >= 0 and grid[x-1][y] == 0:
                    move_dist = 1
                else:
                    move_dist = 0
                #check if we need to add numbers and add them
                if grid[x][y] == grid[x-move_dist-1][y] and x-move_dist-1 >= 0:
                    grid[x-move_dist-1][y] = grid[x][y] *2
                    grid[x][y] = 0
                #othwise just move them
                elif move_dist != 0:
                    grid[x-move_dist][y] = grid[x][y]
                    grid[x][y] = 0
    place_new_tile()
def move_right():
    for x in range(0,4):
        for y in range(0,4):
            #check what is the max distance that is safe to move
            xn = 3-x
            if grid[xn][y] != 0:
                if xn+3 <= 3 and grid[xn+3][y] == 0:
                    move_dist = 3
                elif xn+2 <= 3 and grid[xn+2][y] == 0:
                    move_dist = 2
                elif xn+1 <= 3 and grid[xn+1][y] == 0:
                    move_dist = 1
                else:
                    move_dist = 0
                #check if we need to add numbers and add them
                if xn+move_dist+1 <= 3 and grid[xn][y] == grid[xn+move_dist+1][y]:
                    grid[xn+move_dist+1][y] = grid[xn][y] *2
                    grid[xn][y] = 0
                elif move_dist != 0:
                    grid[xn+move_dist][y] = grid[xn][y]
                    grid[xn][y] = 0
    place_new_tile()
def place_new_tile():
    global score
    empty_tiles = []
    for x in range(0,4):
        for y in range(0,4):
            if grid[x][y] == 0:
                empty_tiles.append((x,y))
    if len(empty_tiles) == 0:
        print("no empty tiles")
        grid_full_is_game_over()
    else:
        position = empty_tiles[random.randint(0, len(empty_tiles)-1)]
        if random.randint(0,3) == 0:
            grid[position[0]][position[1]] = 4
            score += 4
        else:
            grid[position[0]][position[1]] = 2
            score += 2
def grid_full_is_game_over():
    print("game over func called")
    global game_over
    game_over = True
    for x in range(0,3):
        if grid[x][0] == grid[x][1] or grid[x][1] == grid[x][2] or grid[x][2] == grid[x][3]:
            game_over == False
            print("game over false1")
    for y in range(0,3):
        if grid[0][y] == grid[1][y] or grid[1][y] == grid[2][y] or grid[2][y] == grid[3][y]:
            game_over == False
            print("game over false2")

still_want_to_play = True
while still_want_to_play:
    #grid = [[1024,512,256,128],[8,16,32,64],[4,2,2,32],[0,0,0,8]]
    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #grid = [[8,16,8,16], [16,8,16,8], [8,16,8,16], [16,8,16,16]]
    place_new_tile()
    place_new_tile()

    #game loop
    running = True
    while running:
        #user inputs
        #quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                still_want_to_play = False
        #move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up()
                elif event.key == pygame.K_DOWN:
                    move_down()
                elif event.key == pygame.K_LEFT:
                    move_left()
                elif event.key == pygame.K_RIGHT:
                    move_right()


        #update screen
        screen.blit(background_image, [0,0])
        for x in range(0,4):
            for y in range(0,4):
                if grid[x][y] == 2:
                        screen.blit(i2, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 4:
                        screen.blit(i4, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 8:
                        screen.blit(i8, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 16:
                        screen.blit(i16, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 32:
                        screen.blit(i32, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 64:
                        screen.blit(i64, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 128:
                        screen.blit(i128, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 256:
                        screen.blit(i256, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 512:
                        screen.blit(i512, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 1024:
                        screen.blit(i1024, [16+(196*x), 16+(196*y)])
                elif grid[x][y] == 2048:
                        screen.blit(i2048, [16+(196*x), 16+(196*y)])
        #text stuff
        if game_over:
            screen.blit(text_go, (196,210))
            screen.blit(TryAgain, (350,340))
        if score > high_score:
            high_score = score
        screen.blit(text_sc,(0,0))
        text_sc_n = font_small.render(str(score), True, black)
        screen.blit(text_sc_n, (130,0))
        screen.blit(text_hs, (450,0))
        text_hs_n = font_small.render(str(high_score), True, black)
        screen.blit(text_hs_n, (680,0))


        pygame.display.flip()
        clock.tick(60)

p = open("high_scores.txt", "w")
p.write(str(high_score))
p.close
    
pygame.quit
