def foo(a: int = None, b: int = None):
    # if a is None:
    #     pass

    # if isinstance(a, int):

    assert a
    assert b


try:
    foo()
except Exception:
    print("anything")
