import socket
import time
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import re
import ssl
from bs4 import BeautifulSoup

print('Приступаем к изучению протокола HTTP')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
print('-' * 120)

HOST = 'data.pr4e.org'
PORT = 80
mysock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock2.connect((HOST, PORT))
mysock2.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b''
while True:
    data = mysock2.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock2.close()

pos = picture.find(b'\r\n\r\n')
print('Header lenght', pos)
print(picture[:pos].decode())
picture = picture[pos+4:]
fhand = open('stuff.jpg', 'wb')
fhand.write(picture)
fhand.close()
print('_' * 120)
print('Извлечение ВЕБ-страниц с помощью библиотеки URLLIB')
print('_' * 120)

fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for i in fhand2:
    print(i.decode().strip())

print('-' * 120)
fhand3 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for i in fhand3:
    words = i.decode().split()
    for j in words:
        counts[j] = counts.get(j, 0) + 1
print(counts)

print('Чтение двоичных файлов с использованием библиотеки urllib')

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand4 = open('cover3.jpg', 'wb')
fhand4.write(img)
fhand4.close()

print('-' * 120)

img2 = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fh = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img2.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fh.write(info)

print(size, 'characters copied.')
fh.close()
print('-' * 120)
print('Использование регулярных выражений.')
print('-' * 120)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for i in links:
    print(i.decode())

print('-' * 120)
print('BEAUTIFUL SOUP')
print('-' * 120)

ctx2 = ssl.create_default_context()
ctx2.check_hostname = False
ctx2.verify_mode = ssl.CERT_NONE

url2 = input('Enter - ')
html2 = urllib.request.urlopen(url2, context=ctx2).read()
soup = BeautifulSoup(html2, 'html.parser')

tags = soup('a')
for i in tags:
    print(i.get('href', None))

print('-' * 200)

