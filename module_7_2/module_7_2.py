def custom_write(file_name, strings):
    fs = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for ind in range(len(strings)):
        strings_positions[(ind+1, fs.tell())] = strings[ind]
        fs.write(f'{strings[ind]}\n')
    fs.close()
    return strings_positions



if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)