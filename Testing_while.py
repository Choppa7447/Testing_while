i = 1000
while i > 100:
    print(i)
    i /= 2

for j in 'hello world':
    if j == 'w':
        break
    print(j * 2, end = '')

for j in '\nhello world':
    if j == 'a':
        break
    print(j * 3, end = '')
else:
    print('\nБуквы A нет в слове')