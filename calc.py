

while(1):

    a=float(input('Enter a number: '))
    b=float(int(input('Enter another number: ')))

    print('''
        Operator list:
            For addition press +
            For subtraction press -
            For multiplication press *
            For division press /
            For exiting press e 
    ''')

    op=input('Enter operator: ')

    result = 0

    match(op):
        case '+': result = a+b
        case '-': result = a-b
        case '*': result = a*b
        case '/': result = a/b
        case 'e': break
        case _: print('Invalid operator')

    print(f'{a}{op}{b} = {result}')