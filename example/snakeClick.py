#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:39:28 2018

@author: sam0225
"""

from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import time, random



class Snake:
    def __init__(self, mc, startVec3, playingBottomLeft, playingTopRight):
        self.mc = mc
        self.direction = "up"
        self.lenght = 5
        self.tail = []
        self.tail.insert(0, startVec3)
        self.playingBottomLeft = playingBottomLeft
        self.playingTopRight = playingTopRight
        self.createApple()
        self.score = 0
        
    def draw(self):
        for segment in self.tail:
            self.mc.setBlock(segment.x, segment.y, segment.z, 57)
            
    def addSegment(self, segment):
        self.mc.setBlock(segment.x, segment.y, segment.z, 57)
        self.tail.insert(0, segment)
        #do I need to clear the last segment
        if (len(self.tail) > self.lenght):
            lastSegment = self.tail[len(self.tail)-1]
            self.mc.setBlock(lastSegment.x, lastSegment.y, lastSegment.z, 0)
            #pop the last segment off the tail
            self.tail.pop()


    def move(self):
            newSegment = Vec3(self.tail[0].x, self.tail[0].y, self.tail[0].z)
            if self.direction == "up":
                newSegment.y = newSegment.y + 1
            elif self.direction == "down":
                newSegment.y = newSegment.y - 1
            elif self.direction == "left":
                newSegment.x = newSegment.x - 1
            elif self.direction == "right":
                newSegment.x = newSegment.x + 1
            #sleep otherwise the snake moves WAY too fast, 可以改成關卡制，難度
            time.sleep(0.3)
            if (self.checkCollision(newSegment) == False):
                self.addSegment(newSegment)
                #have I eaten the apple?
                if (matchVec3(newSegment, self.apple) == True): 
                    #increase my lenght
                    self.lenght = self.lenght + 2
                    #increase my score
                    self.score = self.score + 10
                    #create a new apple
                    self.createApple()
                return True
            else:
                #game over
                #flash snake head
                mc.setBlock(self.tail[0].x, self.tail[0].y, self.tail[0].z, 0)
                time.sleep(0.3)
                mc.setBlock(self.tail[0].x, self.tail[0].y, self.tail[0].z, 57)
                time.sleep(0.3)
                mc.setBlock(self.tail[0].x, self.tail[0].y, self.tail[0].z, 0)
                time.sleep(0.3)
                mc.setBlock(self.tail[0].x, self.tail[0].y, self.tail[0].z, 57)
                time.sleep(0.3)
                #show score
                mc.postToChat("Game over  得分: " + str(self.score)+"分")
                time.sleep(7)
                
                return False

    def checkCollision(self, newSegment):
        #am I going the boundary
        if ((newSegment.x == playingBottomLeft.x) or (newSegment.y == playingBottomLeft.y) or (newSegment.x == playingTopRight.x) or (newSegment.y == playingTopRight.y)):
            return True
        else:
            #or my own tail
            hitTail = False
            for segment in self.tail:
                if (matchVec3(segment, newSegment) == True):
                    hitTail = True
            return hitTail
        
    def changeDirection(self, newDirection):
        #code to make sure user doesnt try and make the snake move back on itself
        if (newDirection == "up"):
            if (self.direction != "down"): self.direction = newDirection
        elif (newDirection == "down"):
            if (self.direction != "up"): self.direction = newDirection
        elif (newDirection == "left"):
            if (self.direction != "right"): self.direction = newDirection
        elif (newDirection == "right"):
            if (self.direction != "left"): self.direction = newDirection

    def createApple(self):
        badApple = True
        #loop until an apple is created which doesnt collide with the boundary or the snake
        while (badApple == True):
            x = random.randrange(playingBottomLeft.x, playingTopRight.x)
            y = random.randrange(playingBottomLeft.y, playingTopRight.y)
            z = playingBottomLeft.z
            newApple = Vec3(x, y, z)
            badApple = self.checkCollision(newApple)
        self.apple = newApple
        self.mc.setBlock(self.apple.x, self.apple.y, self.apple.z, 213)

        
        
def matchVec3(vec1, vec2):
    if ((vec1.x == vec2.x) and (vec1.y == vec2.y) and (vec1.z == vec2.z)):
        return True
    else:
        return False

#draws a vertical outline
def drawVerticalOutline(mc, x0, y0, x1, y1, z, blockType, blockData=0):
    mc.setBlocks(x0, y0, z, x0, y1, z, blockType, blockData)
    mc.setBlocks(x0, y1, z, x1, y1, z, blockType, blockData)
    mc.setBlocks(x1, y1, z, x1, y0, z, blockType, blockData)
    mc.setBlocks(x1, y0, z, x0, y0, z, blockType, blockData)


if __name__ == "__main__":
    
    mc = Minecraft.create()
    mc.postToChat("Hello, 麥塊貪食蛇, CodingAPE猿創力程式設計學校")
    pos = mc.player.getTilePos()
    
    while True:
        #constants
        screenBottomLeft = Vec3(pos.x-10, pos.y+4, pos.z+25)
        screenTopRight = Vec3(pos.x+10,pos.y+24,pos.z+25)
        playingBottomLeft = Vec3(pos.x-10, pos.y+4, pos.z+24)
        playingTopRight = Vec3(pos.x+10, pos.y+24, pos.z+24)
        snakeStart = Vec3(pos.x, pos.y+5, pos.z+24)
        
        
        #Build game board
        # clear a suitably large area
        mc.setBlocks(pos.x-10, pos.y, pos.z-5, pos.x+10, pos.y+25, pos.z+26, 0)
        # create playing board
        mc.setBlocks(screenBottomLeft.x, screenBottomLeft.y, screenBottomLeft.z, screenTopRight.x, screenTopRight.y, screenTopRight.z, 1)
        drawVerticalOutline(mc, playingBottomLeft.x, playingBottomLeft.y, playingTopRight.x, playingTopRight.y, playingTopRight.z, 49)
        
        mc.setBlock(pos.x, pos.y+1, pos.z+1, 13)
        mc.setBlock(pos.x, pos.y, pos.z+1, 14)
        mc.setBlock(pos.x-1, pos.y, pos.z+1, 15)
        mc.setBlock(pos.x+1, pos.y, pos.z+1, 16)
        
        """另一種基座
        mc.setBlock(pos.x, pos.y-1, pos.z+1, 57)
        mc.setBlock(pos.x, pos.y-1, pos.z-1, 57)
        mc.setBlock(pos.x-1, pos.y-1, pos.z, 57)
        mc.setBlock(pos.x+1, pos.y-1, pos.z, 57)
        
        mc.setBlocks(pos.x-2, pos.y+1, pos.z-2,pos.x+2, pos.y, pos.z+2, 20)
        mc.setBlocks(pos.x-1, pos.y+1, pos.z-1,pos.x+1, pos.y, pos.z+1, 0)
        
        # blocks around control buttons, to stop player moving off buttons
        mc.setBlock(pos.x + 2,pos.y + 1,pos.z, 20)
        mc.setBlock(pos.x - 2,pos.y + 1,pos.z, 20)
        mc.setBlock(pos.x,pos.y + 1,pos.z + 2, 20)
        mc.setBlock(pos.x,pos.y + 1,pos.z - 2, 20)
        mc.setBlock(pos.x - 1,pos.y + 1,pos.z - 1, 20)
        mc.setBlock(pos.x - 1,pos.y + 1,pos.z + 1, 20)
        mc.setBlock(pos.x + 1,pos.y + 1,pos.z + 1, 20)
        mc.setBlock(pos.x + 1,pos.y + 1,pos.z - 1, 20)
        """
        mc.setBlocks(pos.x-1,pos.y - 1,pos.z-2,pos.x+1,pos.y,pos.z,  0)
        # put player in the middle of the control
        mc.player.setPos(pos.x + 0.5,pos.y,pos.z + 0,5)
        
        #time for minecraft to catchup
        time.sleep(3)

    
    
        mc.postToChat("前後左右移動去控制蛇蛇")
        time.sleep(3)
        #create snake
        snake = Snake(mc, snakeStart, playingBottomLeft, playingTopRight)
        snake.draw()
        
        playing = True
        
        try:
            #loop until game over
            while playing == True:
                
                hits = mc.events.pollBlockHits()
                if len(hits)>0:
                    hit = hits[0]
                    block = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
                    if block==13: snake.changeDirection("up")
                    elif block==14: snake.changeDirection("down")
                    elif block==15: snake.changeDirection("left")
                    elif block==16: snake.changeDirection("right")
                """
                #get players position - are they on a control tile, if so change snake's direction
                Pos = mc.player.getTilePos()
                Pos.y = Pos.y - 1
                if matchVec3(Pos, Vec3(pos.x, pos.y-1, pos.z+1)) == True: snake.changeDirection("up")
                elif matchVec3(Pos, Vec3(pos.x, pos.y-1, pos.z-1)) == True: snake.changeDirection("down")
                elif matchVec3(Pos, Vec3(pos.x-1, pos.y-1, pos.z)) == True: snake.changeDirection("left")
                elif matchVec3(Pos, Vec3(pos.x+1, pos.y-1, pos.z))== True: snake.changeDirection("right")
                """
                #move the snake
                playing = snake.move()
        except KeyboardInterrupt:
            print("stopped")
