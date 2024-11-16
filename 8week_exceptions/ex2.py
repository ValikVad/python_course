a = int(input())
b = int(input())

try:
    x = a / b
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print(f"Результат: {x}")
