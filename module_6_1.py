class Animal:
    """Класс животного"""
    alive = True
    fed = False

    def __init__(self, name):  # метод инициализации атрибутов класса
        self.name = name

    def eat(self, food):  # метод проверяющий съедобная еда(food) или нет
        self.food = food
        if isinstance(food, Plant):  # isinstance проверяет: является ли объект класса Plant
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True #смена атрибута False на True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False #смена атрибута True на False


class Plant:
    """Класс растений"""
    edible = False  # растение не съедобное

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    """Класс млекопитающего - дочерний класс животного"""
    pass


class Predator(Animal):
    """Класс хищник - дочерний класс животного"""
    pass


class Flower(Plant):
    """Класс цветов - дочерний класс растения"""
    pass


class Fruit(Plant):
    """Класс фрукты - дочерний класс растения"""

    def __init__(self, name):
        super().__init__(name)  # функция super() вызывает конструктор родительского класса
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
