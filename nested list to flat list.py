
nested_lst = [1, [2, [[3, 4], 5]], [6, 7]]
flattened_lst = []

def flatten(lst):
    for i in lst:
        if type(i) == list:
            flatten(i)
        else:
            flattened_lst.append(i)
flatten(nested_lst)
print(flattened_lst)
