first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(val[0]) - len(val[1]) for val in zip(first, second) if len(val[0]) != len(val[1]))
second_result = (len(first[ind]) == len(second[ind]) for ind in range(len(first)))

print(list(first_result))
print(list(second_result))