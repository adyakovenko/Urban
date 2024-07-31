# computation
def get_dividers(number):
    dividers = [val for val in range(1, number // 2 + 1) if number % val == 0]
    dividers.append(number)
    return dividers


def get_code(number):
    pairs = []
    dividers = get_dividers(number)
    for divider in dividers:
        for val1 in range(1, divider // 2 + 1):
            val2 = divider - val1
            if val1 < val2:
                pairs.append([val1, val2])
    return sorted(pairs)


def convert_code_to_string(code):
    return ''.join([f'{pair[0]}{pair[1]}' for pair in code])


def auto_check():
    # check the correct answer

    # paste and separate values from task
    correct_answer_raw = '''3 - 12
    4 - 13
    5 - 1423
    6 - 121524
    7 - 162534
    8 - 13172635
    9 - 1218273645
    10 - 141923283746
    11 - 11029384756
    12 - 12131511124210394857
    13 - 112211310495867
    14 - 1611325212343114105968
    15 - 1214114232133124115106978
    16 - 1317115262143531341251161079
    17 - 11621531441351261171089
    18 - 12151811724272163631545414513612711810
    19 - 118217316415514613712811910
    20 - 13141911923282183731746416515614713812911'''
    correct_answer = [line.split(' - ')[1] for line in correct_answer_raw.split('\n')]

    # check if correct answers match computations
    for val in range(3, 21):
        computed = convert_code_to_string(get_code(val))
        if computed == correct_answer[val - 3]:
            print(f'n = {val} верно')
        else:
            print(f'n = {val} !!!!! ОШИБКА !!!!!')


# input parameters
check_all = False

if check_all:
    auto_check()
else:
    n = 1
    while n != 0:
        n = int(input("Введите число из первой вставки или 0 для выхода: "))
        result = convert_code_to_string(get_code(n))
        print(result)
