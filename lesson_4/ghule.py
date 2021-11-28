num = 1000 #int(input("press 7 \n"))
time1 = 0
print(num)
while num > 1:
    print(f"1000 - 7 = {num-7}", time1)
    num -= 7
    time1 += 1
    if num < 7:
        break
else:
    print("none")