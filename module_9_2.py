first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(val) for val in first_strings if len(val) >= 5]
second_result = [(val1, val2) for val1 in first_strings for val2 in second_strings if len(val1) == len(val2)]
third_result = {val: len(val) for val in first_strings + second_strings if not len(val) % 2}

print(first_result)
print(second_result)
print(third_result)