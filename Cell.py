# -*- coding: utf-8 -*-

import Position
import MyPygame
import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, position: Position.Position, pygame_object: MyPygame.Pygame = None, is_entrance=False, is_exit=False):
        if pygame_object is not None:
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((32, 32))
            self.image.convert()
            self.image.fill((250, 250, 250))
        self.position = position
        self.item = None
        self.is_entrance = is_entrance
        self.is_exit = is_exit

    def __eq__(self, other_cell):
        if self.position == other_cell.position:
            return True

        return False

    def __hash__(self):
        return hash(self.position)
