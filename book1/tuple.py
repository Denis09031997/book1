import string

print('-' * 50, 'ИЗУЧАЕМ КОРТЕЖИ', '-' * 50)
t = ('a', 'b')
print(t, type(t))
t1 = ('a')
print(t1, type(t1))
t2 = 'a', 'b'
print(t2, type(t2))
t3 = 'a',
print(t3, type(t3))
my_tuple = ('a', 'b', 3, 5, 'Bob')
print(f'my_tuple = {my_tuple}, my_tuple[2] = {my_tuple[2]}')
my_tuple2 = my_tuple + ('Denis', "Bank of America")
print('My tuple =', my_tuple, 'my_tuple2 = ', my_tuple2)
my_tuple3 = my_tuple2[3:]
print(my_tuple3)
print('Сравнение кортежей:')
print(my_tuple < my_tuple2)
print(my_tuple2 == my_tuple3)
x = ('a', 'y')
x2 = ('a', 'z')
x3 = ('a', 'y')
print(x == x2, x == x3, x3 == x2)
print('Сортировка кортежа.', '-' * 50)
tuple1 = (5, 3, 2, 11, 1, 6)
print(tuple1)
print(sorted(tuple1))
print(tuple(sorted(tuple1)))
txt = 'but soft what light in yonder window breaks'
print(txt)
words = txt.split()
print(words)
t = list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
print(t)
res = list()
for lenght, word in t:
    res.append(word)
print('res =', res)
print('_' * 100)
m = ['Qiwi', 'Tinkoff', 'Sber']
a, b, c = m
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(m, type(m))
m2 = ['Kia', 'Volvo']
x1 = m2[1]
y2 = m2[0]
print(x1, type(x1))
print(y2)
print('-' * 120)
d = ['apple', 'lime', 'qiwi']
(z, v, g) = d
print(z, type(z))
print(v)
print(g)
print(z, v, g)
print(z)
z, v, g = g, v, z
print(z, v, g)
print(z)
addr = 'den.scherbinin2018@yandex.ru'
uname, domen = addr.split('@')
print('uname = ', uname, '|', 'domen = ', domen)
dictionary = {'a': 1, 'z': 52, "d": 4, 'b': 2}
print(dictionary)
t_d = list(dictionary.items())
print(t_d)
t_d.sort()
print(t_d)
print('-' * 120)
d_dic = {
    'a': 10,
    'c': 22,
    'b': 1,
}

for key, value in list(d_dic.items()):
    print(f'list(d_dic.items()) = {list(d_dic.items())}')
    print('key -', key, 'value -', value)

print('Сортировка:')
l_dic = []

for k, v in d_dic.items():
    l_dic.append((v, k))
    l_dic.sort(reverse=True)

print(f'res = {l_dic}')
print('-' * 150)

fhand = open('romeo-full.txt')
counts = {}
for l_romeo in fhand:
    l_romeo = l_romeo.translate(str.maketrans('', '', string.punctuation))
    l_romeo = l_romeo.lower()
    words_romeo = l_romeo.split()
    for w in words_romeo:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1

lst_romeo = []
for k, v in list(counts.items()):
    lst_romeo.append((v, k))

lst_romeo.sort(reverse=True)

for k, v in lst_romeo[:10]:
    print(k, v)

print('-' * 120)
print('Практика')
print('-' * 120)
print('УПРАЖНЕНИЕ 1')
file = input('Enter file name: ')
fhand_email_addres = open(file)
counts_email_addres = {}

for i in fhand_email_addres:
    i = i.rstrip()
    if not i.startswith('From'):
        continue
    addres_mail = i.split()
    for mail in addres_mail:
        if addres_mail[1] not in counts_email_addres:
            counts_email_addres[addres_mail[1]] = 1
        else:
            counts_email_addres[addres_mail[1]] += 1

print(f'Писем пришло: {counts_email_addres}')
lst_mails = []
for k, v in list(counts_email_addres.items()):
    lst_mails.append((v, k))

lst_mails.sort()
print(f'Меньше всего писем от - {lst_mails[0]},'
      f'больше всего от - {lst_mails[-1]}')
print('-' * 120)
print('УПРАЖНЕНИЕ 2')
print('-' * 120)
file_hour = input('Enter file name: ')
fhand_hour = open(file)
counts_hour = {}

for line in fhand_hour:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    line = line.split()
    if len(line) > 2:
        line = line[5].split(':')
        for i in line:
            if line[0] not in counts_hour:
                counts_hour[line[0]] = 1
            else:
                counts_hour[line[0]] += 1

lst_hour = []
for k, v in list(counts_hour.items()):
    lst_hour.append((k, v))

lst_hour.sort()

print(f'Результат упражнения 2 = {lst_hour}')
print('-_-' * 25)
print('УПРАЖНЕНИЕ 3')
print('-_-' * 25)

fhand_letter = open('romeo-full.txt')
counts_letter = {}
for i in fhand_letter:
    i = i.translate(str.maketrans('', '', string.punctuation))
    i = i.lower()
    text_line = i.split()
    if len(text_line) == 0:
        continue
    for j in text_line:
        for char in j:
            if char not in counts_letter:
                counts_letter[char] = 1
            else:
                counts_letter[char] += 1

lst_char = []

for k, v in list(counts_letter.items()):
    lst_char.append((v, k))

lst_char.sort(reverse=True)

print('Итог упражнения 3 = ', lst_char, len(lst_char))
