from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx3 = ssl.create_default_context()
ctx3.check_hostname = False
ctx3.verify_mode = ssl.CERT_NONE

url_free = input('Enter url- ')
html3 = urlopen(url_free, context=ctx3).read()
soup2 = BeautifulSoup(html3, 'html.parser')

tags2 = soup2('a')
for i in tags2:
    print('TAG - ', i)
    print('URL: ', i.get('href', None))
    print('Contents = ', i.contents[0])
    print('Attrs: ', i.attrs)
