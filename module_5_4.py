def assert_integer(value):
    assert isinstance(value, int), f'Value must be integer, not {type(value)}'


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, n_of_floors):
        self.name = name
        self.number_of_floors = n_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __add__(self, value):
        assert_integer(value)
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        assert_integer(value)
        self.number_of_floors -= value
        return self

    def __isub__(self, value):
        return self.__sub__(value)

    def __rsub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        assert_integer(value)
        self.number_of_floors *= value
        return self

    def __imul__(self, value):
        return self.__mul__(value)

    def __rmul__(self, value):
        return self.__mul__(value)

    def __floordiv__(self, value):
        assert_integer(value)
        self.number_of_floors //= value
        return self

    def __truediv__(self, value):
        return self.__floordiv__(value)

    def go_to(self, new_floor):
        assert new_floor == int(new_floor), 'Этаж должен быть целым числом.'
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)

