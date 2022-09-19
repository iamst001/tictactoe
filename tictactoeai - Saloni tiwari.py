import sys 
from tkinter import *
from tkinter import font as tkfont

class Gameboard:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Tic-Tac-Toe")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost", 1)
        self.wld = [0] * 3
        self.gameover = False
        self.gameclose = False
        self.gamecanvas = None
        self.startgame()
        self.tk.mainloop()
    def startgame(self):
        if self.gameover == True and self.gamecanvas is not None:
            self.gamecanvas.destroy()
            self.gameover = False
        self.board = [0] * 9
        self.turncount = 1
        self.gamecanvas = Canvas(self.tk, width=400, height=400)
        self.gamecanvas.pack()
        self.gamecanvas.bind_all('<KeyPress-y>', self.restart)
        self.gamecanvas.bind_all('<KeyPress-Y>', self.restart)
        self.gamecanvas.bind_all('<KeyPress-n>', self.endgame)
        self.gamecanvas.bind_all('<KeyPress-N>', self.endgame)
        self.gamecanvas.bind_all('<KeyPress-0>', self.playZero)
        self.gamecanvas.bind_all('<KeyPress-1>', self.playOne)
        self.gamecanvas.bind_all('<KeyPress-2>', self.playTwo)
        self.gamecanvas.bind_all('<KeyPress-3>', self.playThree)
        self.gamecanvas.bind_all('<KeyPress-4>', self.playFour)
        self.gamecanvas.bind_all('<KeyPress-5>', self.playFive)
        self.gamecanvas.bind_all('<KeyPress-6>', self.playSix)
        self.gamecanvas.bind_all('<KeyPress-7>', self.playSeven)
        self.gamecanvas.bind_all('<KeyPress-8>', self.playEight)
        self.gamecanvas.bind_all('<KeyPress-8>', self.playEight)
        self.gamecanvas.bind_all('<KeyPress-Return>', self.closegame)
        labels = plotBoard(self.board)
        showBoard(self.gamecanvas,labels)
    def restart(self,evt):
        if self.gameover == True:
            self.startgame()
    def endgame(self,evt):
        if self.gameover == True:
            self.gamecanvas.delete('all')
            smallfont = tkfont.Font(family="Arial", size=15)
            self.gamecanvas.create_text(200, 50, font=smallfont, text = 'Thanks for playing!', fill = 'blue')
            winstext = ('Wins: ' + str(self.wld[0]))
            lossestext = ('Losses: ' + str(self.wld[1]))
            drawstext = ('Draws: ' + str(self.wld[2]))
            self.gamecanvas.create_text(200, 100, font=smallfont, text = winstext, fill = 'blue')
            self.gamecanvas.create_text(200, 150, font=smallfont, text = lossestext, fill = 'blue')
            self.gamecanvas.create_text(200, 200, font=smallfont, text = drawstext, fill = 'blue')
            self.gamecanvas.create_text(200, 300, font=smallfont, text = 'Hit Enter to leave.', fill = 'blue')
            self.gameclose = True
    def closegame(self,evt):
        if self.gameover == True and self.gameclose == True:
            self.tk.destroy()
            sys.exit()
    def advanceTurn(self):
        self.turncount += 1
        labels = plotBoard(self.board)
        showBoard(self.gamecanvas,labels)
        winner = checkWin(self.board,self.turncount,self.wld)
        if winner in ['O','X','D']:
            winMessage(self.gamecanvas,winner)
            self.gameover = True
        else:
            self.board = aiMove(self.board,self.turncount)
            self.turncount += 1
            labels = plotBoard(self.board)
            showBoard(self.gamecanvas,labels)
            winner = checkWin(self.board,self.turncount,self.wld)
            if winner in ['O','X','D']:
                winMessage(self.gamecanvas,winner)
                self.gameover = True
    def playZero(self,evt):
        if self.board[0] == 0 and self.gameover == False:
            self.board[0] = 1
            self.advanceTurn()
    def playOne(self,evt):
        if self.board[1] == 0 and self.gameover == False:
            self.board[1] = 1
            self.advanceTurn()
    def playTwo(self,evt):
        if self.board[2] == 0 and self.gameover == False:
            self.board[2] = 1
            self.advanceTurn()
    def playThree(self,evt):
        if self.board[3] == 0 and self.gameover == False:
            self.board[3] = 1
            self.advanceTurn()
    def playFour(self,evt):
        if self.board[4] == 0 and self.gameover == False:
            self.board[4] = 1
            self.advanceTurn()
    def playFive(self,evt):
        if self.board[5] == 0 and self.gameover == False:
            self.board[5] = 1
            self.advanceTurn()
    def playSix(self,evt):
        if self.board[6] == 0 and self.gameover == False:
            self.board[6] = 1
            self.advanceTurn()
    def playSeven(self,evt):
        if self.board[7] == 0 and self.gameover == False:
            self.board[7] = 1
            self.advanceTurn()
    def playEight(self,evt):
        if self.board[8] == 0 and self.gameover == False:
            self.board[8] = 1
            self.advanceTurn()
 
def plotBoard(board):
    ## check values of the board and assign number, X, or O to a list
    currentBoard=['']*9
    for i in range(0,9):
        if board[i] == 0:
            currentBoard[i] = str(i)
        elif board[i] == 1:
            currentBoard[i] = 'X'
        elif board[i] == 2:
            currentBoard[i] = 'O'
    return currentBoard
 
def showBoard(canvas,board):
    ## draw the board for creating or drawing lines we use method create_line(coords,options)here coords are given as four integer number x1,y1,x2,y2.
    canvas.delete('all')
    canvas.create_line(150, 50, 150, 350)
    canvas.create_line(250, 50, 250, 350)
    canvas.create_line(50, 150, 350, 150)
    canvas.create_line(50, 250, 350, 250)
    canvas.create_text(100, 100, text=board[0], font=('Times', 80))
    canvas.create_text(200, 100, text=board[1], font=('Times', 80))
    canvas.create_text(300, 100, text=board[2], font=('Times', 80))
    canvas.create_text(100, 200, text=board[3], font=('Times', 80))
    canvas.create_text(200, 200, text=board[4], font=('Times', 80))
    canvas.create_text(300, 200, text=board[5], font=('Times', 80))
    canvas.create_text(100, 300, text=board[6], font=('Times', 80))
    canvas.create_text(200, 300, text=board[7], font=('Times', 80))
    canvas.create_text(300, 300, text=board[8], font=('Times', 80))
 
def checkWin(board,turncount,wld):
    ##check for X win
    if ((board[0] == board[1] == board[2] == 1) \
        or (board[0] == board[4] == board[8] == 1) \
        or (board[0] == board[3] == board[6] == 1) \
        or (board[3] == board[4] == board[5] == 1) \
        or (board[6] == board[4] == board[2] == 1) \
        or (board[6] == board[7] == board[8] == 1) \
        or (board[1] == board[4] == board[7] == 1) \
        or (board[2] == board[5] == board[8] == 1)):
        wld[0] += 1
        return 'X'
    ##check for O win
    elif ((board[0] == board[1] == board[2] == 2) \
        or (board[0] == board[4] == board[8] == 2) \
        or (board[0] == board[3] == board[6] == 2) \
        or (board[3] == board[4] == board[5] == 2) \
        or (board[6] == board[4] == board[2] == 2) \
        or (board[6] == board[7] == board[8] == 2) \
        or (board[1] == board[4] == board[7] == 2) \
        or (board[2] == board[5] == board[8] == 2)):
        wld[1] += 1
        return 'O'
    ##check for draw
    elif turncount == 10:
        wld[2] += 1
        return 'D'
    else:
        return None
 
def aiMove(board,turncount):
    ## on second turn, take middle square if open, or top left corner if X took middle
    if turncount == 2:
        if board[4] == 0:
            board[4] = 2
        else:
            board[0] = 2
    ## on any turn beyond second, check if O can win, then check if X can win
    ## and make the appropriate move to win or block
    elif (board[3] == board[6] == 2 and board[0] == 0)\
         or (board[1] == board[2] == 2 and board[0] == 0)\
         or (board[4] == board[8] == 2 and board[0] == 0):
        board[0] = 2
    elif (board[0] == board[2] == 2 and board[1] == 0)\
         or (board[4] == board[7] == 2 and board[1] == 0):
        board[1] = 2
    elif (board[0] == board[1] == 2 and board[2] == 0)\
         or (board[6] == board[4] == 2 and board[2] == 0)\
         or (board[5] == board[8] == 2 and board[2] == 0):
        board[2] = 2
    elif (board[0] == board[6] == 2 and board[3] == 0)\
         or (board[4] == board[5] == 2 and board[3] == 0):
        board[3] = 2
    elif (board[0] == board[8] == 2 and board[4] == 0)\
         or (board[3] == board[5] == 2 and board[4] == 0)\
         or (board[6] == board[2] == 2 and board[4] == 0)\
         or (board[1] == board[7] == 2 and board[4] == 0):
        board[4] = 2
    elif (board[3] == board[4] == 2 and board[5] == 0)\
         or (board[2] == board[8] == 2 and board[5] == 0):
        board[5] = 2
    elif (board[0] == board[3] == 2 and board[6] == 0)\
         or (board[4] == board[2] == 2 and board[6] == 0)\
         or (board[7] == board[8] == 2 and board[6] == 0):
        board[6] = 2
    elif (board[1] == board[4] == 2 and board[7] == 0)\
         or (board[6] == board[8] == 2 and board[7] == 0):
        board[7] = 2            
    elif (board[0] == board[4] == 2 and board[8] == 0)\
         or (board[6] == board[7] == 2 and board[8] == 0)\
         or (board[2] == board[5] == 2 and board[8] == 0):
        board[8] = 2
    elif (board[3] == board[6] == 1 and board[0] == 0)\
         or (board[1] == board[2] == 1 and board[0] == 0)\
         or (board[4] == board[8] == 1 and board[0] == 0):
        board[0] = 2
    elif (board[0] == board[2] == 1 and board[1] == 0)\
         or (board[4] == board[7] == 1 and board[1] == 0):
        board[1] = 2
    elif (board[0] == board[1] == 1 and board[2] == 0)\
         or (board[6] == board[4] == 1 and board[2] == 0)\
         or (board[5] == board[8] == 1 and board[2] == 0):
        board[2] = 2
    elif (board[0] == board[6] == 1 and board[3] == 0)\
         or (board[4] == board[5] == 1 and board[3] == 0):
        board[3] = 2
    elif (board[0] == board[8] == 1 and board[4] == 0)\
         or (board[3] == board[5] == 1 and board[4] == 0)\
         or (board[6] == board[2] == 1 and board[4] == 0)\
         or (board[1] == board[7] == 1 and board[4] == 0):
        board[4] = 2
    elif (board[3] == board[4] == 1 and board[5] == 0)\
         or (board[2] == board[8] == 1 and board[5] == 0):
        board[5] = 2
    elif (board[0] == board[3] == 1 and board[6] == 0)\
         or (board[4] == board[2] == 1 and board[6] == 0)\
         or (board[7] == board[8] == 1 and board[6] == 0):
        board[6] = 2
    elif (board[1] == board[4] == 1 and board[7] == 0)\
         or (board[6] == board[8] == 1 and board[7] == 0):
        board[7] = 2            
    elif (board[0] == board[4] == 1 and board[8] == 0)\
         or (board[6] == board[7] == 1 and board[8] == 0)\
         or (board[2] == board[5] == 1 and board[8] == 0):
        board[8] = 2      
##    If we get to this point, it is at least the 4th turn and there
##    is no win possible for either player, so we start checking for
##    more specific scenarios
    ## If it's the 4th turn and X went in the center first,
    ## then O is in top left and any move by X other than
    ## bottom right should have already been countered
    ## thanks to win condition checks
    elif (board[4] == board[8] == 1 and turncount == 4 and board[6] == 0):
        board[6] = 2
    ## check if 7 and 5 are occupied and 8 is open (any other scenario
    ## of two side squares occupied by X is already countered)
    elif (board[7] == board[5] == 1 and board[8] == 0):
        board[8] = 2
         ## check for circumstance where X played a corner followed by non-adjacent
    ## side square, and take the opposite corner
    elif (board[2] == 1 and (board[7] == 1 or board[3] == 1) and board[6] == 0):
        board[6] = 2
    elif (board[0] == 1 and (board[7] == 1 or board[5] == 1) and board[8] == 1):
        board[8] = 2
    ## check for circumstance where X occupies opposite corners and
    ## play a side to prevent any win opportunities
    elif (board[0] == 1 and board[8] == 1 and board[7] == 1):
        board[7] = 2
    elif (board[2] == 1 and board[6] == 1 and board[5] == 0):
        board[5] = 2
    ## if we get to this point, just take the first open square we can find
    else:
        move = 0
        for i in range(0,9):
            if board[i] == 0:
                move = i
                break
        board[move] = 2
    return board
 
def winMessage(canvas,winner):
    fatfont = tkfont.Font(family="Arial", size=75, weight="bold")
    slimfont = tkfont.Font(family="Arial", size=45)
    smallfont = tkfont.Font(family="Arial", size=15)
    if winner == 'X':
        canvas.create_text(200, 100, font=fatfont, text = 'YOU', fill = 'red')
        canvas.create_text(200, 175, font=fatfont, text = 'WON!', fill = 'red')
        canvas.create_text(200, 270, font=slimfont, text = 'IMPOSSIBLE!', fill = 'red')
        canvas.create_text(200, 360, font=smallfont, text = 'Enter Y to play again or N to quit.', fill = 'black')
    elif winner == 'O':
        canvas.create_text(200, 35, font=slimfont, text = 'O WINS!', fill = 'blue')
        canvas.create_text(200, 160, font=slimfont, text = 'GAME', fill = 'blue')
        canvas.create_text(200, 240, font=slimfont, text = 'OVER', fill = 'blue')
        canvas.create_text(200, 360, font=smallfont, text = 'Enter Y to play again or N to quit.', fill = 'black')
    elif winner == 'D':
        canvas.create_text(200, 35, font=slimfont, text = 'DRAW', fill = 'blue')
        canvas.create_text(200, 160, font=slimfont, text = 'GAME', fill = 'blue')
        canvas.create_text(200, 240, font=slimfont, text = 'OVER', fill = 'blue')
        canvas.create_text(200, 360, font=smallfont, text = 'Enter Y to play again or N to quit.', fill = 'black')
 
Gameboard()
