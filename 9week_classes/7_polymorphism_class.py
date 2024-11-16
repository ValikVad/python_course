from abc import ABC, abstractmethod


# Определяем абстрактный класс
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Подклассы, реализующие абстрактный метод speak
class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class Cow(Animal):
    def speak(self):
        return "Му!"


# Функция для использования полиморфизма
def animal_sound(animal):
    print(animal.speak())


# Создаем экземпляры классов
dog = Dog()
cat = Cat()
cow = Cow()

# Вызов функции с различными объектами
animal_sound(dog)  # Вывод: Гав!
animal_sound(cat)  # Вывод: Мяу!
animal_sound(cow)  # Вывод: Му!
