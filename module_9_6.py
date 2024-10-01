import itertools


def all_variants(text):
    for n_letters in range(1, len(text) + 1):
        for start in range(len(text)):
            if start + n_letters < len(text) + 1:
                yield text[start:start + n_letters]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)
