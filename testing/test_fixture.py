import pytest


# 如果测试用例里，需要用到fixture的返回值 的话，fixture的名字需要以参数的形式传入到方法里，不能使用装饰器的方式。
# @pytest.fixture(autouse=True, scope="function")
# def login():
#     print("登陆操作")
#     yield ["tom", '123456']
#     print("登出操作")
#
#
# @pytest.fixture()
# def connect_db():
#     print("完成数据库连接")
#     yield "db connected"


@pytest.mark.usefixtures("login")
def test_case1():
    # print(login)
    print("case1")


def test_case2(login):
    print(login)
    print("case2")


def test_case3(connect_db):
    print(connect_db)
    print("case3")
