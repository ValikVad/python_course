import multiprocessing
import time

import requests


def worker():
    name = 1
    print(f"Процесс {name} запущен.")
    for i in range(10_000_000):
        abs(round(i**2 / 122) + i * 3.14)

    # requests.get("https://ya.ru")
    #     print("OK")

    print(f"Процесс {name} завершён.")


if __name__ == "__main__":
    const = 4
    processes = []
    start = time.time()
    for i in range(const):
        p = multiprocessing.Process(target=lambda: worker, daemon=True)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Time computing {time.time() - start} sec")
    print("Все процессы завершены.")
