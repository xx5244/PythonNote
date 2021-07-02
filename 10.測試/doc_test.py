def func_demo(a, b):
    """
    >>> func_demo(1, 2)
    3
    >>> func_demo('a', 'b')
    'ab'
    >>> func_demo([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> func_demo(1, '3')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> func_demo({1:1}, {2:2})
    False
    """
    if isinstance(a, dict):
        return False
    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""
如果輸入參數a不是字典的話，那isinstance(a, dict)裡面的程式就不會被測試到，測試覆蓋率也不會是100%
要測試的指令要用註解包住
寫法等同於在python底下直接輸入指令寫法，下面一行要緊跟著期望的結果
執行的時候是原本的執行程式後面加個 -v
例如:python tt.py -v
資訊會顯示測試幾項，幾項成功，幾項失敗
"""
