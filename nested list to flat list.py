
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

def flatten (*n):
    return (e for a in n for e in (flatten(*a)if isinstance(a,(tuple, list)) else (a, )))

if __name__ == '__main__':
    inp = [1,(2, [[3, 4], [5, 6]]), [7, [[8, 9], 10]],["salam",("hi", 50000)]]
    out = []
    print(flatten(inp))
for i in flatten(inp):
    out.append(i)
print(out)
