import math

TYPES_C0NTAINERS = (list, tuple, set)
TYPES_NUMBERS = (int, float, complex)


def is_number(value):
    return type(value) in TYPES_NUMBERS


def is_container(value):
    return type(value) in TYPES_C0NTAINERS


class Figure:
    def __init__(self, color=None, sides=None, filled=None, sides_count=0):

        self.__color = None
        self.__filled = None
        self.__sides_count = int(max(0, sides_count))
        self.__sides = sides

        self.__set_color_initial(color)
        self.__set_filled(filled)
        self.__set_sides_initial(sides)

    def __len__(self):
        if is_container(self.__sides):
            return sum(self.__sides)
        elif is_number(self.__sides):
            return self.__sides * self.__sides_count

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and r == int(r) and g == int(g) and b == int(b)

    def __set_color_initial(self, color):
        if is_number(color) and 0 <= color <= 255:
            self.__color = [color, color, color]
        elif is_container(color) and len(color) == 3:
            self.set_color(color[0], color[1], color[2])
        else:
            self.__color = None

    def __set_filled(self, filled):
        if filled is not None:
            assert isinstance(filled, bool), 'filled atribute must be boolean'
            self.filled = filled

    def __is_valid_sides(self, *sides):
        return (len(sides) == self.__sides_count and all(side > 0 and side == int(side) for side in sides)) or (len(sides) == 1 and sides[0] > 0)

    def __set_sides_initial(self, sides):
        if is_container(sides) and self.__is_valid_sides(sides):
            self.__sides = list(sides)
        elif is_number(sides) and sides > 0:
            self.__sides = sides
        else:
            self.__sides = 1

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = sides if len(sides) > 1 else sides[0]


class Circle(Figure):
    def __init__(self, color=None, side=None, filled=None):
        self.__color = color
        self.__sides = side
        self.__filled = filled
        super().__init__(self.__color, self.__sides, self.__filled, 1)
        self.__radius = None if side is None else side / 2.0 / math.pi

    def get_square(self):
        return 2.0 * math.pi * self.__radius * self.__radius if self.__radius is not None else None


class Triangle(Figure):
    def __init__(self, color=None, sides=None, filled=None):
        self.__color = color
        self.__sides = sides
        self.__filled = filled
        super().__init__(self.__color, self.__sides, self.__filled, 3)
        if self.__is_possible() is False:
            self.__sides = 1
        self.__height = max(self.get_heights())

    def __is_possible(self):
        if self.__sides[0] > self.__sides[1] + self.__sides[2]:
            return False
        if self.__sides[1] > self.__sides[0] + self.__sides[2]:
            return False
        if self.__sides[2] > self.__sides[0] + self.__sides[1]:
            return False
        return True

    def get_square(self):
        if is_container(self.__sides):
            return math.sqrt(self.__len__() * (self.__len__() - self.__sides[0]) * (self.__len__() - self.__sides[1]) * (self.__len__() - self.__sides[2]))
        elif is_number(self.__sides):
            return math.sqrt(3.0) * self.__sides * self.__sides / 4.0
        else:
            TypeError()

    def get_heights(self):
        square = self.get_square()
        if is_container(self.__sides):
            return (2.0 * square / side for side in self.__sides)
        elif is_number(self.__sides):
            value = 2.0 * square / self.__sides
            return value, value, value
        else:
            TypeError()

    def set_sides(self, *sides):
        super().set_sides(sides)
        self.__height = max(self.get_heights())


class Cube(Figure):
    def __init__(self, color=None, sides=None, filled=None):
        self.__color = color
        self.__sides = sides
        self.__filled = filled
        super().__init__(self.__color, self.__sides, self.__filled, 12)

    def get_volume(self):
        if is_number(self.__sides):
            return self.__sides * self.__sides * self.__sides
        elif is_container(self.__sides):
            return self.__sides[0] * self.__sides[0] * self.__sides[0]


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
