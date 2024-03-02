import math


def solve_quadratic_equation(a: int, b: int, c: int) -> (float, float):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


if __name__ == '__main__':
    a = int(input('Введите коэфициент a: '))
    b = int(input('Введите коэфициент b: '))
    c = int(input('Введите коэфициент c: '))
    result = solve_quadratic_equation(a, b, c)
    print(f'Решение уравнения: {result}')
