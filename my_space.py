# -*- coding: utf8 -*-
from random import randint

for i in range(3):
    number = randint(1, 4)

    if number == 1:
        print('Травяные поля')
    elif number == 2:
        print('Скалистая пустыня')
    elif number == 3:
        print('Северный лес')
    else:
        print('Пустынные дюны')
