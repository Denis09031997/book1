import re

print('Упражнения, регулярные выражения')

re_command = input('Enter a regular expression: ')
fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(f'{re_command}', line):
        count = count + 1

print('Result = ', count)

print('-' * 120)

fhand2 = open('mbox.txt')

l_num = []
for i in fhand2:
    i = i.rstrip()
    x = re.findall('^New Revision\S*: ([0-9.]+)', i)
    if len(x) > 0:
        l_num.append(int(x[0]))

print(f'Result = {int(sum(l_num) / len(l_num))}')
