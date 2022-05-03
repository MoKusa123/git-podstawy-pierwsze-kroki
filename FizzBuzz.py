def FizzBuzz():
    for item in range(1, 100, 1):
        if item % 3 == 0 and item % 5 == 0:
            print('fizzbuzz', end=' ')
        elif item % 3 == 0:
            print('fizz', end=' ')
        elif item % 5 == 0:
            print('buzz', end=' ')
        else:
            print(item, end=' ')

FizzBuzz()
