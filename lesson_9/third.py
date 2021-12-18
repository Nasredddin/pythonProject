def gen_f(x, y):
    for i in range(x + 1, y):
        yield i


for n in gen_f(int(input("First num: ")), int(input("Second num: "))):
    print(n, end=" ")
