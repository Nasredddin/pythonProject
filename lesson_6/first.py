import random
list1 = random.sample(range(10), 10)
print(list1)
k = int(input("Число K: "))
for i in range(k + 1, len(list1)):
    list1[i - 1] = list1[i]
list1.pop()
print(list1)
