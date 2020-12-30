# conftest.py 用法
#   conftest.py配置需要注意:
#       conftest.py文件名是不能换的
#       conftest.py与运行的用例要在同一个package下，并且有__init__.py文件
#       不需要import导入conftest.py，pytest用例会自动查找
#       所有同目录测试文件运行前都会执行conftest.py文件
#       全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方。
#       如果项目的不同目录下有相同名字的conftest.py 文件，里面有相同名字的fixture, 测试用例里面调用的fixture方法，会使用离这个文件最近的一层目录下的conftest.py里面的fixture方法
import pytest
import yaml

from pythoncode.calculator import Calculator
from pythoncode.search_rotated_list import Solution


@pytest.fixture(scope="function", params=["tom", "jerry"])
def login(request):
    print("登陆操作")
    username = request.param
    # yield ["tom", '123456']
    yield username
    print("登出操作")


@pytest.fixture()
def connect_db():
    print("完成数据库连接")
    yield "db connected"


@pytest.fixture(scope="module")
def get_calc():
    print("计算开始")
    yield Calculator()
    print("计算结束")


@pytest.fixture(scope='module')
def get_function():
    solution = Solution()
    yield solution
    print('test end')
