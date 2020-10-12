
result = []

for itm in range(10):
    if itm & 1:  # побитовое сравнение 0001 and (нечетное число)
        result.append(itm)

print(result)

result2 = [itm for itm in range(10) if itm & 1]
print(result2)

def my_map(func, iter_object):
    for itm in iter_object:
        yield func(itm) # возврат промежуточных значений

print(list(my_map(lambda x: x ** 2 , range(10))))

def some(x):
    yield  x - 2
    yield x - 3
    yield  x - 4