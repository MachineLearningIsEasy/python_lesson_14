import re

string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

#pattern = r'It'

# findall-------------------------------
#print(len(re.findall(pattern, string)))

# [  ]----------------------------------

#pattern = r'[ab]'
#pattern = r'[a-zA-Z0-9]'
#pattern = r'[,]'

#print(len(re.findall(pattern, string)))

# (.)----------------------------------
#pattern = r'[w]..'
#print(re.findall(pattern, string))

# Поиск специальных символов----------

# \w - все, кроме спец знаков
# \W - все спец знаки

# \d - любая цифра
# \D - не цифра

# pattern = r'\D'
# print(re.findall(pattern, string))

# Поиск определенного количества заданных символов

# \d{n} - ровно n раз
# \d{n,} - более n раз
# \d{n,m} - не менее n цифр, но не более m


#pattern = r'\W\w{2,4}\W' # - поиск слов заданной длины
#print(re.findall(pattern, string))


# search ---------------------------
# pattern = r'\W\w{2,4}\W'
# print(re.search(pattern, string))

# sub ------------------------------

pattern = r'\W\w{2,4}\W' # - поиск слов заданной длины
print(re.sub(pattern,r' ', string))