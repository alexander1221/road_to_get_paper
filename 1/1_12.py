mode = input("Введите вариант (a, b или c): ")

if mode == 'a':
    data = ['5 10', '7 см']
    for i in data: print(i)
elif mode == 'b':
    t = int(input('Введите значение переменной t: '))
    v = int(input('Введите значение переменной v: '))
    data = [[100, t], [1949, v]]
    for i in data: print(" ".join([str(x) for x in i]))
elif mode == 'c':
    x = int(input('Введите значение переменной x: '))
    y = int(input('Введите значение переменной y: '))
    data = [[x, 25], [x, y]]
    for i in data: print(" ".join([str(x) for x in i]))
