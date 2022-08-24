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
n = int(input("Enter Grid Size:"))
HEIGHT=SQUARESIZE *n
WIDTH=SQUARESIZE *n
board = np.arange(1,n*n+1,1)
board.resize((n,n))

Point = Tuple[int,int]

class SlidingGame:
    def __init__(self,board:np.ndarray):
        self.board = board
         
    
    def rotationA(self,pointA:Point,pointB:Point,pointC:Point,dir:str):
        #  A
        #  |
        #  p
        #  |
        #  B - q - C
        # 
        
        q = pointC[1] - pointB[1]
        p = abs(pointB[0] - pointA[0])
        if dir == "CW":
            self.moveboard(pointB,Direction.West,q,True,200)
            self.moveboard(pointB,Direction.South,p,True,200)
            self.moveboard(pointB,Direction.East,q,True,200)
            self.moveboard(pointB,Direction.North,p,True,200)
              
        elif dir == "CCW":
            self.moveboard(pointB,Direction.South,p,True,200)
            self.moveboard(pointB,Direction.West,q,True,200)
            self.moveboard(pointB,Direction.North,p,True,200)
            self.moveboard(pointB,Direction.East,q,True,200)
              
        return self.board


    def rotationB(self,pointA:Point,pointB:Point,pointC:Point,dir:str):
        # A - q - B
        # |
        # p
        # |
        # C
        #
        
        q = pointB[1] - pointA[1]
        p = abs(pointC[0] - pointA[0])
        if dir == "CW":
            self.moveboard(pointA,Direction.North,p,True,200)
            self.moveboard(pointA,Direction.West,q,True,200)
            self.moveboard(pointA,Direction.South,p,True,200)
            self.moveboard(pointA,Direction.East,q,True,200)
        elif dir == "CCW":
            self.moveboard(pointA,Direction.South,p,True,200)
            self.moveboard(pointA,Direction.West,q,True,200)
            self.moveboard(pointA,Direction.North,p,True,200)
            self.moveboard(pointA,Direction.East,q,True,200)

    def rotationC(self,pointA:Point,pointB:Point,pointC:Point,dir:str):
        # A - q - B
        #         |
        #         p
        #         |
        #         C
        #
        
        
        
        q = pointB[1]-pointA[1]
        p = pointC[0] - pointB[0]
        if dir == "CW":
            self.moveboard(pointA,Direction.East,q,True,200)
            self.moveboard(pointB,Direction.North,p,True,200)
            self.moveboard(pointA,Direction.West,q,True,200)
            self.moveboard(pointB,Direction.South,p,True,200)
        elif dir == "CCW":
            self.moveboard(pointB,Direction.North,p,True,200)
            self.moveboard(pointA,Direction.East,q,True,200)
            self.moveboard(pointB,Direction.South,p,True,200)
            self.moveboard(pointA,Direction.West,q,True,200)
    def rotationD(self,pointA:Point,pointB:Point,pointC:Point,dir:str):
        #       A
        #       |
        #       p
        #       |
        # B - q - C

        q = pointC[1] - pointB[1]
        p = pointB[0] - pointA[0]
        if dir == "CW":
            self.moveboard(pointA,Direction.South,p,True,200)
            self.moveboard(pointB,Direction.East,q,True,200)
            self.moveboard(pointA,Direction.North,p,True,200)
            self.moveboard(pointB,Direction.West,q,True,200)
        elif dir == "CCW":
            self.moveboard(pointB,Direction.East,q,True,200)
            self.moveboard(pointA,Direction.South,p,True,200)
            self.moveboard(pointB,Direction.West,q,True,200)
            self.moveboard(pointA,Direction.North,p,True,200)
    
    def tw(self,pointA:Point,pointB:Point,pointC:Point,dir:str):
        corner = [pointB[0]-1,pointB[1]]
        if dir == "W":
            self.rotationD(corner,pointA,pointB,"CW")
            self.rotationA(corner,pointB,pointC,"CW")
        elif dir == "E":
            self.rotationA(corner,pointB,pointC,"CCW")
            self.rotationD(corner,pointA,pointB,"CCW")

    def gameover(self):
        # If game over is true, draw game over
        text = self.font.render("Game Over", True, (255,255,255))
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.fill((0,0,0))
        self.screen.blit(text, [text_x, text_y])
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.display.quit()
        pygame.quit()
        sys.exit()


    def solve(self):
        for r in range(1,n*n+1-n,1):
            correctspot = [(r-1)//n,(r-1)%n]
            actualloc = np.where(self.board==r)
            actualloc = [actualloc[0][0],actualloc[1][0]]
            if correctspot == actualloc:
                print("same location")
                continue
            elif actualloc[1] > correctspot[1]:
                if actualloc[0] == correctspot[0]:
                    corner = [actualloc[0]+1,actualloc[1]]
                    print(f"rotating {r} into place case 1")
                    self.rotationC(correctspot,actualloc,corner,"CCW")
                elif actualloc[0] > correctspot[0]:
                    corner = [correctspot[0],actualloc[1]]
                    print(f"rotating {r} into place case 2")
                    self.rotationC(correctspot,corner,actualloc,"CW")
            elif actualloc[1]<correctspot[1]:
                if actualloc[0] > correctspot[0]:
                    print(f"rotating {r} into place case 3")
                    corner = [actualloc[0],correctspot[1]]
                    self.rotationD(correctspot,actualloc,corner,"CW")
            elif actualloc[1] == correctspot[1]:
                if actualloc[1]==n-1:
                    corner = [actualloc[0],actualloc[1]-1]
                    print(f"rotating {r} into place case 4")
                    self.rotationD(correctspot,corner,actualloc,"CCW")
                elif actualloc[1]>=0:
                    corner = [actualloc[0],actualloc[1]+1]
                    print(f"rotating {r} into place case 5")
                    self.rotationA(correctspot,actualloc,corner,"CW")

        for r in range(n*n-n+1,n*n-1,1):
            winstate = self.checkwin()
            if winstate:
                self.gameover()
            correctspot = [(r-1)//n,(r-1)%n]
            actualloc = np.where(self.board==r)
            actualloc = [actualloc[0][0],actualloc[1][0]]
            leftcorner = np.where(self.board==n*n-n+1)
            leftcorner = [leftcorner[0][0],leftcorner[1][0]]
            if correctspot == actualloc:
                print("same location")
                continue
            if actualloc[1] == correctspot[1]+1:

                print(f"moving {r} into place case 1")
                pointC = [correctspot[0],actualloc[1]+1]
                self.tw(correctspot,actualloc,pointC,"W")
            elif actualloc[1] - correctspot[1]>1:
                print(f"moving {r} into place case 2")
                pointC = [correctspot[0],correctspot[1]+1]
                self.tw(correctspot,pointC,actualloc,"E")

        winstate = self.checkwin()
        if winstate:
            self.gameover()
        # swap last two pieces
        for i in range(n-2,-2,-2):
            self.tw([n-1,i-1],[n-1,i],[n-1,i+1],"E")
        self.moveboard([n-1,0],Direction.West,1,True,1000)
        winstate = self.checkwin()
        if winstate:
            self.gameover()
    
    def rungame(self):
        running = True
        moved=False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.font = pygame.font.SysFont('arial',20)

        self.randomize()
        self.drawboard()
        pygame.display.update()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("solving")
                        self.solve()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    elemx,elemy = event.pos[0]//SQUARESIZE,event.pos[1]//SQUARESIZE

                if event.type == pygame.MOUSEBUTTONUP:
                    elem2x,elem2y = event.pos[0]//SQUARESIZE,event.pos[1]//SQUARESIZE

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
                    moved = deltax!=0 or deltay!=0
                if moved:

                    elem = elemy,elemx
                    self.moveboard(elem,direc,amount)
                    moved=False
                    self.drawboard()
                    pygame.display.update()

                state = self.checkwin()
                if state:
                    self.gameover()

    def randomize(self):
        direcs = list(Direction)
        for _ in range(100):
            randx = random.randint(0,n-1)
            randy = random.randint(0,n-1)
            direc = random.choice(direcs)
            amount = random.randint(1,n-1)
            elem = randx,randy
            self.moveboard(elem,direc,amount)
        
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

    def moveboard(self,elem:Point,direc:Direction,amount:int,draw:bool=False,delay:int=0):
        x,y = elem
        amount = abs(amount)
        if direc == Direction.North:
            self.board[:,y] = np.roll(self.board[:,y],-amount)
        if direc == Direction.South:
            self.board[:,y] = np.roll(self.board[:,y],amount)
        if direc == Direction.West:
            self.board[x,:] = np.roll(self.board[x,:],-amount)
        if direc == Direction.East:
            self.board[x,:] = np.roll(self.board[x,:],amount)
        if draw:
            self.drawboard()
            pygame.display.update()
            if delay>0:
                pygame.time.wait(delay)

if __name__ == "__main__":

    game = SlidingGame(board)
    game.rungame()
