

def calculate(x, y):
    # uncomment to use operator inside function
    # operator = input('select operator +,-,*,/ : ')
    result = 0
    if operator == '+':
        result = x+y
    elif operator == '-':
        result = x-y
    elif operator == '*':
        result = x*y
    elif operator == '/':
        if y == 0:
            print('error! cannot divide by zero !!')
            result = 'not defined'
        else:
            result = x/y
    return result


while True:
    num1 = int(input('enter first number :'))
    operator = input('select operator +,-,*,/ : ')
    num2 = int(input('enter second number :'))
    print(f'{num1}{operator}{num2} = {calculate(num1, num2)}')
    while True:
        option = input('enter again(y/n)')
        if option == 'y' or option == 'Y':
            break
        elif option == 'n' or option == 'N':
            exit()
        else:
            print('please enter (y/n) only!!')
            continue
