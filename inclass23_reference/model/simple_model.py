# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:34:24 2014

@author: pruvolo
"""

import pygame
import random

class Model:
    """ Encodes the game state for the Brick Breaker game """
    BRICK_SIZE = (94,20)
    BRICK_GAPS = (10,10)
    BALL_RADIUS = 10
    
    def __init__(self,size):
        """ Constructs a new Model object """
        self.bricks = []
        self.size = size
        for x in range(self.BRICK_GAPS[0],self.size[0]-(self.BRICK_SIZE[0]+self.BRICK_GAPS[0]),self.BRICK_SIZE[0]+self.BRICK_GAPS[0]):
            for y in range(self.BRICK_GAPS[1],int(self.size[1]/2.0),self.BRICK_SIZE[1]+self.BRICK_GAPS[1]):
                brick_color = pygame.Color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
                new_brick = Brick(x,y,self.BRICK_SIZE[0],self.BRICK_SIZE[1],brick_color)
                self.bricks.append(new_brick)
        self.paddle = Paddle(self.size[0]/2.0,self.size[1]-40.0,100,20)
        self.ball = Ball(self.paddle.x+self.paddle.width/2.0,self.paddle.y - (self.BALL_RADIUS+10),self.BALL_RADIUS,0.0,-1.0)

    def update(self):
        self.paddle.update()
        self.ball.update()
        # detect collisions here TODO

    def change_paddle_velocity(self,acceleration):
        self.paddle.velocity_x += acceleration

class Ball:
    """ Encodes the state of the ball in the Brick Breaker game """
    def __init__(self,x,y,r,vx,vy):
        """ Constructs a Ball object
            x: x-coordinate of the center of the ball
            y: y-coordinate of the center of the ball
            r: the radius of the ball """
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
    
    def update(self):
        """ Update the ball state """
        self.x += self.vx
        self.y += self.vy

class Brick:
    """ Encodes the state of a brick """
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def update(self):
        """ Update Brick state """
        pass
    
class Paddle:
    """ encodes the state of the paddle (player) """
    def __init__(self,x,y,width,height):
        """ Constructor for Paddle class
            x: the x-coordinate of the left side of the paddle
            y: the y-coordinate of the top side of the paddle
            width: the width of the paddle
            height: the height of the paddle """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x = 0.0
    
    def update(self):
        """ update the state of the Paddle """
        self.x += self.velocity_x
        if self.x < 0 or self.x + self.width > 640:
            self.velocity_x = 0
