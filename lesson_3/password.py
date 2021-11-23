import time
print("Введите пароль")
first_pass = input()
print("Повторите пароль")
second_pass = input()
if first_pass == second_pass:
    print("OK!")
else:
    print("Пароли не совпадают!")
time.sleep(5)
