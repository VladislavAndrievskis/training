class MushroomsCollector:

    def __init__(self):
        self.mushrooms = []

    def is_poisonous(self, name):
        if name == 'Мухомор' or name == 'Поганка':
            return True
        else:
            return False

    def add_mushroom(self, name):
        if self.is_poisonous(name):
            print('Нельзя добавить ядовитый гриб')
        else:
            self.mushrooms.append(name)

    def __str__(self):
        return ', '.join(self.mushrooms)


collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
collector_2.add_mushroom('Поганка')
print(collector_1)
print(collector_2)
