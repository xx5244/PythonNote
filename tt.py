def test():
    return 1, 2, 3

a, b, c = test()
print(a, b, c)

d, _, _ = test()
print(d)