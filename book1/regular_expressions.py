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
