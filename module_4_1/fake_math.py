def divide(first, second):
    return first / second if second != 0 else 'Ошибка'


def main():
    print(divide(1, 2))
    print(divide(1, 0))


if __name__ == '__main__':
    main()
