class MyCustomError(Exception):
    pass


def my_function():
    raise MyCustomError("Это собственное исключение")


try:
    my_function()
except MyCustomError as e:
    print(f"Произошло исключение: {e}")
