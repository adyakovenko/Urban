number1, number2, number3 = int(input()), int(input()), int(input())
if number1 == number2 and number1 == number3:
    print(3)
elif number1 == number2 or number1 == number3 or number2 == number3:
    print(2)
else:
    print(0)