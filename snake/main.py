import pygame
from random import randint

pygame.init()
bg = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Minesweeper")

_cycle_ = True
_game_ = False
_gameover_ = False
_gamewin_ = False
_quit_ = False
_quitgame_ = False
_gametype_ = 0
pg_timer = pygame.time.Clock()
mine_kol = 0
mined_kol = 0
kl_list = []
gui_list = []
menu_btns = []
menu_btns_text = []
kl_wid, kl_hid = 20, 20
menu_btn_wid, menu_btn_hid = 177, 25
bg_wid, bg_hid = 500, 500

C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_LIGHT_GRAY = (162, 162, 162)
C_DARK_GRAY = (100, 100, 100)
C_DARK_BLUE = (0, 0, 255)
C_LIGHT_BLUE = (50, 50, 200)
C_LIDARK_BLUE = (0, 0, 150) # LIGHT-DARK BLUE
C_RED = (255, 0, 0)

class Text():
    def __init__(self, x: int, y, text, font, fsize, txt_col, win):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.fsize = fsize
        self.txt_col = txt_col
        self.win = win #и это окно
    def drawText(self, _bold_ = False, _italic_ = False):
        text_ = pygame.font.SysFont(self.font, self.fsize, bold = _bold_, italic = _italic_)
        text = text_.render(self.text, 1, self.txt_col)
        self.win.blit(text, (self.x, self.y))

class Kletka():
    def __init__(self, x: int, y, wid: float, hid: float, win, col: tuple = C_LIGHT_GRAY, cnt_col: tuple = C_BLACK): # если что-то будет
        self.x = x                                                                                              # с флоатом в hid и wid
        self.y = y                                                                                              # сделать int
        self.wid = wid                                                                                          # в других классах тоже
        self.hid = hid
        self.win = win
        self.col = col #window - окно
        self.cnt_col = cnt_col

        self.open = False
        self.mined = False
        self.mines = 0
        self.mine = False
    def drawKl(self):
        down_rect = pygame.rect.Rect(self.x, self.y, self.wid + 2, self.hid + 2)
        pygame.draw.rect(self.win, self.cnt_col, down_rect)

        rect = pygame.rect.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.win, self.col, rect)

        self.rect = rect
    def drawOpenKl(self):
        self.col = C_DARK_GRAY
        self.cnt_col = C_LIGHT_GRAY

        down_rect = pygame.rect.Rect(self.x, self.y, self.wid + 2, self.hid + 2)
        pygame.draw.rect(self.win, self.cnt_col, down_rect)

        rect = pygame.rect.Rect(self.x, self.y, self.wid, self.hid)
        pygame.draw.rect(self.win, self.col, rect)

        if self.mines > 0:
            self.drawText(True)
        else:
            pass

        self.rect = rect
    def mine_otr_flag(self): # флаг
        pass
    def openMine(self): # отрисовка мин при проигрыше
        pass
    def collPoint(self, x: float, y: float):
        return self.rect.collidepoint(x, y)
    
class Btn():
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

class Apple():
    def __init__(self, ):
        pass

class Snake():
    def __init__(self): # сделать другие названия
        self.kletka = kl_list[4][4] # клетка спавна
        self.storona = 3 # сторона поворота
        """стороны:""""""""""""
        "   вверх - 1         "
        "   лево - 2          "
        "   право - 3         "
        "   вниз - 4          "
        """""""""""""""""""""""
        self.apples = 3 # съеденные яблоки/клетки змеи