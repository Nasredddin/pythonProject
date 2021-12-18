import random
nums = random.sample(range(10), 10)
y = int(input("Y: "))
var = list(map(lambda x: x ** y, nums))
print(var)
