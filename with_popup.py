import time
import pygame, sys
import numpy


pygame.init()

widthofscreen= 600
heightofscreen= 600
board_rows= 3
board_cols= 3

#rgb format index for each component varies between 0 and 255
red =(255, 0, 0)
#green =(0, 255, 0)
#blue =(0,0, 255)
bgcolor= (200, 50, 180)
linecolor= (125, 0, 125)
circle_radius= 80
circle_width= 10
circle_color= (0, 0, 0)
cross_width= 25
space= 35
cross_color= (0, 0, 0)

screen= pygame.display.set_mode((widthofscreen, heightofscreen))
pygame.display.set_caption("\t\tTicTacToe GAME! :)")     #sets title
screen.fill(bgcolor)   #sets color to screen

#to draw line on the screen
#pygame.draw.line(screen, blue, (10, 10), (300,300), 10) #pygame.draw.line(screenobj, color,startingcoordasatuple,endingcooredasatuple,linewidth) 

board= numpy.zeros( (board_rows, board_cols))
#print(board)

def drawlines():
    pygame.draw.line(screen, linecolor, (10, 190),(590, 190), 10)
    pygame.draw.line(screen, linecolor, (10, 390), (590, 390), 10)
    pygame.draw.line(screen, linecolor,(190, 10),(190, 590), 10)
    pygame.draw.line(screen, linecolor, (390, 10), (390, 590), 10)


def xo_mark(player):
    for x in range(board_rows):
        for y in range(board_cols):
            if player!=1 and board[x][y]==1: 
                pygame.draw.circle(screen, circle_color, (int(col*190+ 95), int(row*190 +95)), circle_radius, circle_width)
                #to draw circle
                #format: (screen, color, (centre_coordinates), circle's radius, circle's width)
            if player!=2 and board[x][y]==2:
                a=int(x*190)
                b= int(y*190)
                #pygame.draw.line(screen, circle_color, (a,b), (a+190, b+190), 5)
                pygame.draw.line(screen, cross_color,(b+ space, a+ 190- space),(b+ 190- space, a+space), cross_width)
                pygame.draw.line(screen, cross_color, (b+ space, a+ space), (b+ 190-space, a+190-space), cross_width)

def goto_square(row, col, player):
    board[row][col]= player

def check_iffree(row, col):
    if not board[row][col]:
        return True
    return False

def is_boardfull():
    for x in range(board_rows):
        for y in range(board_cols):
            if check_iffree(x, y):
                return False
    return True

def vertical_win_line(col):
    begin_pos = col*190 + 95
    pygame.draw.line(screen, linecolor, (begin_pos, 20),(begin_pos, 580), 20 )
  

def horizontal_win_line(row):
    begin_pos = row*190 + 95
    print('Helloo horizontal')
    pygame.draw.line(screen, linecolor, (20, begin_pos),(580, begin_pos), 20)

def diag_desc_win_line():
    pygame.draw.line(screen, linecolor, (20,20),(580, 580), 20)

def diag_asc_win_line():
    pygame.draw.line(screen, linecolor, (580,20), (20, 580), 20)

flag=0

def check_win(player):

    #vertical
    for y in range(board_cols):
        if board[0][y]==player and board[1][y]==player and board[2][y]==player:
            vertical_win_line(y)
            print("Vertical win for player ",player)
            flag=1
            return flag
                         
    #horizontaal
    for x in range(board_rows):
       if board[x][0]==player and board[x][1]==player and board[x][2]==player:
           horizontal_win_line(x)
           print("Horizontal win by player ",player)
           flag=1
           return flag
    
    #diag_desc
    cnt=0
    for x in range(3):
        if board[x][x]==player:
            cnt=cnt+1
        if cnt==3:
            diag_desc_win_line()
            print("d1 win by player ",player)
            flag=1
            return flag
        

    #diag_asc
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        diag_asc_win_line()
        print("d2 win by player ",player)    
        flag=1
        return flag
    flag=0
    return flag

def restart(player):
    screen.fill(bgcolor)
    drawlines()
    player=player%2 +1
    for i in range(board_rows):
        for j in range(board_cols):
            board[i][j]=0


drawlines()
#main loop to make sure the screen stays put, its always the same:
player=1
var=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not var:
            mouseX = event.pos[0]   #get X coord
            mouseY = event.pos[1]   #get Y coord

            clicked_row= int(mouseY)
            clicked_col= int(mouseX)

            row, col= 0,0

            if clicked_row in range(190): row=0
            elif clicked_row in range(380): row=1
            elif clicked_row in range(570): row=2

            if clicked_col in range(190): col=0
            elif clicked_col in range(380): col=1
            elif clicked_col in range(570): col=2

            if check_iffree(row, col):
                goto_square(row, col, player)
                var=check_win(player)
                player= player%2 +1 
                xo_mark(player) 
                if var: 
                    xo_mark(player)
                    restart(player)
    pygame.display.update()     #to update the set color



    