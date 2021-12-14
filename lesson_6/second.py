import random
my_list = random.sample(range(10), 10)
print(my_list)
k = int(input("Число К: "))
c = int(input("Число C: "))
my_list.append(0)
for i in range(len(my_list) - 1, k, -1):
    my_list[i] = my_list[i - 1]
my_list[k] = c
print(my_list)
