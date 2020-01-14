from bs4 import BeautifulSoup
import requests
#from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import re

# response = requests.get('url', auth = HTTPBasicAuth('ypur_login', 'your_password'))

URL = 'https://www.drom.ru/reviews/volvo/v40/5kopeek/'

page = requests.get(URL)

print(page.status_code)
#print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')


reviews = soup.find_all('div', class_ = 'b-fix-wordwrap')

print(len(reviews))




# поиск тегов по классу
rev_plus = []
rev_minus = []
i = 0
for rev in reviews:
    if i%3 == 0:
        rev_plus.append(rev.text)
        i+=1
    elif i%3 == 1:
        rev_minus.append(rev.text)
        i+=1
    else:
        i+=1
print(rev_plus)


# иерархия

parts = soup.find('div', class_ = 'b-wrapper')

print(len(parts.contents))

for part in parts.contents:
    print('--------------------------------------------')
    #print(part)
    try:
        print(len(part.contents))
    except:
        print('Error')

print('ANOTHER EXAPLE')

URL_ ='https://auto.ria.com/reviews/volvo/v40/'

page_ = requests.get(URL_)
print(page_.status_code)


soup_ = BeautifulSoup(page_.text, 'html.parser')

reviews_ = soup_.find_all('div', class_='reviews-car-cardi-top')


for rev in reviews_ :
    print(rev.text)
