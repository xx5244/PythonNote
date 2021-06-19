# module 練習

def my_sum(*args):
    result = 0
    for item in args:
        result += item

    return result


def my_max(*args):
    print('最大值')


def my_min(*args):
    print('最小值')


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
