class MyClass:
    def __init__(self):
        self._protected_attr = "Я защищённый атрибут"
        self.__private_attr = "Я приватный атрибут"

    def get_private_attr(self):
        return self.__private_attr

    @property
    def attr(self):
        return self.__private_attr

    @attr.setter
    def attr(self, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        self.__private_attr = value
