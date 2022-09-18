# -*- coding: utf-8 -*-
import pygame, random
map = [['0','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0']]
# Загрузка текстур
map_tile = pygame.image.load("Textures/map.bmp")
map_tile.set_colorkey((255, 255, 255))
yellow_tile = pygame.image.load("Textures/yellow_tile.bmp")
yellow_tile.set_colorkey((255, 255, 255))
red_tile = pygame.image.load("Textures/red_tile.bmp")
red_tile.set_colorkey((255, 255, 255))
yellow = pygame.image.load("Textures/yellow_tile.bmp")
yellow.set_colorkey((255, 255, 255))
red = pygame.image.load("Textures/red_tile.bmp")
red.set_colorkey((255, 255, 255))
logo = pygame.image.load("Textures/logo.jpg")
logo.set_colorkey((255, 255, 255))
logoscale = pygame.transform.scale(logo, (logo.get_width()//5,
                                          logo.get_height()//5))

# Настройки окна
pygame.init()
screen = pygame.display.set_mode((350,350),0,32)
pygame.display.set_caption("Four in a row!")
bgColor = (255,255,255)
mainLoop = True
playerLetter = yellow
player2Letter = red
choicex = 0
menu = True
font = pygame.font.Font(None, 25)
font_active = pygame.font.Font(None, 30)
FBord = font.render("Ничья", True, (0,0,0))
win1 = font.render("Игрок#1 Выиграл!", True, (0, 0, 0))
win2 = font.render("Игрок#2 Выиграл!", True, (0, 0, 0))
mousex = 0
mousey = 0
mousebutton = False


def clearBoard():
    global map
    map = [['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0']]


# Обработка ничьи
def isBoardFull():
    FilledStroke = 0
    FilledTile = 0
    for stroke in map[0:6]:
        for col in stroke:
            if col != '0':
                FilledTile += 1
        FilledStroke += FilledTile
        FilledTile = 0
    if FilledStroke == 42:
        return True
    else:
        return False


# Функция получения хода игрока
def getPlayerMove(playerLetter):
    choiced = False
    global choicex
    global yellow
    while choiced == False:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                choiced = True
                return 'exit'
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    choicex -= 50
                elif i.key == pygame.K_RIGHT:
                    choicex += 50
                elif i.key == pygame.K_SPACE:
                    if map[0][choicex//50] == '0':
                        choiced = True
        if choicex > 300:
            choicex = 0
        elif choicex < 0:
            choicex = 300
        DrawScreen()
        screen.blit(playerLetter, (choicex, 0))
        pygame.display.update()
    return choicex // 50


# Функция рисовки экрана
def DrawScreen():
    screen.fill(bgColor)
    x = 0
    y = 0
    for stroke in map:
        for cln in stroke:
            if cln == '0':
                screen.blit(map_tile, (y * 50, x * 50 + 50))
            elif cln == '1':
                screen.blit(red_tile, (y * 50, x * 50 + 50))
            elif cln == '2':
                screen.blit(yellow_tile, (y * 50, x * 50 + 50))
            y += 1
        y = 0
        x += 1


def whoGoesFirst():
    if random.choice(['0','1']) == '0':
        return 'Игрок#1'
    else:
        return 'Игрок#2'


# Обработка выигрыша
def isWinner(playerLetter):
    if playerLetter == red:
        playerChar = '1'
    else:
        playerChar = '2'
    for stroke in range(7):
        for col in range(4):
            if map[stroke][col] == playerChar and map[stroke][col + 1] == playerChar and map[stroke][col + 2] == playerChar and map[stroke][col + 3] == playerChar:
                return True

    for stroke in range(4):
        for col in range(7):
            if map[stroke][col] == playerChar and map[stroke + 1][col] == playerChar and map[stroke + 2][col] == playerChar and map[stroke + 3][col] == playerChar:
                return True

    for stroke in range(4):
        for col in range(4):
            if map[stroke][col] == playerChar and map[stroke + 1][col + 1] == playerChar and map[stroke + 2][col + 2] == playerChar and map[stroke + 3][col + 3] == playerChar:
                return True

    for stroke in range(7):
        for col in range(7):
            if map[stroke][col] == playerChar and map[stroke + 1][col - 1] == playerChar and map[stroke + 2][col - 2] == playerChar and map[stroke + 3][col - 3] == playerChar:
                return True
    return False


def Menu():
    global mousey, mousex, mousebutton, menu
    clearBoard()
    if mousex in range(150,250) and mousey in range(140, 175):
        menu_1 = font_active.render("Играть", True, (0, 0, 0))
        if mousebutton:
            menu = False
            mousebutton = False
    else:
        menu_1 = font.render("Играть", True, (0, 0, 0))
    if mousex in range(150,250) and mousey in range(175, 210):
        menu_2 = font_active.render("Выход", True, (0, 0, 0))
        if mousebutton:
            pygame.quit()
            mousebutton = False
    else:
        menu_2 = font.render("Выход", True, (0, 0, 0))
    screen.fill(bgColor)
    screen.blit(logoscale, (125, 10))
    screen.blit(menu_1, (150, 150))
    screen.blit(menu_2, (150, 185))
    mousebutton = False


# Главный цикл игры
turn = whoGoesFirst()
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousebutton = True
    if menu:
        Menu()
    else:
        if turn == 'Игрок#1':
            choice = getPlayerMove(playerLetter)
            if choice == 'exit':
                pygame.quit()
            else:
                for stroke in range(len(map)):
                    if map[stroke][choice] == '1' or map[stroke][choice] == '2' or stroke == 6:
                        map[stroke - 1][choice] = '2'
                        break
            if isWinner(playerLetter):
                while menu == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEMOTION:
                            mousex, mousey = event.pos
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousebutton = True
                    screen.fill(bgColor)
                    DrawScreen()
                    screen.blit(win1, [20, 20])
                    if mousex in range(180, 250) and mousey in range(15, 35):
                        gotomenu = font_active.render("Меню", True, (0, 0, 0))
                        if mousebutton:
                            menu = True
                            mousebutton = False
                    else:
                        gotomenu = font.render("Меню", True, (0, 0, 0))
                    screen.blit(gotomenu, [200, 20])
                    pygame.display.update()
            if isBoardFull():
                while menu == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEMOTION:
                            mousex, mousey = event.pos
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousebutton = True
                    screen.fill(bgColor)
                    DrawScreen()
                    screen.blit(FBord, [20, 20])
                    if mousex in range(180, 250) and mousey in range(15, 35):
                        gotomenu = font_active.render("Меню", True, (0, 0, 0))
                        if mousebutton:
                            menu = True
                            mousebutton = False
                    else:
                        gotomenu = font.render("Меню", True, (0, 0, 0))
                screen.blit(gotomenu, [200, 20])
                pygame.display.update()
            turn = 'Игрок#2'

        else:
            choice = getPlayerMove(player2Letter)
            if choice == 'exit':
                pygame.quit()
            else:
                for stroke in range(len(map)):
                    if map[stroke][choice] == '1' or map[stroke][choice] == '2' or stroke == 6:
                        map[stroke - 1][choice] = '1'
                        break
            if isWinner(player2Letter):
                while menu == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEMOTION:
                            mousex, mousey = event.pos
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousebutton = True
                    screen.fill(bgColor)
                    DrawScreen()
                    screen.blit(win2, [20, 20])
                    if mousex in range(180, 250) and mousey in range(15, 35):
                        gotomenu = font_active.render("Меню", True, (0, 0, 0))
                        if mousebutton:
                            menu = True
                            mousebutton = False
                    else:
                        gotomenu = font.render("Меню", True, (0, 0, 0))
                    screen.blit(gotomenu, [200, 20])
                    pygame.display.update()
            if isBoardFull():
                while menu == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEMOTION:
                            mousex, mousey = event.pos
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousebutton = True
                    screen.fill(bgColor)
                    DrawScreen()
                    screen.blit(FBord, [20, 20])
                    if mousex in range(180, 250) and mousey in range(15, 35):
                        gotomenu = font_active.render("Меню", True, (0, 0, 0))
                        if mousebutton:
                            menu = True
                            mousebutton = False
                    else:
                        gotomenu = font.render("Меню", True, (0, 0, 0))
                    screen.blit(gotomenu, [200, 20])
                    pygame.display.update()
            turn = 'Игрок#1'

    pygame.display.update()
