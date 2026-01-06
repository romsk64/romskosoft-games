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
pg_timer = pygame.time.Clock()
mine_kol = 0
kl_list = []
gui_list = []
menu_btns = []
menu_btns_text = []
kl_wid, kl_hid = 20, 20
menu_btn_wid, menu_btn_hid = 177, 25

class Text():
    def __init__(self, x, y, text, font, fsize, txt_col, win):
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
    def __init__(self, x, y, wid, hid, win, col = (162, 162, 162), cnt_col = (100, 100, 100)):
        super().__init__(font = "Arial", fsize = 12, txt_col = (0, 0, 0), x = x, y = y, text = None, win = win)
        self.x = x
        self.y = y
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
    def collPoint(self):
        return self.rect.collidepoint(x, y)
    
class Btn():
    def __init__(self, x, y, wid, hid, win, col = (162, 162, 162), cnt_col = (100, 100, 100)):
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
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.win = win
    def draw(self):
        for i in range(6):
            pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(self.x - 2 + i, self.y - 6, 1, 1)) # черный пиксель самый верх
            pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x - 2 + i, self.y - 5, 1, 1)) # желтый пиксель самый верх
        for i2 in range(2):
            for j in range(2):
                pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(self.x - 4 + (i2 * 6) + j, self.y - 5, 1, 1)) # по 2 черных пикселя чуть ниже верха
        for i3 in range(10):
            pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x - 4 + i3, self.y - 4, 1, 1)) # ряд из 10 желтых пикселей
        for i4 in range(2):
            pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(self.x - 5 + (i4 * 10), self.y - 4, 1, 1)) # 2 черных пикселя по краям ряда выше
        for i5 in range(12):
            pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x - 5 + i5, self.y - 3, 1, 1)) # ряд из 12 желтых пикселей
        for i6 in range(2):
            for j2 in range(2):
                pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x - 4 + (i6 * 8) + j2, self.y - 2, 1, 1)) # по 2 желтых писеля с краев
        for i7 in range(2):
            for j3 in range(3):
                pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x - 5 + (i7 * 8) + j3, self.y - 1, 1, 1)) # по 3 жельых пикселя с краев
        for i8 in range(2):
            for j4 in range(2):
                for x in range(2):
                    pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(self.x - 2 + x + (i8 * 4), self.y - 2 + j4, 1, 1)) # глаза
        for i9 in range(2):
            for j5 in range(2):
                pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(self.x - 5 + (i9 * 12), self.y - 3 + j5, 1, 1)) # 2 черных пикселя с краев
        for i10 in range(2): # 14
            for j6 in range(4): # 6
                pygame.draw.rect(self.win, (0, 0, 0), pygame.rect.Rect(self.x - 6 + (i10 * 14), self.y - 1 + j6, 1, 1)) # 4 черных пикселя по краям
        for i11 in range(3): # -5
            for j7 in range(13): # 14
                pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x - 5 + j7, self.y + i11, 1, 1)) # желтые пиксели в середине лица
        for i12 in range(2):
            for j8 in range(2):
                pygame.draw.rect(self.win, (255, 255, 0), pygame.rect.Rect(self.x + j8, self.y - 2 + i12, 1, 1)) # между глазами

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
    for i in range(9):
        for j in range(9):
            kl_list[i].append(Kletka(5 + j * kl_wid + j, 50 + (kl_hid * i) + (2 * i), kl_wid, kl_hid, bg))
            kl_list[i][j].drawKl()

    time_timer_otr_btn.drawBtn()
    mine_kol_otr_btn.drawBtn()
    time_timer_otr.drawText()
    mine_kol_otr.drawText()
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

def menu_btn_draw(): # потом
    global menu_btns
    global menu_btns_text
    for i in range(6):
        menu_btns[i].drawBtn()
    for j in range(7):
        menu_btns_text[j].drawText()

bg.fill((200, 200, 200))
name = Text(10, 10, "romsk64's minesweeper", "Arial", 24, (0, 0, 0), bg)
menu_btns_text.append(name)

btn_1 = Btn(10, 50, menu_btn_wid, menu_btn_hid, bg)
btn_1_text = Text(10, 52, "[1] Новичок (9x9)", "Times New Roman", 16, (0, 0, 0), bg)
menu_btns.append(btn_1)
menu_btns_text.append(btn_1_text)

btn_2 = Btn(10, 85, menu_btn_wid, menu_btn_hid, bg)
btn_2_text = Text(10, 87, "[2] Любитель (16x16)", "Times New Roman", 16, (0, 0, 0), bg)
menu_btns.append(btn_2)
menu_btns_text.append(btn_2_text)

btn_3 = Btn(10, 120, menu_btn_wid, menu_btn_hid, bg)
btn_3_text = Text(10, 122, "[3] Профессионал (30x16)", "Times New Roman", 16, (0, 0, 0), bg)
menu_btns.append(btn_3)
menu_btns_text.append(btn_3_text)

btn_4 = Btn(10, 155, menu_btn_wid, menu_btn_hid, bg)
btn_4_text = Text(10, 157, "[4] Пользовательский", "Times New Roman", 16, (0, 0, 0), bg)
menu_btns.append(btn_4)
menu_btns_text.append(btn_4_text)

btn_5 = Btn(10, 225, menu_btn_wid, menu_btn_hid, bg)
btn_5_text = Text(10, 227, "[5] Настройки", "Times New Roman", 16, (0, 0, 0), bg)
menu_btns.append(btn_5)
menu_btns_text.append(btn_5_text)

btn_6 = Btn(10, 260, menu_btn_wid, menu_btn_hid, bg)
btn_6_text = Text(10, 262, "[ESC] Выход", "Times New Roman", 16, (0, 0, 0), bg)
menu_btns.append(btn_6)
menu_btns_text.append(btn_6_text)

menu_btn_draw()

time_timer = 0 #ну типа тайм
time_timer_otr = Text(5, 7, f"{time_timer}", "Arial", 16, (0, 0, 0), bg) # корды для новичка
time_timer_otr_btn = Btn(5, 5, 30, 20, bg)
mine_kol_otr = Text(160, 7, f"{mine_kol}", "Arial", 16, (0, 0, 0), bg) # корды для новичка
mine_kol_otr_btn = Btn(160, 5, 30, 20, bg)
smile_otr = 0
smile_otr_btn = Btn(100, 5, 25, 25, bg)

smile = Smile(200, 100, bg)
smile.draw()

gui_list.append([time_timer_otr, time_timer_otr_btn])
gui_list.append([mine_kol_otr, mine_kol_otr_btn])
gui_list.append([smile_otr, smile_otr_btn])

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

                    bg = pygame.display.set_mode((200, 255))
                    pygame.display.set_caption("Новичок")
                    bg.fill((200, 200, 200))

                    time_timer_otr_btn.drawBtn()
                    mine_kol_otr_btn.drawBtn()
                    time_timer_otr.drawText()
                    mine_kol_otr.drawText()

                    drawAll_1()
                    _game_ = True
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    all_mines = mines(40, 16, 16)
                    print(all_mines)

                    bg = pygame.display.set_mode((350, 420))
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
                    choise = Text(50, 100, "Выйти в главное меню?", "Arial", 24, (0, 0, 0), bg)
                    choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, (0, 0, 0), bg)
                    choise.drawText(True)
                    choise_pl.drawText(True)
                    pygame.display.update()
                elif event.key == pygame.K_ESCAPE:
                    bg.fill((200, 200, 200))
                    drawAll_1_list()
                    pygame.display.update()

                    _quit_ = True
                    choise = Text(50, 100, "Выйти?", "Arial", 24, (0, 0, 0), bg)
                    choise_pl = Text(20, 120, "Y (Yes)/N (No)", "Arial", 24, (0, 0, 0), bg)
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
            elif event.button == 2:
                if _game_ == True:
                    x, y = event.pos #отметка миной
                    for i in kl_list:
                        for j in kl_list[i]:
                            if kl_list[i][j].collPoint(x, y):
                                if kl_list[i][j].mined == False:
                                    kl_list[i][j].mined = True
                                    mine_kol -= 1
                                elif kl_list[i][j].mined == True:
                                    kl_list[i][j].mined = False
                                    mine_kol += 1
    
    pg_timer.tick(40)