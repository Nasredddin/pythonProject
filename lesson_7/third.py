dictionary = {}
var = 1
for i in range(int(input("Количество строк: "))):
    line = input(f"{var} строка:\n").split()
    var += 1
    for word in line:
        dictionary[word] = dictionary.get(word, 0) + 1

max_value = max(dictionary.values())
most_frequent = [k for k, v in dictionary.items() if v == max_value]
print(min(most_frequent))
