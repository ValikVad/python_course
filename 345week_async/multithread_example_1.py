import threading


def print_numbers():
    for i in range(1, 6):
        print(i)


# Создаем поток

thread = threading.Thread(target=print_numbers)

# Запускаем поток

thread.start()

# Ждем завершения потока

thread.join()
