types_containers = (list, tuple, set)
types_numbers = (int, float, complex)


def compute_internal_sum(data, internal_sum=0):
    if type(data) in types_numbers:
        return internal_sum + data
    elif type(data) is str:
        return internal_sum + len(data)
    elif type(data) in types_containers:
        return internal_sum + sum(compute_internal_sum(val) for val in data)
    elif type(data) is dict:
        return internal_sum + sum(len(val) for val in data.keys()) + sum(compute_internal_sum(val) for val in data.values())


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(compute_internal_sum(data_structure))
