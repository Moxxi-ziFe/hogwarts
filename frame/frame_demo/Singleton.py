# 单例, 无需传递driver, 利用组合, 无需继承BasePage
# note. 单例模式, 代理模式
def singleton(func):
    _instance = {}

    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)
        return _instance[func]

    return wrapper
