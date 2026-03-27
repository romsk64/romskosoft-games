import pygame
import socket
from add import *

# настройки
setting_display_size = (1920, 1000)

pygame.init()
bg = pygame.display.set_mode(setting_display_size)
pygame.display.set_caption("Aero Hockey")