timetable = {
    "Понедельник": ["Русский", "Литература", "Биология", "Биология", "Алгебра", "Информатика", "Информатика"],
    "Вторник": ["История", "География", "Английский", "Физ.культура", "Родная литература", "Технология"],
    "Среда": ["Химия", "Химия", "Геометрия", "Алгебра", "Обществознание", "Английский", "Русский"],
    "Четверг": ["Алгебра", "Физика", "Физика", "Русский", "Литература", "ОБЖ", "Английский"],
    "Пятница": ["Музыка", "Фин.грамотность", "Физ.культура", "Геометрия", "География", "История"]
}

def print_timetable():
    for i in timetable:
        print(str(i) + ":", ", ".join(timetable[i]) + ".")