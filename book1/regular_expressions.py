import re

print("Регулярные выражения.")
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From', line):
        print(line)

print('-' * 120)

hand2 = open('mbox-short.txt')
for i in hand2:
    i = i.rstrip()
    if re.search('^Message-ID:', i):
        print(i)

print('-' * 120)

hand3 = open('mbox-short.txt')
for i in hand3:
    i = i.rstrip()
    if re.search('^F..m', i):
        print(i)

print('-' * 120)

hand4 = open('mbox-short.txt')
for i in hand4:
    i = i.rstrip()
    if re.search('^From:.+@', i):
        print(i)

print('-' * 30, 'Findall', '-' * 30)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2pm'
lst = re.findall('\S+@\S+', s)
print(lst)

hand5 = open('mbox-short.txt')
for i in hand5:
    i = i.rstrip()
    x = re.findall('\S+@\S+', i)
    if len(x) > 0 :
        print(x)

hand6 = open('mbox-short.txt')
for i in hand6:
    i = i.rstrip()
    x2 = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', i)
    if len(x2) > 0:
        print(x2)

print('-' * 25, 'ОБЪЕДИНЕНИЕ ПОИСКА И ИЗВЛЕЧЕНИЯ', '-' * 25)

hand7 = open('mbox-short.txt')
for i in hand7:
    i = i.rstrip()
    if re.search('^X\S*: [0-9.]+', i):
        print(i)

hand8 = open('mbox-short.txt')
for i in hand8:
    i = i.rstrip()
    x_i = re.findall('^X\S*: ([0-9.]+)', i)
    if len(x_i) > 0:
        print(x_i)

print('hand9')
hand9 = open('mbox-short.txt')
for i in hand9:
    i = i.rstrip()
    x2_i = re.findall('^Details:.*rev=([0-9.]+)', i)
    if len(x2_i) > 0:
        print(x2_i)

print('hand10')
hand10 = open('mbox-short.txt')
for i in hand10:
    i = i.rstrip()
    x2_i = re.findall('^From .* ([0-9][0-9]):', i)
    if len(x2_i) > 0:
        print(x2_i)

print('СПЕЦИАЛЬНЫЙ СИМВОЛ ЭКРАНИРОВАНИЯ')
l_str = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', l_str)
print(y, type(y))
