def sum():
    num = list(input("Введите список:\n").split())
    k = int(input("K: "))
    for i in range(1, len(num) + 1):
        for j in range(i + 1, len(num) + 1):
            if i + j == k:
                return True


print(sum())
