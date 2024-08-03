calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(line):
    count_calls()
    return len(line), line.upper(), line.lower()


def is_contains(line, lines):
    count_calls()
    return line.lower() in [val.lower() for val in lines]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
