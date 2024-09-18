# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = sum(1 for letter in word.lower() if letter in ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"))
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = list(sentence.split(" "))
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = list(sentence.split(" "))
for i in range(0, len(words)):
    print(words[i][0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(words)/len(sentence))