"""
Дан список слов: ['snow', 'rain', 'wind', 'sun', ''clouds].
Проверьте, есть ли среди них хотя бы одно слово с длиной менее 4-х символов.
Выведите соответствующее сообщение на экран.
Решите эту задачу для случая, когда нужно найти хотя бы 2 таких случая.
"""

l=['snow', 'rain', 'a', 'wind', 'sun', 'clouds']
#only 1 word

for elem in l:
    if len(elem)<4:
        print('yes')
        break
else:
    print('No')

#only 2 words
count=0
for elem in l:
    if len(elem)<4:
        count+=1
    if count==2:
        print('yes')
        break
else:
    print('No')






