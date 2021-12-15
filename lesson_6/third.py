import random
print(len(list(set(random.sample(range(100), 10)) ^ set(random.sample(range(100), 10)))))
