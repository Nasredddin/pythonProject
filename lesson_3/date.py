import time
print("Введите год:")
date = int(input())

if 1900 < date < 1000000:
    var = 0
else:
    print("Введенный год не соответствует условию, повторите ввод.")
    exit()

if (date % 4 == 0 and not date % 100 == 0
    or date % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")
time.sleep(5)
