file = open("data.txt", "r")
data = file.read()


try:
    a = 2
    x = 1 / 0
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
finally:
    print(data, a)
    file.close()  # Закрытие файла независимо от успешности операций


# db_session = db.session_open()

# try:
#     db_session.write()
# except DB_Exception:
#     print()
# finally:
#     db_session.close()
