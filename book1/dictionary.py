import string

dictionary = {}
print(dictionary, type(dictionary))
dictionary['auto'] = 'KIA'
print(dictionary)
dictionary = {
    'auto': 'KIA',
    'age': 26,
    'work': 'Alfa Group',
    'Courses': 'Python',
    }
print(dictionary)
print(dictionary['work'])
print(len(dictionary))
print('KIA' in dictionary)
print('age' in dictionary)
vals_dictionary = list(dictionary.values())
print(vals_dictionary)
key_dictionary = list(dictionary.keys())
print(key_dictionary)
print('-' * 100)
dict_file = open('txt_dict.txt')

dict_txt = {}

for line in dict_file:
    key = line.split()
    for i in key:
        dict_txt[i] = 'значение'

print(dict_txt)
print('care' in dict_txt)
print('car' in dict_txt)
print('vasts' in dict_txt)
print('Bob' in dict_txt)
print('_' * 100)

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

print(d)
print(d.get('w', 'uuups'))
# Посчитаем сколько раз встречается слово в отрывке Шекспира.
fname = open('romeo.txt')
counts = dict()
for l in fname:
    words = l.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
print('-' * 100)
counts2 = {
    'Any': 28,
    'Denis': 26,
    'Max': 27,
    'Jana': 24,
    'Nadya': 22,
}

for key in counts2:
    print(f'key = {key}, counts2[key] = {counts2[key]}')

print(counts2.keys())
print(counts2.values())

# Выведем в алфовитном порядке:

counts3 = {
    'Any': 28,
    'Denis': 26,
    'Max': 27,
    'Zaliya': 45,
    'Jana': 24,
    'Nadya': 22,
}

lst = list(counts3.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts3[key])

print('-' * 100)

fname_punctuation = open('romeo_text2.txt')
counts_punctuation = dict()
for line in fname_punctuation:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words2 = line.split()
    for word in words2:
        if word not in counts_punctuation:
            counts_punctuation[word] = 1
        else:
            counts_punctuation[word] += 1

print(counts_punctuation)
print('-' * 25, 'P R A C T I C', '-' * 25)
fhand_mails = open('text.txt')
result_days_mails = {}

for line in fhand_mails:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    word_mail = line.split()
    for i in word_mail:
        if word_mail[2] not in result_days_mails:
            result_days_mails[word_mail[2]] = 1
        else:
            result_days_mails[word_mail[2]] += 1

print(result_days_mails)
print('-' * 25, 'УПРАЖНЕНИЕ 3', '-' * 25)
fhand_email_addres = open('text.txt')
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
print('-' * 25, 'УПРАЖНЕНИЕ 4', '-' * 25)

print(counts_email_addres)
counts_write = 0
counts_autor = ''
for i in counts_email_addres:
    if counts_email_addres[i] > counts_write:
        counts_write = counts_email_addres[i]
        counts_autor = i
print('Result =', counts_autor, counts_write)
print('-' * 25, 'УПРАЖНЕНИЕ 5', '-' * 25)
fhand_domen = open('text.txt')
count_doments = 0
domen = {}
for i in fhand_domen:
    i = i.rstrip()
    if not i.startswith('From'):
        continue
    domen_list = i.split()
    for j in domen_list:
        if '@' not in j:
            continue
        index = j.index('@')
        if domen_list[1][index + 1:] not in domen:
            domen[domen_list[1][index + 1:]] = 1
        else:
            domen[domen_list[1][index + 1:]] += 1

print(f'Итог 5го упражнения:{domen}')
