class Dog:
    def __init__(self, name, age):
        self.name = name  # Атрибут имени
        self.age = age  # Атрибут возраста

    def bark(self):
        """Метод, который заставляет собаку лаять"""
        return f"{self.name} говорит: Гав!"


# Создание экземпляра класса
my_dog = Dog("Buddy", 3)

# Вызов метода и доступ к атрибутам
print(my_dog.bark())  # Вывод: Buddy говорит: Гав!
print(f"Собака зовут: {my_dog.name}")  # Вывод: Собака зовут: Buddy
print(f"Возраст собаки: {my_dog.age} лет")  # Вывод: Возраст собаки: 3 лет
