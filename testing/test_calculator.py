import pytest
import yaml
import allure


# from pythoncode.calculator import Calculator


def get_data(file_name):
    with open(file_name) as f:
        test_data = yaml.safe_load(f)
        return test_data


# @pytest.fixture(scope="class")
# def get_calc():
#     print("计算开始")
#     yield Calculator()
#     print("计算结束")

@allure.feature("计算器")
class TestCalculator:

    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize("a,b,expect", [
    #     [1, 1, 2],
    #     [100, 100, 200],
    #     [0.1, 0.1, 0.2],
    #     [-1, -1, -2],
    #     [0, 1, 1]
    # ], ids=["int_case",
    #         "big_num_case",
    #         "float_case",
    #         "minus_case",
    #         "zero_case"
    #         ])
    @allure.story("加法")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", get_data("../Datas/datas.yml")["add"]["datas"],
                             ids=get_data("../Datas/datas.yml")["add"]["ids"])
    def test_add(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = round(get_calc.add(a, b), 3)
        assert result == expect

    @allure.story("减法")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_data("../Datas/datas.yml")["sub"]["datas"],
                             ids=get_data("../Datas/datas.yml")["sub"]["ids"])
    def test_sub(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.sub(1, 1)
        result = round(get_calc.sub(a, b), 3)
        assert result == expect

    @allure.story("乘法")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_data("../Datas/datas.yml")["mul"]["datas"],
                             ids=get_data("../Datas/datas.yml")["mul"]["ids"])
    def test_mul(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.mul(1, 1)
        result = round(get_calc.mul(a, b), 3)
        assert result == expect

    # @pytest.mark.parametrize("a,b", [
    #     [1, 0],
    #     [0.1, 0],
    #     [0, 0]
    # ])
    @allure.story("除法")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_data("../Datas/datas.yml")["div"]["datas"],
                             ids=get_data("../Datas/datas.yml")["div"]["ids"])
    def test_div_zero(self, get_calc, a, b, expect):
        # with pytest.raises(ZeroDivisionError):
        #     get_calc.div(a, b)
        try:
            result = round(get_calc.div(a, b), 3)
            assert result == expect
        except ZeroDivisionError:
            print("Divide by zero")
