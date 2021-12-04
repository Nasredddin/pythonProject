enter_num = int(input("Введите число от 3 до 9: \n"))
if 3 <= enter_num <= 9:
    for i in range(2, enter_num+2):  # Количество шагов
        for j in range(1, i - 1):  # Числа по возрастанию
            print(j, end="")
        for j in range(i - 1, 0, -1):  # Числа по убыванию
            print(j, end="")
        print()
else:
    print("TOTAL ERROR")
