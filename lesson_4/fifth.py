string = input("Введите строку:\n")
char = input("Ведите символ для поиска\n")
score = 0
d = -1
while True:
    d = string.find(char, d+1)
    # print(d)
    if d < 0:
        break
    score += 1
print("Символов в строке: ", score)
