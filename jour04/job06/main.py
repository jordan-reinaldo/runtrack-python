def list():
    L= [10, 20, 30, 40, 50]
    return L
print(list())


def list():
    L= [10, 20, 30, 40, 50]
    L[0], L[-1] = L[-1], L[0]
    return L
print(list())