# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ('а', 'я', 'е', 'э', 'о', 'ё', 'у', 'и', 'ы', 'ю')
quantity = 0
for i in word.lower():
    if i in vowels:
        quantity += 1
print(quantity)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print(sum(len(i) for i in sentence.split()) // len(sentence.split()))