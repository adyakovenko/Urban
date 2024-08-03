def get_multiplied_digits(number):
    str_number = str(number).replace('0', '')
    first = int(str_number[0])
    first = 1 if first == 0 else first
    if len(str_number) == 1:
        return int(first)
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)