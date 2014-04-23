# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:26:32 2014

@author: pruvolo
"""

import pygame

class View:
    """ Encodes a view of the BrickBreaker game in a PyGame window """
    
    def __init__(self, screen, model):
        """ Constructs a PyGameWindowView object
            screen: the window to draw the game to
            model: the Brick Breaker game state """
        self.screen = screen
        self.model = model
        
    def draw(self):
        """ Draws the game state to the PyGame window """
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, brick.color, pygame.Rect(brick.x,brick.y,brick.width,brick.height))
        pygame.draw.rect(self.screen, pygame.Color(255,255,255), pygame.Rect(self.model.paddle.x,self.model.paddle.y,self.model.paddle.width,self.model.paddle.height))
        pygame.draw.ellipse(self.screen, pygame.Color(128,128,128),(self.model.ball.x-self.model.ball.r, self.model.ball.y-self.model.ball.r, 2*self.model.ball.r,2*self.model.ball.r))
        pygame.display.update()