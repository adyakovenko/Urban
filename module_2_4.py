numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = [], []
for ind in range(len(numbers)):
    if numbers[ind] == 1:
        continue
    max_val_to_check = numbers[ind] // 2
    is_prime = True
    for divider in range(2, max_val_to_check + 1):
        if numbers[ind] % divider == 0:
            is_prime = False
            not_primes.append(numbers[ind])
            break
    if is_prime:
        primes.append(numbers[ind])
print('Primes:', primes)
print('Not Primes:', not_primes)