num = input("число: ")
count = 0
for x in range(0, len(num)):
    for y in range(x + 1, len(num), 2):
        if num[x] == num[y]:
            count += 1
if count > 0:
    print("Цифры повторяются")
else:
    print("Цифры не повторяются")
