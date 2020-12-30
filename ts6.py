def Title_func(s):
    return(s.title())
while True:
    s = input('Введите слова, Enter - завершить:')
    if s == '':
        break
    print(Title_func(s))
