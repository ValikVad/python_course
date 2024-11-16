# Определяем базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Я животное"


# Определяем подкласс Dog, который наследует класс Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"


# Определяем подкласс Cat, который также наследует класс Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"


# Создаем экземпляры классов
dog = Dog("Бобик")
cat = Cat("Мурка")

# Вызов методов speak
print(dog.speak())  # Вывод: Бобик говорит: Гав!
print(cat.speak())  # Вывод: Мурка говорит: Мяу!
