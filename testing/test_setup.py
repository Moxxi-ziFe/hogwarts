def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


def setup_function():
    print("setup function")


def teardown_function():
    print("teardown function")


def test_func():
    print("test function")


class TestDemo:
    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_case1(self):
        print("test case1")

    def test_case2(self):
        print("test case2")
