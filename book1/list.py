l = [1, 2, 5.65, 'Bob', ['apple', '88']] # noqa
print(l)

for i in l:
    print(type(i))

print(f'Длина списка = {len(l)}')

print(l[2])

list1 = [12, 44, 52]
print(list1)
list1[1] = 10

print(list1)

print(10 in list1)

numbers = [2, 4, 6, 8, 10]

for i in range(len(numbers)):
    print('i = ', i)
    numbers[i] = numbers[i] * 2

print(numbers)

print('-' * 50)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(c * 5)
print(c[1:3])

x = ['Denis', 'Max', 'Jana', 'Dasha']
x[1:3] = ['Bob', 'Mark']
print(x)

y = [3, 5, 11]
y.append('j')
print(y)

y = [12, 44, 33]
y2 = ['l', 'we']
y.extend(y2)
print(y)

num = [2, 3, 1, 9, 14]
num.sort()
print(num)
print('Delet elem in list:')
t = ['a', 'b', 'c', 'z', 'd', '23', 88, 96, 105, '0017']
print(t)
d = t.pop(5)
print(d)
print(t)

del t[3]
print(t)
t.remove(88)
print(t)
t.pop()
print(t)
del t[1:3]
print(t)
print('-' * 100)
list2 = [25, 48, 15, 44, 32]
print(len(list2))
print(max(list2))
print(sum(list2))
print(sum(list2)/len(list2))
s = 'spam'
t = list(s)
print(t)
s2 = 'Go to work in Krasty Krabs'
t2 = s2.split()
print(t2)
Mineli = 'ram-pam-pam'
delimetr = '-'
Mineli = Mineli.split(delimetr)
print(Mineli)
jl = ['Krasty', 'Krabs', "cool!", 'burger']
delimetr2 = ' '
print(delimetr2.join(jl))

print('-' * 100)

fhand = open('text.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])
print('-' * 30, 'OBJECT', '-' * 30)

a = 'banana'
b = 'banana'
print(a is b)
print(f'a = {id(a)}, b = {id(b)}, {id(a) == id(b)}')
a_l = [1, 2, 3]
b_l = [1, 2, 3]

print(id(a_l) == id(b_l))
print(id(a_l))
print(id(b_l))

print('-' * 25, 'ПСЕВДОНИМЫ', '-' * 25)

u = [1, 2, 3]
u2 = u
print(u, 'and', u2)
print(u is u2, ',', id(u), '==', id(u2))

print('-' * 100)

li1 = [1, 2]
li2 = li1.append(3)
print(li1)
print(li2)
li3 = li1 + [3]
print(li3)

print('-' * 50, 'Practic', '-' * 50)

input_practic = [1, 2, 3, 4, 5]
input_practic2 = [1, 2, 3, 4, 5]


def chop(input_practic):
    input_practic.pop(0)
    del input_practic[-1]
    return None


def middle(input_practic2):
    return input_practic2[1:-1]


print(chop(input_practic))
print(middle(input_practic2))

print('-' * 30, 'ОТЛАДКА!!!', '-' * 30)

li4 = [1, 2, 6, 4, 9, 11, 3, 12]
print(li4)
li4.sort()
print(li4)
print('-' * 100)
original_list = [1, 10, 100, 10000, 1000000]
copy_list = original_list[:]
print(f'Original = {original_list}, copy = {copy_list}')
copy_list.append(25)
copy_list.append(15)
copy_list.append(128)
copy_list.sort()
print(f'Original = {original_list}, copy = {copy_list}')
print('-' * 30, 'Debugging', '-' * 30)

fhand_debug = open('text.txt')
for i in fhand_debug:
    words2 = i.split()
    # print('Debug: ', words2)
    if len(words2) == 0 or words2[0] != 'From':
        continue
    else:
        print(words2[2])

print('-' * 50, 'P R A C T I C', '-' * 50)

romeo = open('romeo.txt')
itog = []

for line_romeo in romeo:
    result = []
    line_romeo = line_romeo.rstrip()
    split_romeo = line_romeo.split()
    for i in split_romeo:
        if split_romeo.count(i) == 1:
            result.append(i)
    itog.extend(result)

sorted_res = list(set(itog))

print('RESULT = ', sorted(sorted_res))

print('-' * 15, 'УПРАЖНЕНИЕ 5!   ' * 5, '-' * 15)

mail = open('text.txt')
count_mail = 0

for line_mail in mail:
    if not line_mail.startswith('From '):
        continue
    words_mail = line_mail.split()
    print(words_mail[1])
    count_mail = count_mail + 1

print(f'There were {count_mail} lines in the file with '
      'From as the first word.')
print('_' * 100)
print('-' * 15, 'УПРАЖНЕНИЕ 6!   ' * 5, '-' * 15)
numbers_list = []
while True:
    num_list = input('Enter number: ')
    if num_list == 'Done':
        break
    numbers_list.append(num_list)
print(f'Миниимальное число: {float(min(numbers_list))},'
      f'Максимальное: {float(max(numbers_list))}')
