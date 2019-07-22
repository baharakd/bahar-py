
infinito_power = (num**2 for num in range(0, 1000000))

print(infinito_power.__next__())
print(infinito_power.__next__())
print(infinito_power.__next__())
print(next(infinito_power))
print(next(infinito_power))
print(next(infinito_power))

def pick_one_element(n):
    list_of_generator = []
    infinito_power = (num ** 2 for num in range(0, 1000000))
    for i in range(0,n):
        list_of_generator.append(next(infinito_power))
    return list_of_generator[-1]

print("thats the element you picked : ", pick_one_element(5))


