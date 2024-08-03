def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# ---------- task 1 ----------

print_params('Невяное', 'преобразование', 'типов')
print_params('кажется', 'опасным?', )
print_params(b=25)
print_params(c=[1, 2, 3])

# ---------- task 2 ----------

values_list = [1, 'y', True]
values_dict = {'a': 1, 'b': 'y', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# ---------- task 3 ----------

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)