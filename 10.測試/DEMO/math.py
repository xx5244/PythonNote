def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError('a和b必須是整數')
