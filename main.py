from prettytable import PrettyTable
from bulls_and_cows_game import *
from guiCalc import run_calculator as run_gui_calc
from leapYear import check_leap_year_definition
from timetable import print_timetable
import datetime

run_status = True


def render_main_menu():
    mytable_do = PrettyTable()
    mytable_do.field_names = ["Команда", "Действие"]
    for key, val in menu_items.items():
        mytable_do.add_row([key, val.get('name')])
    print(mytable_do)


def set_run_status(status=False):
    global run_status
    run_status = status


menu_items = {
        "1": {"name": "Текущий год", "func": lambda: print(datetime.date.today().year)},
        "2": {"name": "Текущий месяц", "func": lambda: print(datetime.date.today().month)},
        "3": {"name": "Текущий день", "func": lambda: print(datetime.date.today().day)},
        "4": {"name": "Текущая дата", "func": lambda: print(datetime.date.today())},
        "5": {"name": "Калькулятор", "func": run_gui_calc},
        "6": {"name": "Игра быки и коровы.", "func": game},
        "7": {"name": "расписание на неделю для 8 'Д' класса", "func": print_timetable},
        "8": {"name": "Проверка на високосный год", "func": check_leap_year_definition},
        "9": {"name": "Вывод меню", "func": render_main_menu},
        "0": {"name": "Выход из программы", "func": set_run_status}
        }

render_main_menu()
while run_status:
    request = input("Введите необходимую команду: ")
    menu_item = menu_items.get(request)
    if menu_item is not None:
        menu_item.get('func')()
    else:
        print("Неизвестная команда. Введите верную команду.")












