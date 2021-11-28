# num = input("число: ")
# count = 0
# for i in range(0, len(num)):
#     for j in range(i + 1, len(num)):
#        if num[i] == num[j]:
#            count += 1
# print(i, j)
# if count > 0:
#     print("Да")
# else:
#     print("Нет")

m = int(input("input num: "))
d = m % 10
print(d)
i = m // 10
print(i)
m = m // 10
print(m)
flag = 0
while (i > 0) and (flag == 0):
    if d == i % 10:
        flag = 1
    i = i // 10
while (m > 0) and (flag == 0):
    if m == d:
        flag == 1
    if m % 10 == d:
        flag == 1
    else:
        m = m // 10
if flag == 1:
    print('YES')
else:
    print("NO")
