import random

# while (digits_count > 0):
#     mystery.append(str(random.randint(0, 9)))
#     digits_count -= 1
# print(mystery)


def game():
    while True:   #Зацикливаем игру

        #Создаём нужные переменные.
        digits_count = 4
        mystery = []
        numders = list("0123456789")

        #Создаём число с неповторяющимися цифрами
        while digits_count > 0:
            num = random.choice(numders)
            numders.remove(num)
            mystery.append(num)
            digits_count -= 1

        while True:  #Зацикливаем возможность пользователя угадывать число

            #Ввод числа и проверка на правильность
            while True:
                print("Введите число (4 цифры):")
                attempt = input()
                if len(attempt) != 4:
                    print("Число должно содержать только 4 числа!")
                else:
                    break

            #Вычисляем число быков и коров
            b = []
            for i, v in enumerate(attempt):
                if v not in mystery:
                    b.append("grey")
                elif v == mystery[i]:
                    b.append("green")
                else:
                    b.append("yellow")
            print(*b)

            #Проверяем, угадал ли пользователь число
            if b.count("green") == 4:
                print("Ты победил!")
                break

        #Спрашиваем у пользователя хочет ли он продолжить играть. (Y - да, любые другие значения - нет)
        print("Вы хотите продолжить играть дальше? (Y/N)")
        if input() == "Y":
            continue
        else:
            break