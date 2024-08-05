class House:
    def __init__(self, name, n_of_floors):
        self.name = name
        self.number_of_floors = n_of_floors


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def go_to(self, new_floor):
        assert new_floor == int(new_floor), 'Этаж должен быть целым числом.'
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))