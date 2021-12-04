enter_num = input("Введите число от 3 до 9: \n")
if enter_num.isdigit():
    if 3 <= int(enter_num) <= 9:
        for i in range(2, int(enter_num)+2):  # Количество шагов
            for j in range(1, i - 1):  # Числа по возрастанию
                print(j, end="")
            for j in range(i - 1, 0, -1):  # Числа по убыванию
                print(j, end="")
            print()
    else:
        print("!")
else:
    print("Ошибка. Повторите")
