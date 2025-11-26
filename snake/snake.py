import os
import random
import threading
import time
import readchar
from threading import Thread
import queue
import re
############
# ширина!, длина!, пустая клетка!, голова!, тело!, цвет!, скорость!, играть в листах или в строках!
colors_help = '''0 = Black
1 = Blue
2 = Green
3 = Aqua
4 = Red
5 = Purple
6 = Yellow
7 = White
8 = Gray
9 = Light Blue
a = Light Green
b = Light Aqua
c = Light Red
d = Light Purple
e = Light Yellow
f = Bright White'''
empty_cell = '0'
row = [[empty_cell]*16 for i in range(12)]
field = {'value': '12x16',
'first_inst': 'Введите размер игрового поля в формате "12x15" (12 - сверху вниз, 15 - слева направо).\nМаксимальный размер: 49x49\nМинимальный: 3x3\n',
'assuring': 'Подтвердите, введя "Y"/"y" или выбирайте другой размер\nМаксимальный размер: 49x49\nМинимальный: 3x3\n',
'error': 'Непредусмотренный размер. Попробуйте ещё раз.',
'value_re': r'(^[1-4][0-9][xх][1-4][0-9]$)|(^[3-9][xх][3-9]$)|(^[1-4][0-9][xх][3-9]$)|(^[0-9][xх][1-4][3-9]$)'}
color = {'value': '07',
'first_inst': f'Выберите цвет фона и поля в формате "1a" (1 - фон, a - поле):\n\n{colors_help}\n',
'assuring': f'Подтвердите, введя "Y"/"y" или выбирайте другой цвет.\n\n{colors_help}\n',
'error': 'Непредусмотренный ввод. Попробуйте ещё раз.',
'value_re': r'^[0-9a-fABCDEF]{2}$'}
speed = 1
food = {'location': None, 'status': False, 'symbol': '+'}
snake = {'head': [2,2], 'body': [(2,1),(2,0)], 'tail_old': (2,len(row[0])-1), 'symbol': '1'}
direction = {'current': 'd', 'old': 'd'}
possible_dirs = ('d', 'a', 'w', 's')
def set_option(option: dict, option_type: str, field_state, empty_cell: str): # функция для установки размера поля и цвета
    i = False
    while True:
        os.system('cls')
        print(*field_state, sep = '\n')
        if i == False:
            option['value'] = input(option['first_inst'])
            i = True
            if bool(re.search(option['value_re'], option['value'])) == True:
                match option_type:
                    case 'color':
                        os.system(f'color {option['value']}')
                    case 'field':
                        scales = list(re.finditer(r'^(?P<fir>\d+)[xх](?P<sec>\d+)$', option['value']))
                        if type(field_state[0]) == list:
                            field_state = [[empty_cell]*int(scales[0]['sec']) for i in range(int(scales[0]['fir']))]
                        else:
                            field_state = [empty_cell*int(scales[0]['sec']) for i in range(int(scales[0]['fir']))]
        elif bool(re.search(r'^[Yy]$', option['value'])) == True:
            break
        elif bool(re.search(option['value_re'], option['value'])) == True:
            option['value'] = input(option['assuring'])
            if bool(re.search(option['value_re'], option['value'])) == True:
                match option_type:
                    case 'color':
                        os.system(f'color {option['value']}')
                    case 'field':
                        scales = list(re.finditer(r'^(?P<fir>\d+)[xх](?P<sec>\d+)$', option['value']))
                        if type(field_state[0]) == list:
                            field_state = [[empty_cell]*int(scales[0]['sec']) for i in range(int(scales[0]['fir']))]
                        else:
                            field_state = [empty_cell*int(scales[0]['sec']) for i in range(int(scales[0]['fir']))]
        else:
            print(option['error'])
            option['value'] = input(option['first_inst'])
            match option_type:
                case 'color':
                    os.system(f'color {option['value']}')
                case 'field':
                    scales = list(re.finditer(r'^(?P<fir>\d+)[xх](?P<sec>\d+)$', option['value']))
                    if bool(re.search(option['value_re'], option['value'])) == True:
                        if type(field_state[0]) == list:
                            field_state = [[empty_cell]*int(scales[0]['sec']) for i in range(int(scales[0]['fir']))]
                        else:
                            field_state = [empty_cell*int(scales[0]['sec']) for i in range(int(scales[0]['fir']))]
    return field_state

def set_characters(string: str, char_type: str):
    while True:
        os.system('cls')
        match char_type:
            case 'empty':
                string = input('Введите символ для пустого места: ')
            case 'body':
                string = input('Введите символ для тела змеи: ')
            case 'food':
                string = input('Введите символ для еды: ')
        if len(string) != 1:
            os.system('cls')
            print('Ошибка ввода. Нужно ввести один символ.')
            time.sleep(2)
        else:
            print(f'Символ {string} установлен.', sep= '\n')
            time.sleep(2)
            break
    return string

def set_speed(speed):
    while True:
        os.system('cls')
        try:
            speed = 1/float(input('Введите скорость змеи (клетки в секунду): '))
            break
        except:
            print('Недопустимое число. Попробуйте ещё раз.')
            time.sleep(2)
    return speed
        
         
def set_str_or_list(field):
    while True:
        os.system('cls')
        decid = input('Вы хотите играть в списках или в строках?\nНапишите "str" или "list" для выбора.\n')
        if decid == 'str':
            field = [''.join(x) for x in field]
            print('Выбрана игра в строках.')
            time.sleep(2)
            break
        elif decid == 'list':
            print('Выбрана игра в списках.')
            time.sleep(2)
            break
        else:
            print('Неправильный ввод. Попробуйте ещё раз.\n')
            time.sleep(2)
    return (field, decid)
############
row, decid = set_str_or_list(row)
snake['symbol'] = set_characters(snake['symbol'], 'body')
empty_cell = set_characters(empty_cell, 'empty')
food['symbol'] = set_characters(food['symbol'], 'food')
speed = set_speed(speed)
if decid == 'str': # костыли для правильного отображения поля
    row = [empty_cell*16 for x in range(12)]
else:
    row = [[empty_cell]*16 for x in range(12)]
row = set_option(field, 'field', row, empty_cell)
set_option(color, 'color', row, empty_cell)
############
if decid == 'str': # конвертация в списки
    converted = []
    for y in row:
        con = []
        for x in y:
            con.append(x)
        converted.append(con)
    row = converted

row[2][2] = snake['symbol'] #координаты тела
row[2][1] = snake['symbol']
row[2][0] = snake['symbol']

if decid == 'str': # конвертация обратно в строки
    converted = []
    for y in row:
        converted.append(''.join(y))
    row = converted
######
def body_move(snake, empty_cell: str):
    body = []
    snake['tail_old'] = snake['body'][-1]
    for i in range(len(snake['body'])):
        if snake['body'][0] == snake['body'][i]: # the closest part to head
            body.append(tuple(snake['head']))
        elif snake['body'][-1] == snake['body'][i] and food['location'] == tuple(snake['head']): # eating
            body.append(snake['body'][i])
        elif snake['body'][-1] == snake['body'][i]: # tail
            row[snake['body'][i][0]][snake['body'][i][1]] = empty_cell
            body.append(snake['body'][i-1])
        else:
            body.append(snake['body'][i-1])
    snake['body'] = body
######

queue_obj = queue.Queue()
def input_dir(d, q):
    while True:
        d = readchar.readkey()
        if d == readchar.key.ESC:
            break
        q.put(d)
t1 = threading.Thread(target = input_dir, args = (direction['current'], queue_obj))
t1.start()
def check_dir(): # проверка на то, чтобы не проходили противоположные направления и непредусмотренный инпут
    match direction:
        case {'current': 'a', 'old': 'd'} | {'current': 'd', 'old': 'a'} | {'current': 'w', 'old': 's'} | {'current': 's', 'old': 'w'}:
            direction['current'] = direction['old']
        case x if not x['current'] in possible_dirs:
            direction['current'] = direction['old']


def food_appear(food): # выбирает любое свободное место для появления еды и вызывает её
    if food['status'] == False:
        food['location'] = random.choice([(x,y) for x in range(len(row)) for y, elm in enumerate(row[x]) if elm != snake['symbol'] and elm != snake['symbol']])
        row[food['location'][0]][food['location'][1]] = food['symbol']
        food['status'] = True

def food_eating(food, counting, snake):
    if food['location'] == tuple(snake['head']):
        counting += 1
        food['status'] = False
        food['location'] = None
        snake['body'].append(snake['tail_old'])
        row[snake['tail_old'][0]][snake['tail_old'][1]] = snake['symbol']
    return counting

def collision(snake, count):
    count = str(count) + ' Game over'
    return count
######
count = 0
food_status = False
######
while True:
    if tuple(snake['head']) in snake['body']: # Game over
        count = collision(snake, count)
        os.system('cls')
        print(*row, direction['current'], f'count: {count}', 'Нажмите ESC для выхода', food['location'], sep = '\n')
        break
    if decid == 'str': # конвертация в списки
        converted = []
        for y in row:
            con = []
            for x in y:
                con.append(x)
            converted.append(con)
        row = converted
    time.sleep(speed)
    os.system('cls')
    food_appear(food)
    try:
        direction['current'] = queue_obj.get(0)
    except:
        direction['current'] = direction['current']

######
    check_dir()
######
    match direction['current']:
        case 'd':
            if snake['head'][1] == len(row[0])-1:
                row[snake['head'][0]][0] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][1] = 0

            else:
                row[snake['head'][0]][snake['head'][1]+1] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][1] += 1
        
        case 'a':
            if snake['head'][1] == 0:
                row[snake['head'][0]][len(row[0])-1] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][1] = len(row[0])-1

            else:
                row[snake['head'][0]][snake['head'][1]-1] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][1] -= 1
        case 'w':
            if snake['head'][0] == 0:
                row[len(row)-1][snake['head'][1]] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][0] = len(row)-1

            else:
                row[snake['head'][0]-1][snake['head'][1]] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][0] -= 1
        
        case 's':
            if snake['head'][0] == len(row)-1:
                row[0][snake['head'][1]] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][0] = 0

            else:
                row[snake['head'][0]+1][snake['head'][1]] = snake['symbol']
                body_move(snake, empty_cell)
                snake['head'][0] += 1
    count = food_eating(food, count, snake)
    if decid == 'str': # конвертация обратно в строки
        converted = []
        for y in row:
            converted.append(''.join(y))
        row = converted
    print(*row, direction['current'], f'count: {count}', food['location'], sep = '\n') # визуализация
    direction['old'] = direction['current']
#while True:
    
