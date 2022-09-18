def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_demo():
    assert 1 + 1 == 2


def test_demo_2():
    assert 2 + 2 == 4
