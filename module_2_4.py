numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = [], []
for number in numbers:
    if number == 1:
        continue
    max_val_to_check = number // 2
    is_prime = True
    for divider in range(2, max_val_to_check + 1):
        if number % divider == 0:
            is_prime = False
            not_primes.append(number)
            break
    if is_prime:
        primes.append(number)
print('Primes:', primes)
print('Not Primes:', not_primes)