var = input("Ведите текст\n")
text_split = var
text_split = text_split.split()
while len(text_split) > 1:
    var = (var[::-1])
    print(var.title())
    break
else:
    print("Repeat")
