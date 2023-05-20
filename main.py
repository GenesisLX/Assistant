from prettytable import PrettyTable
from bulls_and_cows_game import *
from guiCalc import run_calculator as run_gui_calc
from leapYear import *

table_do = ["Какой сегодня год/месяц/день/дата?", "Включи калькулятор.", "Включи игру быки и коровы.",
            "Выведи расписание на неделю для 8 'Д' класса", "Этот год високосный?"]

timetable = {
    "Понедельник": ["Русский", "Литература", "Биология", "Биология", "Алгебра", "Информатика", "Информатика"],
    "Вторник": ["История", "География", "Английский", "Физ.культура", "Родная литература", "Технология"],
    "Среда": ["Химия", "Химия", "Геометрия", "Алгебра", "Обществознание", "Английский", "Русский"],
    "Четверг": ["Алгебра", "Физика", "Физика", "Русский", "Литература", "ОБЖ", "Английский"],
    "Пятница": ["Музыка", "Фин.грамотность", "Физ.культура", "Геометрия", "География", "История"]
}

mytable_do = PrettyTable()
mytable_do.field_names = ["Команда/Фраза."]
for i in table_do:
    mytable_do.add_row([i])
print(mytable_do)

while True:
    request = input("Введите вашу команду: ").lower()

    if request == "включи игру быки и коровы" or request == "включи игру быки и коровы.":
        game()
    elif request == "включи калькулятор" or request == "включи калькулятор.":
        run_gui_calc()
    elif request == "этот год високосный" or request == "этот год високосный?":
        leap_year_definition()
    elif request == "какой сегодня год" or request == "какой сегодня год?":
        print(datetime.date.today().year)
    elif request == "какой сегодня месяц" or request == "какой сегодня месяц?":
        print(datetime.date.today().month)
    elif request == "какой сегодня день" or request == "какой сегодня день?":
        print(datetime.date.today().day)
    elif request == "какая сегодня дата" or request == "какая сегодня дата?":
        print(datetime.date.today())
    elif request == "выведи расписание на неделю для 8 'д' класса" or request == "выведи расписание на неделю для 8 д класса":
        for i in timetable:
            print(str(i) + ":", ", ".join(timetable[i]) + ".")
    else:
        print("Неизвестная команда. Введите верную команду.")









