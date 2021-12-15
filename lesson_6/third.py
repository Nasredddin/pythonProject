import random
print(len(set(random.sample(range(100), 10)) ^ set(random.sample(range(100), 10))))
