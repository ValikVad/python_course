class Person:
    def __init__(self, name):
        self._name = name  # защищённый атрибут

    # @property
    # def name(self):
    #     """Получение имени"""
    #     return self._name

    # @name.setter
    # def name(self, new_name):
    #     """Установка имени"""
    #     if not new_name:
    #         raise ValueError("Имя не может быть пустым")
    #     self._name = new_name

    # @name.deleter
    # def name(self):
    #     """Удаление имени"""
    #     del self._name


# защищённый атрибут не защищен от изменений
person = Person("Alice")
print(person._name)  # Вывод: Alice
person._name = "Bob"
print(person._name)  # Вывод: Bob


# person.name = "Bob"  # Устанавливаем новое имя
# print(person.name)  # Вывод: Bob

# try:
#     person.name = ""  # Попытка установить пустое имя
# except ValueError as e:
#     print(e)  # Вывод: Имя не может быть пустым

# del person.name  # Удаляем имя
