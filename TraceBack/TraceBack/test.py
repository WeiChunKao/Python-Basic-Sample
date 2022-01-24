import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.costco.com/')
bs = BeautifulSoup(html, 'lxml')
print(bs.find_all('li'))
os.system('pause')