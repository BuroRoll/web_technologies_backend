def find_max_value(numbers: list) -> int:
    if not numbers:
        return None

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value


if __name__ == '__main__':
    numbers: list = list(map(int, input("Введите числа через пробел: ").split()))
    result = find_max_value(numbers)
    print(f'Максимальное значение массива: {result}')
