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
    print(f'd_dic.items() = {d_dic.items()}')
    print(f'k = {k}, v = {v}')
    l_dic.append((v, k))
    print(f'l_dic = {l_dic}')
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
