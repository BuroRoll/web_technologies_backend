class Rectangle:
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width


if __name__ == '__main__':
    w = float(input('Введите ширину прямоугольника: '))
    h = float(input('Введите высоту прямоугольника: '))
    rectangle = Rectangle(width=w, height=h)
    print(f'Площадь прямоугольника равна {rectangle.calculate_area()}')
