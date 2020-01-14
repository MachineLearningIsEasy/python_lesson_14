import re

text = "100 ИНФ 8(903)6174741 Информатика abc@mail +7(903)6174731 213 МАТ abc@.mail.ru 1.1.91 1\\12\\1991 89036174739 1.1.1991 Математика 1.11.1991 +79036174740  1/12/1991 cnn@gmail.com 21.01.1991 156 АНГ  Английский 89036174738 nn@gmail.com"

# шаблон для даты


# шаблон для номеров телефонов

pattern = r'\S{1,2}\S?\d{3}\S?\d{7}' # символ? - символ может быть, а может нет
#print(re.findall(pattern, text))

# шаблон для email
#pattern = r'\S+[@][a-z]\S+[.]\S+'
#print(re.findall(pattern, text))

# pattern = r'\d{1,2}[./\\]\d{1,2}[./\\]\d{2,4}'
# print(re.findall(pattern, text))


# Фильтрация даных
telephone_numbers = ['8(903)6174741','+7(903)6174731','cnn@gmail.com','89036174739','+79036174740','89036174738', '+7903617473745','asd@mail.ru']

for num in telephone_numbers:
    print(num, re.match(pattern,num))