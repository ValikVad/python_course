try:
    x = int(input("Введите число: "))
    y = 10 / x
except (ZeroDivisionError, ValueError) as e:
    print(f"Произошло исключение: {e}")
