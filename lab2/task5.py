import math


class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    r = float(input('Введите радиус круга: '))
    circle = Circle(radius=r)
    print(f'Площадь круга равна: {circle.get_area()}')
    print(f'Периметр круга равен: {circle.get_perimeter()}')
