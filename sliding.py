from typing import Tuple
import numpy as np
import pygame
from pygame.locals import *
import sys
import random
from enum import Enum

class Direction(Enum):
    East="E"
    West="W"
    North="N"
    South="S"
    
SQUARESIZE = 100
m,n = 3,3
HEIGHT=SQUARESIZE *m
WIDTH=SQUARESIZE *n
board = np.arange(1,m*n+1,1)
board.resize((m,n))


class SlidingGame:
    def __init__(self,board:np.ndarray):
        self.board = board
         
    
    def rotationA(self,pointA,pointB,pointC,dir):
        q = pointC[1] - pointB[1]
        r = pointB[0]
        p = abs(pointB[0] - pointA[0])
        c = pointA[1]
        if dir == "CW":
            self.board = self.moveboard(pointB,Direction.West,-q)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,Direction.South,p)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,Direction.East,q)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,Direction.North,-p)
            pygame.time.wait(500)
            self.drawboard()
            pygame.display.update()
        elif dir == "CCW":
            self.board = self.moveboard(pointB,Direction.South,p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,Direction.West,-q)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,Direction.North,-p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointB,Direction.East,q)
            self.drawboard()
            pygame.display.update()
        return self.board


    def rotationB(self,pointA,pointB,pointC,dir):
        q = pointB[1] - pointA[1]
        r = pointB[0]
        p = abs(pointC[0] - pointA[0])
        c = pointA[1]
        if dir == "CW":
            self.board = self.moveboard(pointA,Direction.North,-p)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,Direction.West,-q)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,Direction.South,p)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,Direction.East,q)
            pygame.time.wait(1000)
            self.drawboard()
            pygame.display.update()
        elif dir == "CCW":
            self.board = self.moveboard(pointA,Direction.South,p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,Direction.West,-q)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,Direction.North,-p)
            self.drawboard()
            pygame.display.update()
            self.board = self.moveboard(pointA,Direction.East,q)
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
                    pygame.display.quit()
                    pygame.quit()
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
                        direc = Direction.East
                        amount = deltax
                    elif deltax < 0:
                        direc = Direction.West
                        amount = deltax
                    elif deltay < 0:
                        direc = Direction.North
                        amount = deltay
                    elif deltay > 0:
                        direc = Direction.South
                        amount = deltay
                    moved = True
                if moved:

                    elem = elem[1],elem[0]
                    board = self.moveboard(elem,direc,amount)
                    moved=False
                    self.drawboard()
                    pygame.display.update()

                state = self.checkwin()
                if state:
                    # If game over is true, draw game over
                    text = self.font.render("Game Over", True, (255,255,255))
                    text_rect = text.get_rect()
                    text_x = self.screen.get_width() / 2 - text_rect.width / 2
                    text_y = self.screen.get_height() / 2 - text_rect.height / 2
                    self.screen.fill((0,0,0))
                    self.screen.blit(text, [text_x, text_y])
                    pygame.display.update()
                    pygame.time.wait(1000)
                    running = False

    def randomize(self):
        direcs = list(Direction)
        for i in range(100):
            randx = random.randint(0,m-1)
            randy = random.randint(0,n-1)
            direc = random.choice(direcs)
            amount = random.randint(1,m-1)
            elem = randx,randy
            self.board = self.moveboard(elem,direc,amount)
        return self.board
        

    def checkwin(self) -> bool:
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
        


    def moveboard(self,elem:Tuple[int,int],direc:Direction,amount:int):
        x,y = elem
        if direc == Direction.North:
            self.board[:,y] = np.roll(self.board[:,y],amount)
        if direc == Direction.South:
            self.board[:,y] = np.roll(self.board[:,y],amount)
        if direc == Direction.West:
            self.board[x,:] = np.roll(self.board[x,:],amount)
        if direc == Direction.East:
            self.board[x,:] = np.roll(self.board[x,:],amount)
        return self.board
        
if __name__ == "__main__":

    game = SlidingGame(board)
    game.rungame()