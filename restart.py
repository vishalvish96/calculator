num = int(input('enter any number: '))
arm = 0
n = num
while (num > 0):
    rem = num % 10
    arm = arm+(num**3)
    num = num/10
if (arm == n):
    print('it is a armstrong')
else:
    print('it is not armstrong')
