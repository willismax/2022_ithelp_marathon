def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_demo():
    assert 1 + 1 == 2


def test_demo_2():
    assert 2 + 2 == 4
