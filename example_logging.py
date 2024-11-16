import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
verbose = "info"

a = input("Введи число:")

logging.info(f"Пользователь ввел число {a}")

if verbose == "info":
    print(f"Пользователь ввел число {a}")

sum_value = a**2

logging.debug(f"ф**2 = {sum_value}")


"""
Levels:
    1) INFO
    2) DEBUG
    3) WARNING
    ...
"""
