

while(1):

    print('Welcome to Python Calulator !\nPress c to continue\nPress e to exit')

    choice = input()

    if choice=='e': break

    a=float(input('Enter a number: '))
    b=float(int(input('Enter another number: ')))

    print('''
        Operator list:
            For addition press +
            For subtraction press -
            For multiplication press *
            For division press /
            For modulo press %
    ''')

    op=input('Enter operator: ')

    result = 0

    match(op):
        case '+': result = a+b
        case '-': result = a-b
        case '*': result = a*b
        case '/': 
            if b==0: 
                print('Cannot divide by zero')
                continue
            else: result = a/b
        case '%': result = a%b
        case _: 
            print('Invalid operator')
            continue

    print(f'{a} {op} {b} = {result}')