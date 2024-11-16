import logging

logging.basicConfig(level=logging.WARNING)


class SomeExcept1(Exception):
    pass


class SomeExcept2(Exception):
    pass


def main():
    try:
        pass
    except SomeExcept1:
        print()

    try:
        pass
    except SomeExcept2:
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print()
        logging.warning()
