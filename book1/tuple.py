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
