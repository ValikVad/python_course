import threading
import time

import requests


def activity():
    for i in range(1000000):
        abs(round(i**2 / 122) + i * 3.14)


def activity1():
    requests.get("https://www.google.com")


def run(thread=False):
    start = time.time()
    if not thread:
        for j in range(10):
            activity()

    else:
        threads = [threading.Thread(target=activity1, daemon=True) for _ in range(10)]
        for j in threads:
            j.start()
        for j in threads:
            j.join()

    end = time.time()
    print(f"Time: {end - start} seconds")


if __name__ == "__main__":
    run(thread=True)
