# Romsk Python Graphic Library v1.1
# Распространяется по лицензии MIT
# Русская документация по пути ../docs/ru-doc.md

import pygame
import time
import logging
from datetime import date
from random import randint

# wid - ширина
# hid - длина

C_RED = (255, 0, 0)
C_GREEN = (0, 255, 51)
C_YELLOW = (255, 255, 0)
C_BLUE = (0, 0, 100)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_LIGHT_GRAY = (211, 211, 211)
C_DARK_GRAY = (100, 100, 100)
C_GRAY = (128, 128, 128)

pygame.init()

# logging.basicConfig(level=logging.INFO, filename=f"base_log_{date.today()}.log",filemode="w",
#                     format="%(asctime)s %(levelname)s %(message)s")

def log(func):
    def outputLog(**kwargs):
        if func == 0:
            logging.log(20, f"[{__name__}]: функция работает в порядке.")
        elif func == 1:
            logging.log(40, f"[{__name__}]: получена ошибка! Текст: {kwargs.get('error')}.")
        elif func == 2:
            logging.log(30, f"[{__name__}]: предупреждение: {kwargs.get('warning')}")
        elif func == 3:
            pass
        elif func == 4:
            logging.log(50, f"[{__name__}]: КРИТИЧЕСКАЯ ОШИБКА! Текст: {kwargs.get('error')}")
    return outputLog

class Area:
    def __init__(self, window, x, y, wid, hid, contour, colArea, colContour = (0, 0, 0), hidContour = 0): # window -- где будет расположен квадрат
        self.window = window
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid
        self.contour = contour
        self.colArea = colArea
        self.colContour = colContour
        self.hidContour = hidContour
    def drawAreaRect(self): 
        if self.contour == True:
            rectContour = pygame.Rect(self.x - (self.hidContour / 2), self.y - (self.hidContour / 2), self.wid + self.hidContour, self.hid + self.hidContour)
            pygame.draw.rect(self.window, (self.colContour), rectContour)
        # верх
        rectArea = pygame.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.window, (self.colArea), rectArea)
        self.rectArea = rectArea #если нужен будет collide
    def drawAreaRectTextured(self, texture):
        rectArea = pygame.Surface((self.wid, self.hid), pygame.SRCALPHA) #SRCALPHA это поверхность с альфа-каналом
        if self.contour == True:
            pass #пока
        elif self.contour == False:
            self.window.blit(rectArea, (self.x, self.y))
            rectArea.set_alpha(0)
    def colChange(self, type_col, color): # type_col -- "1" - area, "2" - contour
        if type_col == 1:
            self.colArea = color
            self.drawAreaRect()
        elif type_col == 2:
            self.colContour = color
            self.drawAreaRect()

class TextArea(Area):
    def __init__(self, text, font, fsize, colText, textOts, textOtsX = 0, textOtsY = 0): 
        Area().__init__()        # textOts:
        self.text = text         # "0" - слева в середине по Y
        self.font = font         # "1" - справа в середине по Y
        self.fsize = fsize       # "2" - в середине по X и по Y
        self.colText = colText   # "3" - только textOtsX и textOtsY
        self.textOts = textOts
        self.textOtsX = textOtsX
        self.textOtsY = textOtsY
    def drawText(self):
        txt = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
        self.window.blit(txt, (self.x + self.textOtsX, self.y + self.textOtsY))

class Text():
    def __init__(self, text, font, fsize, colText, textX, textY, win):
        self.text = text
        self.font = font
        self.fsize = fsize
        self.colText = colText
        self.textX = textX
        self.textY = textY
        self.win = win # окно типа виндоу
    def drText(self):
        txt = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
        self.win.blit(txt, (self.textX, self.textY))

class TexturedArea():
    def __init__(self, x, y, wid, hid):
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid

class ConturedTexturedArea(TexturedArea):
    def __init__(self, x, y):
        super.__init__(TexturedArea)
        self.x = x
        self.y = y

class TexturedSprite():
    def __init__(self, x, y, wid, hid, type):
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid
        
        if type == 1 or type == "Square":
            self.type = 1 # 1 - квадрат

class Textured3DSprite():
    def __init__(self, x, y, z, wid, wid_2, hid):
        self.x = x
        self.y = y
        self.z = z
        self.wid = wid
        self.wid_2 = wid_2
        self.hid = hid
class Button():
    def __init__(self, window, x: float, y: float, wid: float, hid: float, hidContour: float, function: function, text: str, font, fsize: int, colText: tuple, textOts: int, textOtsX: float = 0, textOtsY: float = 0, colArea: tuple = (128, 128, 128), colContour: tuple = (255, 255, 255), colContourDown: tuple = (0, 0, 0)):
        self.window = window # где расположена кнопка (поверхность)
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid
        self.colArea = colArea
        self.colContour = colContour
        self.colContourDown = colContourDown
        self.hidContour = hidContour
        self.function = function # функция бодет выполнятся при нажатии на кнопку
        self.text = text
        self.font = font
        self.fsize = fsize
        self.colText = colText
        self.textOts = textOts
        self.textOtsX = textOtsX
        self.textOtsY = textOtsY
    def drawButton(self, textTrue: bool):
        # белый строк (контур)
        rectContour_1 = pygame.Rect(self.x - (self.hidContour / 2), self.y - (self.hidContour / 2), self.wid + self.hidContour, self.hid + self.hidContour)
        pygame.draw.rect(self.window, (self.colContour), rectContour_1)
        # черный строк (контур)
        rectContour_2 = pygame.Rect(self.x, self.y, self.wid + self.hidContour, self.hid + self.hidContour)
        pygame.draw.rect(self.window, (self.colContourDown), rectContour_2)
        # верх
        rectArea = pygame.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.window, (self.colArea), rectArea)
        self.rectArea = rectArea
        # текст
        if textTrue == True:
            if self.textOts == 0: # слева
                textLol = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
                self.window.blit(textLol, (self.x, self.y + (self.hid / 2)))
            elif self.textOts == 1: # справа
                textLol = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
                self.window.blit(textLol, (self.x + self.wid, self.y + (self.hid / 2)))
            elif self.textOts == 2: # по центру
                textLol = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
                self.window.blit(textLol, (self.x + (self.wid / 2), self.y + (self.hid / 2)))
            elif self.textOts == 3: # по textOts
                textLol = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
                self.window.blit(textLol, (self.x + self.textOtsX, self.y + self.textOtsY))
    def effectNav(self): #эффект наведения
        pass
    # еще сделать при наведении выделение
    def execFunc(self, x, y, args): # осуществление функции (Execute Function) 
        # self.rectArea.collidepoint(x, y) -- это из pygame.mouse.get_pos()
        if (self.rectArea.collidepoint(x, y)) == True:
            self.function(args) # а аргументы пусть сами дописывают сюда (или я сделаю потом такую фишку)
            # logging.info("вроде работает")
    # пока так, потому что пока совместимости нет
    def drawBtn(self):
        down_rect = pygame.rect.Rect(self.x, self.y, self.wid + 5, self.hid + 5)
        pygame.draw.rect(self.window, self.colContour, down_rect)

        rect = pygame.rect.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.window, self.colArea, rect)

        self.rect = rect
    def collPoint(self, x: float, y: float):
        return self.rect.collidepoint(x, y)

class LiteButton(): # временно
    def __init__(self, x: int, y: int, wid: float, hid: float, win, col: tuple = C_LIGHT_GRAY, cnt_col: tuple = C_DARK_GRAY):
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid
        self.win = win #тоже окно
        self.col = col
        self.cnt_col = cnt_col
    def drawBtn(self):
        down_rect = pygame.rect.Rect(self.x, self.y, self.wid + 5, self.hid + 5)
        pygame.draw.rect(self.win, self.cnt_col, down_rect)

        rect = pygame.rect.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.win, self.col, rect)

        self.rect = rect
    def collPoint(self, x: float, y: float):
        return self.rect.collidepoint(x, y)