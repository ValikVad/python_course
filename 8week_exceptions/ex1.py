import logging

logging.basicConfig(level=logging.WARNING)

try:
    x = 1 / 0  # Попытка деления на ноль
except ZeroDivisionError as e:
    logging.warning(
        f"""Произошло исключение: __context__ = {e.__context__}\n Произошло исключение: __cause__ = {e.__cause__}\nПроизошло исключение: __suppress_context__ = {e.__suppress_context__}\n"""
    )
