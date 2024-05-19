if __name__ == '__main__':
    try:
        value = int(input("Введите число и я определю четное оно или нет: "))
    except ValueError:
        print('Введено не число')
        exit(1)
    if value % 2 == 0:
        print(f'Число {value} четное')
    else:
        print(f'Число {value} нечетное')


print('test')
