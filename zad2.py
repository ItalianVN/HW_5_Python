# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

n = 2021
import random
print(f'Конфет на столе: {n}')
is_my_turn = bool(random.randint(0, 1))
while n > 0:
    if is_my_turn:
        while 1:
            try:
                x = int(input('>'))
                if x not in range(1, 29) or x > n:
                    raise ValueError
                break
            except ValueError:
                print('Некорректное значение, введите число от 1 до 28')
    else:
        x = random.randint(1, 28)
        if n < 29:
            x = n
        elif n - x < 29:
            x = n - 29
            if x <= 0:
                x = 1
    n -= x
    print(f'{"Я" if is_my_turn else "Бот"} взял {x} конфет',
        f'{n} осталось на столе', sep='\n')
    is_my_turn = not is_my_turn
print(f'{"Компьютер" if is_my_turn else "Я"} выиграл!')