num = int(input("Число: "))
for i in range(1, num):
    a = i ** 2
    if (a % 10 == i
        or a % 100 == i and not a % 10 == i
            or a % 1000 == i and not a % 100 == i and not a % 10 == i):
        print(f"{i} * {i} =", a)
