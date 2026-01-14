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

class Kletka(Text):
    def __init__(self, x: int, y, wid: float, hid: float, win, col: tuple = C_LIGHT_GRAY, cnt_col: tuple = C_BLACK): # если что-то будет
        super().__init__(font = "Arial", fsize = 12, txt_col = C_BLACK, x = x, y = y, text = None, win = win) # с флоатом в hid и wid
        self.x = x                                                                                              # сделать int
        self.y = y                                                                                              # в других классах тоже
        self.wid = wid
        self.hid = hid
        self.win = win #window - окно
        self.col = col
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
    def collPoint(self, x, y):
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
    def collPoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Smile():
    def __init__(self, x: int, y: int, win):
        self.x = x
        self.y = y
        self.win = win
    def draw(self):
        for i in range(6):
            pygame.draw.rect(self.win, C_BLACK, pygame.rect.Rect(self.x - 2 + i, self.y - 6, 1, 1)) # черный пиксель самый верх
            pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x - 2 + i, self.y - 5, 1, 1)) # желтый пиксель самый верх
        for i2 in range(2):
            for j in range(2):
                pygame.draw.rect(self.win, C_BLACK, pygame.rect.Rect(self.x - 4 + (i2 * 6) + j, self.y - 5, 1, 1)) # по 2 черных пикселя чуть ниже верха
        for i3 in range(10):
            pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x - 4 + i3, self.y - 4, 1, 1)) # ряд из 10 желтых пикселей
        for i4 in range(2):
            pygame.draw.rect(self.win, C_BLACK, pygame.rect.Rect(self.x - 5 + (i4 * 10), self.y - 4, 1, 1)) # 2 черных пикселя по краям ряда выше
        for i5 in range(12):
            pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x - 5 + i5, self.y - 3, 1, 1)) # ряд из 12 желтых пикселей
        for i6 in range(2):
            for j2 in range(2):
                pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x - 4 + (i6 * 8) + j2, self.y - 2, 1, 1)) # по 2 желтых писеля с краев
        for i7 in range(2):
            for j3 in range(3):
                pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x - 5 + (i7 * 8) + j3, self.y - 1, 1, 1)) # по 3 жельых пикселя с краев
        for i8 in range(2):
            for j4 in range(2):
                for x in range(2):
                    pygame.draw.rect(self.win, C_BLACK, pygame.rect.Rect(self.x - 2 + x + (i8 * 4), self.y - 2 + j4, 1, 1)) # глаза
        for i9 in range(2):
            for j5 in range(2):
                pygame.draw.rect(self.win, C_BLACK, pygame.rect.Rect(self.x - 5 + (i9 * 12), self.y - 3 + j5, 1, 1)) # 2 черных пикселя с краев
        for i10 in range(2): # 14
            for j6 in range(4): # 6
                pygame.draw.rect(self.win, C_BLACK, pygame.rect.Rect(self.x - 6 + (i10 * 14), self.y - 1 + j6, 1, 1)) # 4 черных пикселя по краям
        for i11 in range(3): # -5
            for j7 in range(13): # 14
                pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x - 5 + j7, self.y + i11, 1, 1)) # желтые пиксели в середине лица
        for i12 in range(2):
            for j8 in range(2):
                pygame.draw.rect(self.win, C_YELLOW, pygame.rect.Rect(self.x + j8, self.y - 2 + i12, 1, 1)) # между глазами

def mines(min_kol, max_x, max_y):
    all_mines = []
    for _ in range(min_kol):
        all_mines.append([randint(0, max_x - 1), randint(0, max_y)]) #возможно поменяю потом
    return all_mines
def drawAll_1():
    global mine_kol
    mine_kol = 10
    global kl_list
    kl_list.clear()
    for _ in range(9):
        kl_list.append(list()) # 9 списков, корды
    """
    for i in range(9):                  --- Планирование строк
        for j in range(9):              --- Отрисовка всех 9 столбиков в строке
            kl_list[i].append(Kletka()) --- В kl_list засунуть клетку
            kl_list[i][j].drawKl()      --- Отрисовать клетку
    """
    for i in range(9):
        for j in range(9):
            kl_list[i].append(Kletka(5 + j * kl_wid + j, 50 + (kl_hid * i) + (2 * i), kl_wid, kl_hid, bg))
            kl_list[i][j].drawKl()

    time_timer_otr_btn.drawBtn()
    mine_kol_otr_btn.drawBtn()
    smile_otr_btn.drawBtn()
    time_timer_otr.drawText()
    mine_kol_otr.drawText()
    smile_otr.draw()
def drawAll_1_list():
    global kl_list
    for i in range(9):
        for j in range(9):
            kl_list[i][j].drawKl()

def drawAll_2():
    global mine_kol
    mine_kol = 40
    global kl_list
    kl_list.clear()
    for _ in range(16):
        kl_list.append(list()) # 16 списков, корды
    for i in range(16):
        for j in range(16):
            kl_list[i].append(Kletka(5 + j * kl_wid + j, 50 + (kl_hid * i) + (2 * i), kl_wid, kl_hid, bg))
            kl_list[i][j].drawKl()
def drawAll_2_list():
    global kl_list
    for i in range(16):
        for j in range(16):
            kl_list[i][j].drawKl()

def drawAll_3(): # пока так
    global mine_kol
    mine_kol = 99
    global kl_list
    kl_list.clear()
    for _ in range(9):
        kl_list.append(list())
    for i in range(9):
        for j in range(9):
            kl_list[i].append(Kletka(5 + j * kl_wid + j, 50 + (kl_hid * i) + (2 * i), kl_wid, kl_hid, bg))
            kl_list[i][j].drawKl()
def drawAll_3_list():
    global kl_list
    for i in range(9):
        for j in range(9):
            kl_list[i][j].drawKl()

def drawAll_3_1(): # тут тоже пока
    global kl_list # профи в 9:16
    kl_list.clear()
    for _ in range(9):
        kl_list.append(list())
    for i in range(9):
        for j in range(9):
            kl_list[i].append(Kletka(5 + j * kl_wid + j, 50 + (kl_hid * i) + (2 * i), kl_wid, kl_hid, bg))
            kl_list[i][j].drawKl()
def drawAll_3_1_list():
    global kl_list
    for i in range(9):
        for j in range(9):
            kl_list[i][j].drawKl()

def drawAll_4(user_x, user_y): # пользовательский
    pass
def drawAll_4_list():
    global kl_list
    for i in kl_list:
        for j in kl_list[i]:
            kl_list[i][j].drawKl()

def autoOpening(e, pl_e): #автооткрытие пустых клеток
    kl_list[e - 1][pl_e - 1].open = True
    kl_list[e - 1][pl_e].open = True
    kl_list[e - 1][pl_e + 1].open = True
    kl_list[e][pl_e - 1].open = True
    kl_list[e][pl_e + 1].open = True
    kl_list[e + 1][pl_e - 1].open = True
    kl_list[e + 1][pl_e].open = True
    kl_list[e + 1][pl_e + 1].open = True

def drawGameGUI():
    time_timer_otr_btn.drawBtn()
    mine_kol_otr_btn.drawBtn()
    smile_otr_btn.drawBtn()
    time_timer_otr.drawText()
    mine_kol_otr.drawText()
    smile_otr.draw()

def menu_btn_draw(): # потом
    global menu_btns
    global menu_btns_text
    for i in range(6):
        menu_btns[i].drawBtn()
    for j in range(7):
        menu_btns_text[j].drawText()

bg.fill((200, 200, 200))
name = Text(10, 10, "romsk64's minesweeper", "Arial", 24, C_BLACK, bg)
menu_btns_text.append(name)

btn_1 = Btn(10, 50, menu_btn_wid, menu_btn_hid, bg)
btn_1_text = Text(10, 52, "[1] Новичок (9x9)", "Times New Roman", 16, C_BLACK, bg)
menu_btns.append(btn_1)
menu_btns_text.append(btn_1_text)

btn_2 = Btn(10, 85, menu_btn_wid, menu_btn_hid, bg)
btn_2_text = Text(10, 87, "[2] Любитель (16x16)", "Times New Roman", 16, C_BLACK, bg)
menu_btns.append(btn_2)
menu_btns_text.append(btn_2_text)

btn_3 = Btn(10, 120, menu_btn_wid, menu_btn_hid, bg)
btn_3_text = Text(10, 122, "[3] Профессионал (30x16)", "Times New Roman", 16, C_BLACK, bg)
menu_btns.append(btn_3)
menu_btns_text.append(btn_3_text)

btn_4 = Btn(10, 155, menu_btn_wid, menu_btn_hid, bg)
btn_4_text = Text(10, 157, "[4] Пользовательский", "Times New Roman", 16, C_BLACK, bg)
menu_btns.append(btn_4)
menu_btns_text.append(btn_4_text)

btn_5 = Btn(10, 225, menu_btn_wid, menu_btn_hid, bg)
btn_5_text = Text(10, 227, "[5] Настройки", "Times New Roman", 16, C_BLACK, bg)
menu_btns.append(btn_5)
menu_btns_text.append(btn_5_text)

btn_6 = Btn(10, 260, menu_btn_wid, menu_btn_hid, bg)
btn_6_text = Text(10, 262, "[ESC] Выход", "Times New Roman", 16, C_BLACK, bg)
menu_btns.append(btn_6)
menu_btns_text.append(btn_6_text)

menu_btn_draw()

time_timer = 0 #ну типа тайм
time_timer_otr = Text(5, 7, f"{time_timer}", "Arial", 16, C_BLACK, bg) # корды для новичка
time_timer_otr_btn = Btn(5, 5, 30, 20, bg)
mine_kol_otr = Text(160, 7, f"{mine_kol}", "Arial", 16, C_BLACK, bg) # корды для новичка
mine_kol_otr_btn = Btn(160, 5, 30, 20, bg)
smile_otr = Smile(102, 17, bg) # смайл
smile_otr_btn = Btn(90, 5, 25, 25, bg)

while _cycle_:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            _cycle_ = False
        elif event.type == pygame.KEYDOWN:
            if _game_ != True:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    all_mines = mines(10, 9, 9)
                    print(all_mines)

                    bg_wid, bg_hid = 200, 255
                    bg = pygame.display.set_mode((bg_wid, bg_hid))
                    pygame.display.set_caption("Новичок")
                    bg.fill((200, 200, 200))
                    mine_kol = 10

                    drawAll_1()
                    _game_ = True
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    all_mines = mines(40, 16, 16)
                    print(all_mines)

                    bg_wid, bg_hid = 350, 420
                    bg = pygame.display.set_mode((bg_wid, bg_hid))
                    pygame.display.set_caption("Любитель")
                    bg.fill((200, 200, 200))

                    drawAll_2()
                    _game_ = True
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    pass
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    pass
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    pass
                elif event.key == pygame.K_6 or event.key == pygame.K_ESCAPE or event.key == pygame.K_KP6:
                    pygame.quit()
                    _cycle_ = False
            elif _game_ == True:
                if event.key == pygame.K_q:
                    bg.fill((200, 200, 200))
                    drawAll_1_list()
                    pygame.display.update()

                    _quitgame_ = True
                    if _gametype_ == 1:
                        choise = Text(50, 100, "Выйти в главное меню?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    elif _gametype_ == 2:
                        choise = Text(50, 100, "Выйти в главное меню?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    elif _gametype_ == 3:
                        choise = Text(50, 100, "Выйти в главное меню?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    elif _gametype_ == 4: # надо поработать над пользовательским режимом
                        choise = Text(50, 100, "Выйти в главное меню?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    choise.drawText(True)
                    choise_pl.drawText(True)
                    pygame.display.update()
                elif event.key == pygame.K_ESCAPE:
                    bg.fill((200, 200, 200))
                    drawAll_1_list()
                    pygame.display.update()

                    _quit_ = True
                    if _gametype_ == 1:
                        choise = Text(50, 100, "Выйти?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    elif _gametype_ == 2:
                        choise = Text(50, 100, "Выйти?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    elif _gametype_ == 3:
                        choise = Text(50, 100, "Выйти?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    elif _gametype_ == 4: # пользовательский, надо будет поработать
                        choise = Text(50, 100, "Выйти?", "Arial", 24, C_BLACK, bg)
                        choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, C_BLACK, bg)
                    choise.drawText(True)
                    choise_pl.drawText(True)
                    pygame.display.update()
                elif _quit_ == True:
                    if event.key == pygame.K_y:
                        _quit_ = False
                        _game_ = False
                        pygame.quit()
                        _cycle_ = False
                    elif event.key == pygame.K_n:
                        _quit_ = False
                        bg.fill((200, 200, 200))
                        drawAll_1_list()
                        pygame.display.update()
                elif _quitgame_ == True:
                    if event.key == pygame.K_y:
                        _quitgame_ = False
                        _game_ = False
                        bg = pygame.display.set_mode((500, 500))
                        pygame.display.set_caption("Minesweeper")
                        bg.fill((200, 200, 200))
                        menu_btn_draw()
                        pygame.display.update()
                    elif event.key == pygame.K_n:
                        _quitgame_ = False
                        bg.fill((200, 200, 200))
                        drawAll_1_list()
                        pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if _game_ != True:
                    if btn_1.collPoint(x, y): #новичок
                        all_mines = mines(10, 9, 9)
                        
                        bg = pygame.display.set_mode((200, 255))
                        pygame.display.set_caption("Новичок")
                        bg.fill((200, 200, 200))
                        
                        drawAll_1()
                        _game_ = True
                    elif btn_2.collPoint(x, y):
                        all_mines = mines(40, 16, 16)
                        print(all_mines)

                        bg = pygame.display.set_mode((350, 420))
                        pygame.display.set_caption("Любитель")
                        bg.fill((200, 200, 200))

                        drawAll_2()
                        _game_ = True
                    elif btn_3.collPoint(x, y):
                        pass
                    elif btn_4.collPoint(x, y):
                        pass
                    elif btn_5.collPoint(x, y):
                        pass
                    elif btn_6.collPoint(x, y):
                        pygame.quit()
                        _cycle_ = False
                elif _game_ == True:
                    for e in range(len(kl_list)):
                        for pl_e in range(len(kl_list[i])):
                            if kl_list[e][pl_e].collPoint(x, y):
                                kl_list[e][pl_e].open = True
                                if kl_list[e][pl_e].mine == True:
                                    globals[_gameover_] = True
                                elif kl_list[e][pl_e].mines == 0 and kl_list[e][pl_e].mine != True:
                                    kl_list[e - 1][pl_e - 1].open = True
                                    kl_list[e - 1][pl_e].open = True
                                    kl_list[e - 1][pl_e + 1].open = True
                                    kl_list[e][pl_e - 1].open = True
                                    kl_list[e][pl_e + 1].open = True
                                    kl_list[e + 1][pl_e - 1].open = True
                                    kl_list[e + 1][pl_e].open = True
                                    kl_list[e + 1][pl_e + 1].open = True
                                if kl_list[e][pl_e].open == True:
                                    if kl_list[e][pl_e].mine == False:
                                        kl_list[e][pl_e].drawOpenKl()
                    else:
                        del e
                        del pl_e
            elif event.button == 2:
                if _game_ == True:
                    x, y = event.pos #отметка миной
                    for i in kl_list:
                        for j in kl_list[i]:
                            if kl_list[i][j].collPoint(x, y):
                                if kl_list[i][j].mined == False:
                                    kl_list[i][j].mined = True
                                    mine_kol -= 1
                                    kl_list[i][j].mine_otr_flag()
                                elif kl_list[i][j].mined == True:
                                    kl_list[i][j].mined = False
                                    mine_kol += 1
                                    kl_list[i][j].mine_otr_flag()
                    else:
                        del i
                        del j
    if _game_ == True:
        for e in range(len(all_mines)):
            if all_mines[e].mined:
                mined_kol += 1
                if mine_kol == 0:
                    globals(_gamewin_) = True
                    _gametype_ = 1
        else:
            del e

        for e in range(kl_list):
            for e2 in range(kl_list[e]):
                if kl_list[e][e2].mines == 0 and kl_list[e][e2].mine != True:
                    autoOpening(e, e2)
        else:
            del e
            del e2
    if _gamewin_:
        if _gametype_ == 1:
            gamewin_text_size = 16
        else:
            gamewin_text_size = 24
        bg.fill(C_YELLOW)
        drawGameGUI()

        gamewin_text_x, gamewin_text_y = (bg_wid / 2) / 2, bg_hid / 2
        gamewin_text = Text(gamewin_text_x, gamewin_text_y, "Ты выиграл!", "Arial", gamewin_text_size, C_DARK_BLUE, bg)
        
        home_btn = Btn(gamewin_text_x, gamewin_text_y + 30, menu_btn_wid, menu_btn_hid, bg, C_LIGHT_BLUE, C_LIDARK_BLUE)
        home_btn_text = Text(gamewin_text_x, gamewin_text_y + 30, "В главное меню", "Arial", gamewin_text_size, C_BLACK, bg)
        replaying_btn = Btn(gamewin_text_x, gamewin_text_y + 60, menu_btn_wid, menu_btn_hid, bg, C_LIGHT_BLUE, C_LIDARK_BLUE)
        replaying_btn_text = Text(gamewin_text_x, gamewin_text_y + 60, "Заново", "Arial", gamewin_text_size, C_BLACK, bg)
    elif _gameover_:
        if _gametype_ == 1:
            gameover_text_size = 16
        else:
            gameover_text_size = 24
        bg.fill(C_DARK_GRAY)
        drawGameGUI()

        gameover_text_x, gameover_text_y = (bg_wid / 2) / 2, bg_hid / 2
        gamewin_text = Text(gameover_text_x, gameover_text_y, "Ты выиграл!", "Arial", gameover_text_size, C_BLACK, bg)
        
        home_btn = Btn(gameover_text_x, gameover_text_y + 30, menu_btn_wid, menu_btn_hid, bg, C_LIGHT_BLUE, C_LIDARK_BLUE)
        home_btn_text = Text(gameover_text_x, gameover_text_y + 30, "В главное меню", "Arial", gameover_text_size, C_BLACK, bg)
        replaying_btn = Btn(gameover_text_x, gameover_text_y + 60, menu_btn_wid, menu_btn_hid, bg, C_LIGHT_BLUE, C_LIDARK_BLUE)
        replaying_btn_text = Text(gameover_text_x, gameover_text_y + 60, "Заново", "Arial", gameover_text_size, C_BLACK, bg)
    # потом доделать
    pg_timer.tick(40)