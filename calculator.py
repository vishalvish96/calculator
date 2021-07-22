import math


def add(a, b):
    return (a+b)


def sub(a, b):
    if a > b:
        return (a-b)
    else:
        return (b-a)


def mul(a, b):
    return(a*b)


def div(a, b):
    r = a % b
    q = a/b
    print('remainder', r)
    print('quotient', q)


def sqrt(a):
    return math.sqrt(a)


while True:
    print('\n\n Choose the operation ')
    print('\n\t1.Addition')
    print('\n\t2.Subtraction')
    print('\n\t3.Multiplication')
    print('\n\t4.Divison')
    print('\n\t5.Square_Root')
    print('\n\t6.Exit')

    choice = int(input('Enter your choice:'))
    if choice == 1:
        a = int(input('enter the value of a:'))
        b = int(input('enter athe value of b:'))
        print('result=', add(a, b))
    elif choice == 2:
        a = int(input('enter the value of a:'))
        b = int(input('enter athe value of b:'))
        print('result=', sub(a, b))
    elif choice == 3:
        a = int(input('enter the value of a:'))
        b = int(input('enter athe value of b:'))
        print('result=', mul(a, b))
    elif choice == 4:
        a = int(input('enter the value of a:'))
        b = int(input('enter athe value of b:'))
        print(div(a, b))
    elif choice == 5:
        a = int(input('enter the value of a:'))

        print(sqrt(a, b))
    else:
        print('You choose to exit\n GOOD BYE')
        break
