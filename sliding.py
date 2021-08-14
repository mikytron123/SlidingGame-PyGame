import numpy as np
import pygame
from pygame.locals import *
import sys
import random
SQUARESIZE = 100
m,n = 5,5
HEIGHT=SQUARESIZE *m
WIDTH=SQUARESIZE *n
board = np.arange(1,m*n+1,1)
board.resize((m,n))


class SlidingGame:
    def __init__(self,board):
        self.board = board 
    
    def rotationA(self,pointA,pointB,pointC,dir):
        q = pointC[1] - pointB[1]
        r = pointB[0]
        p = abs(pointB[0] - pointA[0])
        c = pointA[1]
        if dir == "CW":
            self.board = self.moveboard(pointB,"W",-q)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,"S",p)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,"E",q)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,"N",-p)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
        elif dir == "CCW":
            self.board = self.moveboard(pointB,"S",p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,"W",-q)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,"N",-p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,"E",q)
            self.drawboard()
            pygame.display.update()
        return self.board


    def rotationB(self,pointA,pointB,pointC,dir):
        q = pointB[1] - pointA[1]
        r = pointB[0]
        p = abs(pointC[0] - pointA[0])
        c = pointA[1]
        if dir == "CW":
            self.board = self.moveboard(pointA,"N",-p)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,"W",-q)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,"S",p)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,"E",q)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
        elif dir == "CCW":
            self.board = self.moveboard(pointA,"S",p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,"W",-q)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,"N",-p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,"E",q)
            self.drawboard()
            pygame.display.update()
        return self.board

    def rungame(self):
        running = True
        moved=False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.font = pygame.font.SysFont('arial',20)

        self.board = self.randomize()
        self.drawboard()
        pygame.display.update()

        while running:
            for event in pygame.event.get():
                #self.screen.fill((0,0,0))
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    elem = event.pos[0]//SQUARESIZE,event.pos[1]//SQUARESIZE
                    elemx,elemy = elem
                if event.type == pygame.MOUSEBUTTONUP:
                    elem2 = event.pos[0]//SQUARESIZE,event.pos[1]//SQUARESIZE
                    elem2x,elem2y = elem2
                    deltax = elem2x-elemx
                    deltay = elem2y - elemy
                    if deltax > 0:
                        direc = 'E'
                        amount = deltax
                    elif deltax < 0:
                        direc = 'W'
                        amount = deltax
                    elif deltay < 0:
                        direc = 'N'
                        amount = deltay
                    elif deltay > 0:
                        direc = 'S'
                        amount = deltay
                    moved = True
                if moved:

                    elem = elem[1],elem[0]
                    board = self.moveboard(elem,direc,amount)
                    moved=False
                    self.drawboard()
                    pygame.display.update()

#                state = checkwin(self.board)

    def randomize(self):
        direcs = ["N","S","W","E"]
        for i in range(100):
            randx = random.randint(0,m-1)
            randy = random.randint(0,n-1)
            direc = random.choice(direcs)
            amount = random.randint(1,m-1)
            elem = randx,randy
            self.board = self.moveboard(elem,direc,amount)
        return self.board
        

    def checkwin(self):
        size = self.board.size
        solved = np.arange(1,size+1,1)
        solved.resize(self.board.shape)
        return np.array_equal(solved,self.board)
        
    def drawboard(self):
        shape = self.board.shape
        self.screen.fill((0,0,0))
        for x in range(shape[0]):
            for y in range(shape[1]):
                pygame.draw.rect(self.screen,(255,255,255),
                    [x*SQUARESIZE,y*SQUARESIZE,SQUARESIZE,SQUARESIZE],3)
                numtxt = str(self.board[y][x])
                img = self.font.render(numtxt,True,(255,255,255))
                posx,posy = int(x*SQUARESIZE + SQUARESIZE//3),int(y*SQUARESIZE + SQUARESIZE//3)
                self.screen.blit(img,(posx,posy))
        


    def moveboard(self,elem,direc,amount):
        x,y = elem
        if direc == "N":
            self.board[:,y] = np.roll(self.board[:,y],amount)
        if direc == "S":
            self.board[:,y] = np.roll(self.board[:,y],amount)
        if direc == "W":
            self.board[x,:] = np.roll(self.board[x,:],amount)
        if direc == "E":
            self.board[x,:] = np.roll(self.board[x,:],amount)
        return self.board
        
if __name__ == "__main__":

    game = SlidingGame(board)
    game.rungame()