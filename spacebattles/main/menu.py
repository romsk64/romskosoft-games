import pygame
from random import randint
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from libs import romplog

sys.path.remove(parent_dir) # конец