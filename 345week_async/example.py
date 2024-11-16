import time


def foo1(x):
    print(x**2)
    time.sleep(3)
    print("foo1 завершена")


def foo2(x):
    print(x**0.5)
    time.sleep(3)
    print("foo2 завершена")


# def main():
#     foo1(4)
#     foo2(4)


# print(f"start time = {time.strftime('%X')}")

# main()

# print(f"finish time = {time.strftime('%X')}")


print(type(foo1))
print(type(foo1(4)))
