text = input("Введите текст:\n")
dictionary = {}
for word in text.split():
    if not dictionary.get(word) == None:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for word, value in dictionary.items():
    print(f"Слово '{word}' повторяется {value} раз.")
