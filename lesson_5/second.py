import random
random_value = random.randrange(1, 100)
score = 0

while True:
    num = input("Введите число от 1 до 100:\n")
    if num.isdigit():

        if 1 > int(num) or int(num) > 100:
            score += 1
            print(f"Ошибка, повторите попытку!!!\nЧисло попыток: {score}\n")

        elif int(num) > random_value:
            score += 1
            print(f"Число меньше.\nЧисло попыток: {score}\n")

        elif int(num) < random_value:
            score += 1
            print(f"Число больше.\nЧисло попыток: {score}\n")

        else:
            print(f"\U0001f60e\U0001f60e\U0001f60eВы угадали\U0001f60e\U0001f60e\U0001f60e \nЧисло попыток:{score}")
            break
    else:
        score += 1
        print(f"Ошибка, повторите попытку!!!\nЧисло попыток: {score}\n")
