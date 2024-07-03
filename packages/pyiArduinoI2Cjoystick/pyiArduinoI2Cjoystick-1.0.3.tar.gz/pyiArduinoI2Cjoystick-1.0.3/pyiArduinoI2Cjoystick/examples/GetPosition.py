#!/usr/bin/python3
# ДАННЫЙ ПРИМЕР ВЫВОДИТ КООРДИНАТЫ ДЖОЙСТИКА:

import curses

# Подключаем библиотеку для работы с джойстиком I2C-flash.
from pyiArduinoI2Cjoystick import *

# Объявляем объект для работы с библиотекой, указывая адрес модуля на шине.
j = pyiArduinoI2Cjoystick(bus="/dev/i2c-3")

# Если объявить объект без указания адреса, то адрес будет найден автоматически.
#j = pyiArduinoI2Cjoystick()


def draw_joystick(stdscr):

    stdscr.clear()
    stdscr.refresh()

    k = 0
    # Не блокировать выполнение при getch()
    stdscr.nodelay(1)
    # Время ожидания нажания кнопки клавиатуры (getch())
    stdscr.timeout(100)

    while (k != ord('q')):
        stdscr.clear()
    
        title = "Текущие координаты: (нажмите q для выхода)"
    
        # Получаем и выводим координаты по отдельности: #
        coordstr = "X = {}, Y = {}".format(j.x, j.y)
    
        # Получаем сразу обе координаты:
        x, y = j.getPosition()
    
        bothcoord = "X:Y={}:{}".format(x, y)
    
        stdscr.addstr(0,0, title)
        stdscr.addstr(1,0, coordstr)
        stdscr.addstr(2,0, bothcoord)
        stdscr.refresh()
        k = stdscr.getch()

def main():
    curses.wrapper(draw_joystick)

if __name__ == "__main__":
    main()
