import pygame as pg
from pygame.color import THECOLORS

def check_win(mas, sign):
    drawer = 0
    for row in mas:
        drawer+= row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):
        if mas[0][col]==sign and mas[1][col]==sign and mas[2][col]==sign:
            return sign
    if mas[0][0]==sign and mas[1][1]==sign and mas[2][2]==sign:
        return sign
    if mas[0][2]==sign and mas[1][1]==sign and mas[2][0]==sign:
        return sign
    if drawer==0:
        return 'Draw'
    return False



pg.init()

screen = pg.display.set_mode((450, 450))
pg.display.set_caption('Крестики-нолики')
size_block = 130
margin = 15
width = heigth = size_block*3 + margin*4
query = 0 

mas = []
for i in range(3):
    mas.append([0]*3)
game_over = False
while True:
    for event in pg.event.get():
        if event.type == pg.WINDOWCLOSE:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (size_block + margin) # проверяем на какой блок кликнули
            row = y_mouse // (size_block + margin) 
            if mas[row][col] == 0: # проверка заполненной клетки
                if query%2==0: # меняется очередность хода"
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query+=1
        elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            game_over = False
            mas = []
            for i in range(3):
                mas.append([0]*3)
            query = 0
            screen.fill(THECOLORS['black'])

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col]=='x':
                    color = THECOLORS['red']
                elif mas[row][col]=='o':
                    color = THECOLORS['green']
                else:
                    color = THECOLORS['white']
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pg.draw.rect(screen, color, (x, y, size_block, size_block))
                if color==THECOLORS['red']:
                    pg.draw.line(screen, THECOLORS['white'], (x+4,y+4), (x+size_block-4,y+size_block-4), 5)
                    pg.draw.line(screen, THECOLORS['white'], (x+size_block-4,y+4), (x+4, y+size_block-4), 5)
                elif color==THECOLORS['green']:
                    pg.draw.circle(screen,THECOLORS['white'], (x+size_block//2, y+size_block//2),size_block//2-3, 5)

    if (query-1)%2==0: #x
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(THECOLORS['black'])
        font = pg.font.SysFont('curiernew', 80)
        text1 = font.render(game_over, True, THECOLORS['white'])
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2    
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pg.display.update()
#for commit