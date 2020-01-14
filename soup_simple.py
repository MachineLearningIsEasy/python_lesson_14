# http://wiki.python.su/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8/BeautifulSoup
# документация
from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.drom.ru/reviews/volvo/v40/5kopeek/'

page = requests.get(URL)

print(page.status_code)
print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
print(type(soup))

print(soup.title)                                  # вернет объект с первым тегом soup.teg
print(soup.title.string, type (soup.title.string)) # возвращается строка со спец возможностями
print(soup.title.text, type (soup.title.text))     # возвращается строка


# Получим все ссылки данной html-страницы

print(soup.a)
print(soup.a.text)                                      # содержит то, что между тегами
print(soup.a.get('href'), type(soup.a.get('href')))     # обращение к атрибуту тега

  # find_all
a_tags = soup.find_all('a')
print(type(a_tags))
print(len(a_tags))

for ref in a_tags:
      print(ref.get('href'))

# Решим эту же задачу с помощью регулярных выражений

pattern = r'https?://[\S]+'

ref_all = re.findall(pattern, page.text)

print(len(ref_all))

for ref in ref_all:
      print(ref)



div_tags = soup.find_all('div')

print(len(div_tags))