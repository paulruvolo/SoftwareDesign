# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:32:27 2014

@author: pruvolo
"""

import pygame
from controller import *
from view import *
from model import *
from pygame.locals import *
import time

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = simple_model.Model(size)
    view = pygame_window_view.View(screen, model)
    controller = mouse_controller.Controller(model)
    #controller = keyboard_controller.Controller(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)

        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()