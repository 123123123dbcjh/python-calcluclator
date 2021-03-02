import pygame as pg,sys
from pygame.locals import *
import time

#initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)

#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]
board = [' ' for x in range(10)]


#initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe")

#loading the images
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

#resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))

def bconv(TTT):
    board = [' ' for x in range(10)]
    z=1
    for i in TTT:
        for j in i:
            if j=='x':
                board[z]='X'
            elif j=='o':
                board[z]='O'
            else:
                board[z]=' '
            z+=1
    print(board)
    return board

def tconv(board):
    TTT = [[None]*3,[None]*3,[None]*3]

    z=1
    for i in range(len(TTT)):
        for j in range(len(TTT[i])):
            if board[z]=='X':
                TTT[i][j]='x'
            elif board[z]=='O':
                TTT[i][j]='o'
            else:
                TTT[i][j]=None
            z+=1
    print(TTT)
    return TTT

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '




def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    
    # Drawing vertical lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()
    

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global TTT, winner,draw

    # check for winning rows
    for row in range (0,3):
        if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and(TTT [row][0] is not None)):
            # this row won
            winner = TTT[row][0]
            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                              (width, (row + 1)*height/3 - height/6 ), 4)
            break

    # check for winning columns
    for col in range (0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
            # this column won
            winner = TTT[0][col]
            #draw winning line
            pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\
                          ((col + 1)* width/3 - width/6, height), 4)
            break

    # check for diagonal winners
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        # game won diagonally left to right
        winner = TTT[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
       

    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        # game won diagonally right to left
        winner = TTT[0][2]
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)
    
    if(all([all(row) for row in TTT]) and winner is None ):
        draw = True
    draw_status()


def drawXO(row,col):
    global TTT,XO
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30

    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
    TTT[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img,(posy,posx))
        XO= 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO= 'x'
    pg.display.update()
    #print(posx,posy)
    #print(TTT)
   
    

def userClick():
    #get coordinates of mouse click
    x,y = pg.mouse.get_pos()

    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
        
    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)
    

    if(row and col and TTT[row-1][col-1] is None):
        global XO
        
        #draw the x or o on screen
        drawXO(row,col)
        check_win()

def Cclick(move):
    z=1
    for i in range(3):
        for j in range(3):
            if move==z:
                return (i,j)
            z+=1


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def compMove():
    board=bconv(TTT)
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
        
        

def reset_game():
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner=None
    TTT = [[None]*3,[None]*3,[None]*3]
    board = [' ' for x in range(10)]
    

game_opening()

# run the game loop forever
while not(isBoardFull(board)):
    """for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        else:
            pass"""
    # the user clicked; place an X or O
    board=bconv(TTT)
    #while :
    #print(board)
    if not(isWinner(board, 'O')):
        userClick()
        board=bconv(TTT)
        check_win()
    else:
        print('Sorry, O\'s won this time!')
        break


    if not(isWinner(board, 'X')):
        move = compMove()

        if move == 0:
            print('Tie Game!')
        else:
            insertLetter('O', move)
            print('Computer placed an \'O\' in position', move , ':')
            TTT=tconv(board)
            x,y=Cclick(move)
            drawXO(x+1,y+1)
            check_win()
    else:
        print('X\'s won this time! Good Job!')
        break

    if isBoardFull(board):
        print('Tie Game!')
    if(winner or draw):
        reset_game()
            
            
    pg.display.update()
    CLOCK.tick(fps)
