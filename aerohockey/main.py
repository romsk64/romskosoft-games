import pygame
import socket
from add import *

# настройки
setting_display_size = (1920, 1000)

pygame.init()
bg = pygame.display.set_mode(setting_display_size)
pygame.display.set_caption("Aero Hockey")

class Button:
    def __init__(self, x, y, wid, hid):
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid
    def drawButton(self):
        down_rect = pygame.rect.Rect(self.x, self.y, self.wid + 5, self.hid + 5)
        pygame.draw.rect(self.win, self.cnt_col, down_rect)

        rect = pygame.rect.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.win, self.col, rect)

        self.rect = rect
    def drawTexture(self):
        pass

    def collPoint(self, x, y):
        return self.rect.collidepoint(x, y)