my_dict = {'Johny Depp': 1963, 'Tommy Lee Jones': 1946, 'Tom Hanks': 1956, 'Julia Roberts': 1967, 'Bill Murray': 1950}
print('Dict:', my_dict)
print('Existing value"', my_dict.get('Johny Depp'))
print('Not existing value:', my_dict.get('Bruce Willis'))
my_dict.update({'Bruce Willis': 1955, 'Sandra Bullock': 1964})
value = my_dict.pop('Johny Depp')
print('Deleted value:', value)
print('Modified dictionary: ', my_dict, '\n')

my_set = {'dinosaur', 65, int(23), float(23.0), 23}
print('Set:', my_set)
my_set.update({'cat', 'fish'})
my_set.discard(65)
print('Modified set:', my_set)

