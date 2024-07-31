immutable_var = 1, 2, 'a', 'b'
print('Immutable tuple:', immutable_var)
try: immutable_var[0] = 8
except Exception as e: print("Can't change values in " + str(type(immutable_var))[8:13]+ "!")
mutable_list = [0, 2, 'a', 'b']
mutable_list[0] += 1
mutable_list.append('Modified')
print('Mutable list:', mutable_list)