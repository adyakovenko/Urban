def is_prime(func):
    def wrapper(*vals):
        number = func(*vals)
        flag_prime = True
        for n in range(2, number//2):
            if number % n == 0:
                flag_prime = False
                break
        print('Простое') if flag_prime else print('Составное')
        return number
    return wrapper


@is_prime
def sum_three(*vals):
    return sum(vals)


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
