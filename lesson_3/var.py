import time
num1 = 4
num2 = 6

print("Было:", num1, num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Стало:", num1, num2)

time.sleep(5)
